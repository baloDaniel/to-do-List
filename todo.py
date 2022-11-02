from tkinter import*
from tkinter import ttk


class toDo:
    def __init__(self, root):
        self.root = root
        self.root.title = "To-Do-List"
        self.root.geometry("600x400+30+10")

        self.label = Label(self.root, text="To-Do-List-App", bd=5, font='TimesNewRoman, 16', width=10,
                          bg="purple", fg="black")
        self.label.pack(side="top", fill=BOTH)

        # Label for Text line input (type new task)

        self.label2 = Label(self.root, text="Type new task:", bd=6, font='TimesNewRoman, 14', width=15,
                            bg="orange", fg="black")
        self.label2.place(x=13, y=50)

        # Label for your tasks

        self.label3 = Label(self.root, text="Your tasks:", bd=6, font='TimesNewRoman, 14', width=15,
                            bg="orange", fg="black")
        self.label3.place(x=350, y=50)

        # Listbox

        self.main_text = Listbox(height=90, width=25, bd=5, font="TimesNewRoman, 14")
        self.main_text.place(x=295, y=90)

        # Text line input

        self.text = Text(height=2, width=25, bd=4, font="TimesNewRoman, 12")
        self.text.place(x=10, y=90)

#add task function

        def addNewTask():
            newTask = self.text.get(1.0, END)
            self.main_text.insert(END, newTask)
            with open("tasks.txt", "a") as file:
                file.write(newTask)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

#delete a task

        def deleteTask():
            delete = self.main_text.curselection()
            currentTask = self.main_text.get(delete)
            with open("tasks.txt", "r+") as g:
                new_g = g.readlines()
                g.seek(0) #we set the reference point at the beginning of the file
                for line in new_g:
                    item = str(currentTask)
                    if item not in line:
                        g.write(line)
                g.truncate()
            self.main_text.delete(delete)

        with open ("tasks.txt", "r") as file:
            read = file.readlines()
            for i in read:
                done = i.split()
                self.main_text.insert(END, done)
                file.close()

        self.button = Button(self.root, text="Add", font="ariel, 13",
                             width=10, height=2, bg="red", fg="black", command=addNewTask() )
        self.button.place(x=60, y=270)

        self.button2 = Button(self.root, text="Delete", font="ariel, 13",
                             width=10, height=2, bg="green", fg="black", command=deleteTask )
        self.button2.place(x=60, y=180)






def main():
    root = Tk()
    ui = toDo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
