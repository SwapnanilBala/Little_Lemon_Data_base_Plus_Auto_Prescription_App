from tkinter import *
import openpyxl
from openpyxl import load_workbook
from docx import *



# Initialize the main window
soft = Tk()
soft.title("Patient Information Form")

# Configure grid for better alignment
soft.grid_columnconfigure(0, weight=1)
soft.grid_columnconfigure(7, weight=1)

# Labels
patients_name = Label(soft, text="Enter the patient's name", font=("Ariel", 20), fg="Red")
patients_name.grid(row=1, column=1, padx=5, pady=5, sticky="w")

patients_age = Label(soft, text="Please enter the patient's age", font=("Ariel", 20), fg="Black")
patients_age.grid(row=1, column=2, padx=5, pady=5, sticky="w")

patients_sex = Label(soft, text="Gender of the patient", font=("Ariel", 20), fg="Red")
patients_sex.grid(row=1, column=3, padx=5, pady=5, sticky="w")

date = Label(soft, text="Type in today's date", font=("Ariel", 20), fg="Black")
date.grid(row=1, column=4, padx=5, pady=5, sticky="w")

doctors_name = Label(soft, text="Dr. Kamalesh Bala", font=("Calibri", 32), fg="Blue")
doctors_name.grid(row=0, column=1, columnspan=2, pady=10)

license_number = Label(soft, text="License: LKGM647GH82", font=("Calibri", 22), fg="Blue")
license_number.grid(row=0, column=3, columnspan=2, pady=10)

primary_diagnosis_label = Label(soft, text="Primary Diagnosis", font=("Calibri", 22))
primary_diagnosis_label.grid(row=3, column=1, columnspan=2, pady=5)

medicines_label = Label(soft, text="Prescribed Medicines", font=("Ariel", 22))
medicines_label.grid(row=3, column=3, columnspan=2, pady=5)

# Entry Fields
patient_name_entry = Entry(soft, font=("Ariel", 18), width=20)
patient_name_entry.grid(row=2, column=1, padx=5, pady=5)

patient_age_entry = Entry(soft, font=("Ariel", 18), width=20)
patient_age_entry.grid(row=2, column=2, padx=5, pady=5)

patients_sex_entry = Entry(soft, font=("Ariel", 18), width=20)
patients_sex_entry.grid(row=2, column=3, padx=5, pady=5)

date_entry = Entry(soft, font=("Ariel", 18), width=20)
date_entry.grid(row=2, column=4, padx=5, pady=5)

primary_diagnosis = Entry(soft, font=("Ariel", 18), width=40)
primary_diagnosis.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

medicines_prescribed = Entry(soft, font=("Ariel", 18), width=40)
medicines_prescribed.grid(row=4, column=3, columnspan=2, padx=10, pady=10)

# Functions
def name_submission():
    global name
    name = patient_name_entry.get()
    return

def age_submission():
    global age
    age = patient_age_entry.get()
    return

def gender_submission():
    global sex
    sex = patients_sex_entry.get()
    return

def date_submission():
    global date
    date = date_entry.get()
    return

def diagnosis_submission():
    global diagnosis
    diagnosis = primary_diagnosis.get()
    return

def medicines_submission():
    global medicines
    medicines = medicines_prescribed.get()
    return

def block_execution():
    global name,age,sex,date,diagnosis,medicines
    name_submission()
    age_submission()
    gender_submission()
    date_submission()
    diagnosis_submission()
    medicines_submission()
    name = name
    age = age
    sex = sex
    date = date
    diagnosis = diagnosis
    medicines = medicines
    wb = load_workbook(r"C:\Users\GOGOL\Documents\My Projects copy\Medical_Records.xlsx")
    sheet = wb.active
    new_row = [name,age,sex,date,diagnosis,medicines]
    sheet.append(new_row)
    wb.save(r"C:\Users\GOGOL\Documents\My Projects copy\Medical_Records.xlsx")

    clear_all()
    return

def clear_all():
    patient_name_entry.delete(0, END)
    patient_age_entry.delete(0, END)
    patients_sex_entry.delete(0, END)
    date_entry.delete(0, END)
    primary_diagnosis.delete(0, END)
    medicines_prescribed.delete(0, END)

# Buttons
final = Button(soft, text="Submit All", width=12, borderwidth=4, font=("Ariel", 20), command=block_execution)
final.grid(row=6, column=2, pady=20)

clear = Button(soft, text="Clear All", width=12, borderwidth=4, font=("Ariel", 20), command=clear_all)
clear.grid(row=6, column=3, pady=20)

# Main Loop
soft.mainloop()
