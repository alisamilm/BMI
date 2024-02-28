from tkinter import *
def mainwindow():
    main = Tk()
    main.geometry("300x400")
    main.title("BMI")
    main.rowconfigure((0,1,2,3,4), weight=1)
    main.columnconfigure(0, weight=1)
    main.config(bg="green")
    main.option_add("*Font", "times 15 bold")
    return main

def createframe(main):
    Label(main, text="BMI APP", bg="lightgreen").grid(row=0, column=0, sticky=N)
    frame_1 = Frame(main, bg="white")
    frame_1.grid(row=1, column=0, sticky="NEWS", padx=10, pady=10, ipady=5)

    frame_2 = Frame(main, bg="white")
    frame_2.grid(row=2, column=0, sticky="NEWS", padx=10, pady=10, ipady=5)

    frame_3 = Frame(main, bg="white")
    frame_3.grid(row=3, column=0, sticky="NEWS", padx=10, pady=10, ipady=20)

    frame_bottom = Frame(main, bg="white")
    frame_bottom.grid(row=4, column=0, sticky="NEWS", padx=10, pady=10, ipady=20)
    frame_bottom.columnconfigure(0, weight=0)
    frame_bottom.columnconfigure(1, weight=2)
    return frame_1, frame_2, frame_3, frame_bottom

def widget(frame_1, frame_2, frame_3, frame_bottom):
    Label(frame_1, text="HEIGHT:(cm.)").grid(row=0, column=0, padx=5, pady=5, sticky=W)
    ent_height = Entry(frame_1, bg="pink", textvariable=height_var)
    ent_height.grid(row=1, column=0, ipadx=40, padx=10, sticky=N+W)

    Label(frame_2, text="WEIGHT:(kg.)").grid(row=0, column=0, padx=5, pady=5, sticky=W)
    ent_weight = Entry(frame_2, bg="lightblue", textvariable=weight_var)
    ent_weight.grid(row=1, column=0, ipadx=40, padx=10, sticky=N+W)

    Label(frame_3, text="BMI").grid(row=0, column=0, padx=5, pady=5,sticky=W)
    show_data = Label(frame_3)
    show_data.grid(row=1, column=0, ipadx=40, padx=10, sticky=N+W)

    Button(frame_bottom, text="Calculate", highlightbackground="lightgreen", fg="white", command=find_bmi).grid(row=2, column=1)
    return ent_height, ent_weight, show_data


def find_bmi():
    height = height_var.get()
    weight = weight_var.get()
    # check height and weight filled in
    if height and weight:
        height = float(height) / 100.0
        bmi = round(float(weight) / height ** 2, 2)
        show_data.config(text = bmi)
    else:
        show_data.config(text='')


main = mainwindow()
height_var = StringVar()
weight_var = StringVar()
frame_1, frame_2, frame_3, frame_bottom = createframe(main)
ent_height, ent_weight, show_data = widget(frame_1, frame_2, frame_3, frame_bottom)
main.mainloop()