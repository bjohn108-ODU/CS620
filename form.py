import tkinter as tk
from tkinter import messagebox
import pandas as pd
import threading
import recommender


df = pd.DataFrame()
def getData():
    global df
    df = pd.read_csv("https://raw.githubusercontent.com/bjohn108-ODU/CS620/refs/heads/main/CleanData.csv")

reader = threading.Thread(target=getData)
reader.start()

window = tk.Tk()
window.title("Youth Behavior Obesity Risk Assessment")
bg_color = "#fff5bf"
hover_color = "#96fff8"
window.configure(bg=bg_color)
window.geometry("800x600")

location_label = tk.Label(window, text="Location", bg = bg_color)
location_label.pack()
location_options= [ "Prefer not to say",
                    "Alabama",
                    "Alaska",
                    "Arizona",
                    "Arkansas",
                    "California",
                    "Colorado",
                    "Connecticut",
                    "Delaware",
                    "District of Columbia",
                    "Florida",
                    "Georgia",
                    "Guam",
                    "Hawaii",
                    "Idaho",
                    "Illinois",
                    "Indiana",
                    "Iowa",
                    "Kansas",
                    "Kentucky",
                    "Louisiana",
                    "Maine",
                    "Maryland",
                    "Massachusetts",
                    "Michigan",
                    "Mississippi",
                    "Missouri",
                    "Montana",
                    "National",
                    "Nebraska",
                    "Nevada",
                    "New Hampshire",
                    "New Jersey",
                    "New Mexico",
                    "New York",
                    "North Carolina",
                    "North Dakota",
                    "Ohio",
                    "Oklahoma",
                    "Pennsylvania",
                    "Puerto Rico",
                    "Rhode Island",
                    "South Carolina",
                    "South Dakota",
                    "Tennessee",
                    "Texas",
                    "Utah",
                    "Vermont",
                    "Virgin Islands",
                    "Virginia",
                    "West Virginia",
                    "Wisconsin",
                    "Wyoming"
                ]
location_entry = tk.StringVar()
location_entry.set("Select an option")  # Set default value
location_drop = tk.OptionMenu( window , location_entry , *location_options ) 
location_drop.configure(activebackground=hover_color)
location_drop.pack() 

race_label = tk.Label(window,text="Race/Ethnicity", bg=bg_color)
race_label.pack()
race_options=[
    "Prefer not to say"  
    "American Indian/Alaska Native",
    "Asian",
    "Hawaiian/Pacific Islander",
    "Hispanic",
    "Non-Hispanic Black",
    "Non-Hispanic White"
]
race_entry = tk.StringVar()
race_entry.set("Select an option")
race_drop = tk.OptionMenu( window, race_entry, *race_options )
race_drop.configure(activebackground=hover_color)
race_drop.pack()

gender_label = tk.Label(window, text="Sex", bg=bg_color)
gender_label.pack()
gender_options = [
    "Prefer not to say",
    "Male",
    "Female"
]
gender_entry = tk.StringVar()
gender_entry.set("Select an option")
gender_drop = tk.OptionMenu(window, gender_entry, *gender_options)
gender_drop.configure(activebackground=hover_color)
gender_drop.pack()

grade_label = tk.Label(window, text="Grade", bg=bg_color)
grade_label.pack()
grade_options = [
    "Prefer not to say",
    "9th",
    "10th",
    "11th",
    "12th"
]
grade_entry = tk.StringVar()
grade_entry.set("Select an option")
grade_drop = tk.OptionMenu(window, grade_entry, *grade_options)
grade_drop.configure(activebackground=hover_color)
grade_drop.pack()



questions_label = tk.Label(window, text="Behavioral Questions:", bg=bg_color)
questions_label.pack()
question_options = [
    "Yes",
    "No"
]


q1_label = tk.Label(window, text = "Do you eat at least one vegetable per day on average?", bg=bg_color)
q1_label.pack()
q1_options = question_options
q1_entry = tk.StringVar()
q1_entry.set("Select an Option")
q1_drop = tk.OptionMenu(window, q1_entry, *q1_options)
q1_drop.configure(activebackground=hover_color)
q1_drop.pack()

q2_label = tk.Label(window, text = "Do you eat at least one fruit per day on average?", bg=bg_color)
q2_label.pack()
q2_options = question_options
q2_entry = tk.StringVar()
q2_entry.set("Select an Option")
q2_drop = tk.OptionMenu(window, q2_entry, *q2_options)
q2_drop.configure(activebackground=hover_color)
q2_drop.pack()

q3_label = tk.Label(window, text = "Do you drink at least one soda per day on average?", bg=bg_color)
q3_label.pack()
q3_options = question_options
q3_entry = tk.StringVar()
q3_entry.set("Select an Option")
q3_drop = tk.OptionMenu(window, q3_entry, *q3_options)
q3_drop.configure(activebackground=hover_color)
q3_drop.pack()

q4_label = tk.Label(window, text = "Do you watch TV for at least three hours per day on average?", bg=bg_color)
q4_label.pack()
q4_options = question_options
q4_entry = tk.StringVar()
q4_entry.set("Select an Option")
q4_drop = tk.OptionMenu(window, q4_entry, *q4_options)
q4_drop.configure(activebackground=hover_color)
q4_drop.pack()

q5_label = tk.Label(window, text = "Do you engage in at least one hour of moderate to intense physical activity per day on average?", bg=bg_color)
q5_label.pack()
q5_options = question_options
q5_entry = tk.StringVar()
q5_entry.set("Select an Option")
q5_drop = tk.OptionMenu(window, q5_entry, *q5_options)
q5_drop.configure(activebackground=hover_color)
q5_drop.pack()

q6_label = tk.Label(window, text = "Do you participate in at least one hour of Physical Education per day on average?", bg=bg_color)
q6_label.pack()
q6_options = question_options
q6_entry = tk.StringVar()
q6_entry.set("Select an Option")
q6_drop = tk.OptionMenu(window, q6_entry, *q6_options)
q6_drop.configure(activebackground=hover_color)
q6_drop.pack()

def submit():
    location = location_entry.get()
    stratifications = []
    stratifications.append(race_entry.get())
    stratifications.append(gender_entry.get())
    stratifications.append(grade_entry.get())

    responses = []
    responses.append(q1_entry.get())
    responses.append(q2_entry.get())
    responses.append(q3_entry.get())
    responses.append(q4_entry.get())
    responses.append(q5_entry.get())
    responses.append(q6_entry.get())

    if location == "Select an option":
        messagebox.showwarning("Warning", "Please select an option for all questions")
    
    for i in stratifications:
        if i == "Select an option":
            messagebox.showwarning("Warning", "Please select an option for all questions")
            return

    for i in responses:
        if i == "Select an option":
            messagebox.showwarning("Warning", "Please select an option for all questions")
            return

    reader.join()
    recommendation = recommender.recommend(location, stratifications, responses, df)
    message = ""
    if(recommendation[0] == recommendation[1]):
        message = "To best reduce your risk of obesity and overweight status, " + recommendation[0]
        #print("To best reduce your risk of obesity and overweight status, ", recommendation[0])
    else:
        message = "To best reduce your risk of obesity, " + recommendation[0] + "\nTo best reduce your risk of overweight status, " + recommendation[1]
        #print("To best reduce your risk of obesity, ", recommendation[0], "\nTo best reduce your risk of overweight status, ", recommendation[1])
    messagebox.showinfo("Results", message)
    window.destroy()

submit_button = tk.Button(window, text="Submit", command=submit, bg="red", fg="white", activebackground="blue", activeforeground="white", font=("Times New Roman", 25))
submit_button.pack()

window.mainloop()