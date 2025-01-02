from tkinter import *

soft = Tk()

patients_name = Label(soft, text = "  Enter the patient's name  ",font=("Ariel",20), fg = "Red")
patients_name.grid(row = 1 ,column = 1, padx = 5,pady = 5)
patients_age = Label(soft, text = "  Please enter the patient's age  ",font=("Ariel",20), fg = "Black")
patients_age.grid(row = 1 ,column = 2, padx = 5,pady = 5)
patients_sex = Label(soft, text = "  Gender of the patient  ", font=("Ariel",20), fg = "Red")
patients_sex.grid(row = 1 ,column = 3, padx = 5,pady = 5)
date = Label(soft,text = "  type in today's date  ",font=("Ariel",20), fg = "Black")
date.grid(row = 1 ,column = 4, padx = 5,pady = 5)
doctors_name = Label(soft,text = " Dr. Kamalesh Bala ", font = ("Calibri",32),fg = "Blue")
doctors_name.grid(row = 1 ,column = 5, padx = 5,pady = 5)
license_number = Label(soft, text = " LKGM647GH82 ",font = ("Calibri",22),fg = "Blue")
license_number.grid(row = 1 ,column = 6, padx = 5,pady = 5)
primary_diagnosis = Label(soft,text = " Diagnosis ", font = ("Calibri",22))
primary_diagnosis.grid(row = 3, column = 2, padx = 5, pady = 5)
medicines = Label(soft,text = " Diagnosis ", font = ("Calibri",22))
medicines.grid(row = 3, column = 4, font = ("Calibri",22))



patient_name_entry = Entry(soft)
patient_name_entry.grid(row = 2 ,column = 1, padx = 5,pady = 5)
patient_age_entry = Entry(soft)
patient_age_entry.grid(row = 2 ,column = 2, padx = 5,pady = 5)
patients_sex_entry = Entry(soft)
patients_sex_entry.grid(row = 2 ,column = 3, padx = 5,pady = 5)
date_entry = Entry(soft)
date_entry.grid(row = 2 ,column = 4, padx = 5,pady = 5)
primary_diagnosis = Entry(soft)
primary_diagnosis.grid(row = 4, column = 2, padx =10, pady = 30)
medicines_prescribed = Entry(soft)
medicines_prescribed.grid(row = 4, column = 4,padx =10, pady = 30)



def name_submission():
	global name
	name = patient_name_entry.get()
	return

def age_submission():
	global age
	age = patient_name_entry.get()
	return

def gender_submission():
	global sex
	sex = patient_name_entry.get()
	return

def date_submission():
	global date
	date = patient_name_entry.get()
	return

def diagnosis_submission():
	global diagnosis
	diagnosis = patient_name_entry.get()
	return

def medicines_submission():
	global medicines
	medicines = medicines_prescribed.get()
	return

def block_execution():
	name_submission()
	age_submission()
	gender_submission()
	date_submission()
	diagnosis_submission()
	medicines_submission()










soft.mainloop()

if __name__ == "__main__":
	mainloop()
