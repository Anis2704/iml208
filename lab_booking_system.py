import tkinter
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import messagebox

def enter_data():
    accepted = accept_var.get()

    if accepted=="Accepted":
        #user info
         firstname= first_name_entry.get()
         lastname = last_name_entry.get()
         
         if firstname and lastname:
            matric_label = matric_no.get()
            faculty_label = faculty_combobox.get()
            programme_label = programme_combobox.get()
            semesters_label = semesters_spinbox.get()

            #lab booking
            lab_label = lab_combobox.get()

            print("First name:", firstname, "Last name:", lastname)
            print("Matric no:", matric_label, "Faculty:", faculty_label, "Programme:", programme_label)
            print("Semester:", semesters_label)
            print("----------------------------------------")
            tkinter.messagebox.showinfo(title="Success", message="Your booking is successful!")
         else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
        
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms.")
    

window = tkinter.Tk()
window.title("Lab Booking Registration")

frame = tkinter.Frame(window)
frame.pack()

#saving user info
user_info_frame =tkinter.LabelFrame(frame, text="User Informatiton")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1) 

matric_label = tkinter.Label(user_info_frame, text="Matric no")
matric_no = tkinter.Entry(user_info_frame)
matric_label.grid(row=0, column=2)
matric_no.grid(row=1, column=2)

faculty_label = tkinter.Label(user_info_frame, text="Faculty")
faculty_combobox = ttk.Combobox(user_info_frame, values=["Business & Management", "Science & Technology", "Social Science & Humanities"])
faculty_label.grid(row=2, column=0)
faculty_combobox.grid(row=3, column=0)

programme_label = tkinter.Label(user_info_frame, text="Programme")
programme_combobox = ttk.Combobox(user_info_frame, value= ["Diploma", "Degree"])
programme_label.grid(row=2, column=1)
programme_combobox.grid(row=3, column=1)

semesters_label = tkinter.Label(user_info_frame, text="Semester")
semesters_spinbox = tkinter.Spinbox(user_info_frame, from_=1, to=6)
semesters_label.grid(row=2,column=2)
semesters_spinbox.grid(row=3, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#lab booking
lab_frame = tkinter.LabelFrame(frame)
lab_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

lab_label = tkinter.Label(lab_frame, text="Select lab:")
lab_label.grid(row=1, column=0)
lab_combobox = ttk.Combobox(lab_frame, value=["Lab A", "Lab B", "Lab C"])
lab_combobox.grid(row=1, column=1)

#date selection
date_frame = ttk.LabelFrame(lab_frame, text="Date Selection")
date_frame.grid(row=2, column=1)
date_entry = Calendar(date_frame, selectmode="day", date_pattern="yyyy-mm-dd")
date_entry.grid(row=2, column=2)

#time selection
time_frame = ttk.LabelFrame(lab_frame, text="Time Selection")
time_frame.grid(row=3, column=1)
time_selection = ttk.Combobox(time_frame, values=["8-10 am", "10-12 am", "12-2 pm", "2-4 pm", "4-6 pm", "6-8 pm", "8-10 pm"])
time_selection.grid(row=3, column=2)

#accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable=accept_var, onvalue="Accepted", offvalue="Not accepted")
terms_check.grid(row=0, column=0)

#buttons
button_enter = tkinter.Button(frame, text="Finish booking", command= enter_data)
button_enter.grid(row=3, column=0, sticky="news", padx=10, pady=10)

button_edit = tkinter.Button(frame, text="Edit booking", command= enter_data)
button_edit.grid(row=3, column=1, sticky="news", padx=10, pady=10)

button_delete = tkinter.Button(frame, text="Delete booking", command= enter_data)
button_delete.grid(row=3, column=3, sticky="news", padx=10, pady=10)

window.mainloop()