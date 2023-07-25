
from tkinter import *
from tkinter import ttk
from math import ceil
import json
from tkinter import messagebox

def calculate_dailyCalIntake(gender, weight, height, age, katchMult, weekWeightLoss):
    #bmr = 1
    try:
        if gender == "M":
            bmr = (10 * float(weight)) + (6.25 * float(height)) - (5 * age) + 5
        elif gender == "F":
            bmr = (10 * float(weight)) + (6.25 * float(height)) - (5 * age) - 161
        else:
            messagebox.showerror(title="Input Error", message="Error: Please enter F or M for gender")
    except ValueError:
        messagebox.showerror(title="Input Error", message="Error: Please enter a number for all inputs except gender")
    tdee = bmr * katchMult
    weekCalDeficit = weekWeightLoss * 7700
    dailyCalDeficit = weekCalDeficit / 7
    global dailyCalIntake
    dailyCalIntake = ceil(tdee - dailyCalDeficit)
    calculate_label.config(text="Daily Calorie Intake: " + str(dailyCalIntake))

def submit_gender():
    
    global gender
    gender = gender_entry.get().upper()
      
def submit_weight():
    try:
        global weight
        weight = float(weight_entry.get())
    except ValueError:
        messagebox.showerror(title="Input Error", message="Error: Please enter a number for weight")
    
def submit_height():
    try:
        global height
        height = float(height_entry.get())
    except ValueError:
        messagebox.showerror(title="Input Error", message="Error: Please enter a number for height")

def submit_age():
    try:
        global age
        age = int(age_entry.get())
    except ValueError:
        messagebox.showerror(title="Input Error", message="Error: Please enter a number for age")
    
def submit_katchMult():
    try:
        global katchMult
        katchMult = float(katchMult_entry.get())
    except ValueError:
        messagebox.showerror(title="Input Error", message="Error: Please enter a number for your activity multiplier")

def submit_weekWeightLoss():
    try:
        global weekWeightLoss
        weekWeightLoss = float(week_weight_loss_entry.get())
    except ValueError:
        messagebox.showerror(title="Input Error", message="Error: Please enter a number for your desired weekly weight loss")

def open_list_window():
    
    list_window = Toplevel()
    list_window.title("Food list and their calories")
    list_window.config(background="#c3e898", borderwidth=2)

    notebook = ttk.Notebook(list_window)
    notebook.pack(expand = True , fill = "both")

    global list_frame
    list_frame = Frame(list_window)
    list_frame.pack(expand = True , fill = "both")
    list_frame.config(background="#c3e898", borderwidth=2)

    add_food_button = Button(list_frame, text="ADD FOOD", command=add_food, font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
    add_food_button.grid(row=0, column=0, padx=5, pady=5)

    edit_food_button = Button(list_frame, text="EDIT FOOD", command=edit_food, font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
    edit_food_button.grid(row=0, column=1, padx=5, pady=5)

    refresh_button = Button(list_frame, text="REFRESH LIST", command=refresh_list, font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
    refresh_button.grid(row=0, column=2, padx=5, pady=5)

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('candara', 9)) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('candara', 10,'bold')) # Modify the font of the headings
    #style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

    global FoodCal_tree
    FoodCal_tree = ttk.Treeview(list_frame, columns=("Value"), style="mystyle.Treeview")
    FoodCal_tree.heading("#0", text="Food")
    FoodCal_tree.heading("Value", text="Calories")
   

    sorted_food_dict = {k: food_dict[k] for k in sorted(food_dict)}

    for key, value in sorted_food_dict.items():
        FoodCal_tree.insert("", "end", text=key, values=(value))

    FoodCal_tree.column("#0", width=160)
    FoodCal_tree.column("Value", width=160)
    FoodCal_tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def add_food():
    global add_food_window
    add_food_window = Toplevel()
    add_food_window.title("Add a Food")

    notebook = ttk.Notebook(add_food_window)
    notebook.pack(expand = True , fill = "both")

    add_food_frame = Frame(add_food_window)
    add_food_frame.pack(expand = True , fill = "both")
    add_food_frame.config(background="#c3e898", borderwidth=2)

    add_name_label = Label(add_food_frame, text = "ADD FOOD NAME:", background="#c3e898", font="candara 11")
    add_name_label.grid(row=0, column=0, padx=5, pady=5)

    global add_name_entry  
    add_name_entry = Entry(add_food_frame)
    add_name_entry.grid(row=1, column=0, padx=5, pady=5)

    add_name_button = Button(add_food_frame, text="Submit", command=get_food_name, font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
    add_name_button.grid(row=1, column=1, padx=5, pady=5)

    add_cal_label = Label(add_food_frame, text = "Add the food calorie amount:", background="#c3e898", font="candara 11")
    add_cal_label.grid(row=2, column=0, padx=5, pady=5)

    global add_cal_entry
    add_cal_entry = Entry(add_food_frame)   
    add_cal_entry.grid(row=3, column=0, padx=5, pady=5)

    add_cal_button = Button(add_food_frame, text="SUBMIT", command=get_food_cal, font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
    add_cal_button.grid(row=3, column=1, padx=5, pady=5)

    add_food_dict_button = Button(add_food_frame, text="ADD", command=add_new_food, font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
    add_food_dict_button.grid(row=4, column=0, padx=5, pady=5)

def get_food_name():
    global food_name
    food_name = add_name_entry.get()

def get_food_cal():
    global food_cal
    food_cal = int(add_cal_entry.get())   

def add_new_food():
    food_dict[food_name] = food_cal
    with open("food_list.json","w") as file:
        json.dump(food_dict, file)
    add_food_window.destroy()

def refresh_list():
    global FoodCal_tree
    FoodCal_tree.delete(*FoodCal_tree.get_children())
    FoodCal_tree = ttk.Treeview(list_frame, columns=("Value"))
    FoodCal_tree.heading("#0", text="Food")
    FoodCal_tree.heading("Value", text="Calories")

    global sorted_food_dict
    sorted_food_dict = {k: food_dict[k] for k in sorted(food_dict)}

    for key, value in sorted_food_dict.items():
        FoodCal_tree.insert("", "end", text=key, values=(value))

    FoodCal_tree.column("#0", width=160)
    FoodCal_tree.column("Value", width=160)
    
    FoodCal_tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def edit_food():
    global edit_food_window
    edit_food_window = Toplevel()
    edit_food_window.title("Edit a Food")

    notebook = ttk.Notebook(edit_food_window)
    notebook.pack(expand = True , fill = "both")

    edit_food_frame = Frame(edit_food_window)
    edit_food_frame.pack(expand = True , fill = "both")
    edit_food_frame.config(background="#c3e898", borderwidth=2)

    edit_food_label = Label(edit_food_frame, text = "Choose and edit a food:", background="#c3e898", font="candara 11")
    edit_food_label.grid(row=0, column=0,padx=5, pady=5)
   
    global edit_listbox
    edit_listbox = Listbox(edit_food_frame, font="candara 9", background="#eeeabf")
    edit_listbox.grid(row=1, column=0, padx=5, pady=5)

    sorted_food_dict = {k: food_dict[k] for k in sorted(food_dict)}

    for item in sorted_food_dict.keys():
        edit_listbox.insert("end", item)
    
    edit_listbox.bind("<<ListboxSelect>>", food_select)

    global edit_cal_entry
    edit_cal_entry = Entry(edit_food_frame, text="Change calories")
    edit_cal_entry.grid(row=2, column=0, padx=5, pady=5)
    
    edit_cal_button = Button(edit_food_frame, text="SUBMIT", command=get_cal, font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
    edit_cal_button.grid(row=2, column=1, padx=5, pady=5)

def food_select(event):
     selected_indices = edit_listbox.curselection()
     global selected_food
     if selected_indices:
        selected_index = selected_indices[0]
        selected_food = edit_listbox.get(selected_index)

def get_cal():
    new_cal = edit_cal_entry.get()
    food_dict[selected_food] = new_cal
    with open("food_list.json","w") as file:
        json.dump(food_dict, file)
    edit_food_window.destroy()

def sum_calories():
    global sum_window
    sum_window = Toplevel()
    sum_window.title("Sum")
    
    global sum_frame
    sum_frame = Frame(sum_window)
    sum_frame.pack(expand = True , fill = "both")
    sum_frame.config(background="#c3e898", borderwidth=2)

    global sum_listbox
    sum_listbox = Listbox(sum_frame, font="candara 9",background="#eeeabf")
    sum_listbox.pack(expand = True , fill = "both")

    for i in food_list:
        sum_listbox.insert(0, i)

    select_food_label = Label(sum_frame, text = "Select a food on the list, then press Add: ", background="#c3e898", font="candara 11")
    select_food_label.pack()

    sum_add_button = Button(sum_frame, text = "Add 1 unit", command=get_sum_add, font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
    sum_add_button.pack()

    global sum_label
    sum_label = Label(sum_frame, text = "", background="#c3e898", font="candara 11")
    sum_label.pack()

    remain_label1 = Label(sum_frame, text = "To calculate remaining daily calories,\n first calculate your Daily Calories Intake\n on Diet Plan Tab: ", background="#c3e898", font="candara 11")
    remain_label1.pack()

    remaining_button = Button(sum_frame, text="Calculate Remaining Calories", command=calculate_remain_cal, font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
    remaining_button.pack()

    global remain_label2
    remain_label2 = Label(sum_frame, text="", background="#c3e898", font="candara 11")
    remain_label2.pack()

def get_sum_add():
    
    sum_food_selected = sum_listbox.get(ANCHOR)
    sum_food_selected_short = sum_food_selected.split(':')[0].strip()

    
    sum_food_selected_cal = int(sorted_food_dict[sum_food_selected_short])

    global sum_total_cal  
    sum_total_cal += sum_food_selected_cal
    sum_label.config(text=sum_total_cal)

def calculate_remain_cal():
     global remaining_cal
     remaining_cal = dailyCalIntake - sum_total_cal
     remain_label2.config(text=remaining_cal)

sum_total_cal = 0   


with open("food_list.json","r") as file:
    food_dict = json.load(file)      

sorted_food_dict = {k: food_dict[k] for k in sorted(food_dict)}

food_list = [f"{key}: {value}" for key, value in sorted_food_dict.items()]


# food_dict =     { "White Rice (1/2 cup)" : 346 , "Butter (tbsp)" : 100 , "Olive Oil (tbsp)" : 109 , "Tomato" : 20 , "Spaghetti" : 210 , 
#                   "Yamani Rice (1/2 cup)" : 354 , "Wheat Bread (1 slice)" : 67 , "Spreadable Cheese (tbsp)" : 56 , "Egg" : 70 , 
#                   "Soft Cheese (slice)" : 90 , "Green beans (1/2 cup)" : 65 , "Lentils (1/2 cup)" : 115, "Beer (can)" : 200, 
#                   "Red Wine (250ml)" : 200 , "Pizza for One" : 474 , "Sweet Corn (1/2 cup)" : 75 , "Faina (2 portions)" : 212 , 
#                   "Cappelletti (1 cup)" : 311 , "Sauce (3 bsp)" : 28 , "Squash" : 31 , "Sweet Potato Jam (slice)" : 97 , 
#                   "Alfajor" : 205 , "Noisette Potato (9 u)" : 141 , "Peanuts (1/4 cup)" : 125 , "Banana" : 100 , "Rice Toast" : 31 , 
#                   "Mashed Potato (1/2 dish)" : 200 , "Breaded Soy Fillet " : 176 , "Mayonnaise (tbsp)" : 57 ,  "Textured Soy (1/2 cup)" : 153 }
#------------------------------------------------------------------------------------------------------------------------------------------------
#TKINTER GUI:
root = Tk()
root.title("Diet Calculator")
root.config(background="#c3e898", borderwidth=2)

notebook = ttk.Notebook(root)  # Creates the Notebook widget. It manages a collection of widgets.
notebook.pack(expand = True , fill = "both")

tab1 = Frame(notebook)  # Creates the first tab (it is a frame).
notebook.add(tab1 , text = "Diet Plan")

frame1 = Frame(tab1)  # Creates a frame inside tab 1.
frame1.pack(expand = True , fill = "both")
frame1.config(background="#c3e898", borderwidth=2)

img1 = PhotoImage(file="diet.png")
root.iconphoto(True, img1)

title1_label = Label(frame1, text = "Daily Calorie Intake Calculation", background="#c3e898", font="candara 16 bold")
title1_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

gender_label = Label(frame1, text = "Enter your gender F or M:", background="#c3e898", font="candara 11")
gender_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

gender_entry = Entry(frame1, width=8)   # Creates gender entry box with its button that stores the input with a function.
gender_entry.grid(row=2, column=0, padx=5, pady=5, sticky=W)
gender_button = Button(frame1 , text = "SUBMIT" , command = submit_gender, font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
gender_button.grid(row=2, column=1, padx=5, pady=5)

weight_label= Label(frame1, text = "Enter your weight (kg):", background="#c3e898", font="candara 11")
weight_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

weight_entry = Entry(frame1, width=8)   # Creates weight entry box with its button that stores the input with a function.
weight_entry.grid(row=4, column=0, padx=5, pady=5, sticky=W)
weight_button = Button(frame1 , text = "SUBMIT" , command = submit_weight, font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
weight_button.grid(row=4, column=1, padx=5, pady=5)

height_label= Label(frame1, text = "Enter your height (cm):", background="#c3e898", font="candara 11")
height_label.grid(row=5, column=0, padx=5, pady=5, sticky=W)

height_entry = Entry(frame1, width=8)   # Creates height entry box with its button that stores the input with a function.
height_entry.grid(row=6, column=0, padx=5, pady=5, sticky=W)
height_button = Button(frame1 , text = "SUBMIT" , command = submit_height, font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
height_button.grid(row=6, column=1, padx=5, pady=5)

age_label = Label(frame1, text = "Enter your age:", background="#c3e898", font="candara 11")
age_label.grid(row=7, column=0, padx=5, pady=5, sticky=W)

age_entry = Entry(frame1, width=8)   # Creates age entry box with its button that stores the input with a function.
age_entry.grid(row=8, column=0, padx=5, pady=5, sticky=W)
age_button = Button(frame1 , text = "SUBMIT" , command = submit_age, font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
age_button.grid(row=8, column=1, padx=5, pady=5)

katchMult_label = Label(frame1, text = "Enter your activity level multiplier (See third tab):", background="#c3e898", font="candara 11")
katchMult_label.grid(row=9, column=0, padx=5, pady=5, sticky=W)

katchMult_entry = Entry(frame1, width=8)   # Creates Katch-McArdle multiplier entry box with its button that stores the input with a function.
katchMult_entry.grid(row=10, column=0, padx=5, pady=5, sticky=W)
katchMult_button = Button(frame1 , text = "SUBMIT" , command = submit_katchMult, font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
katchMult_button.grid(row=10, column=1, padx=5, pady=5)

week_weight_loss_label = Label(frame1, text = "Enter your desired weekly weight loss (0.5 to 1 kg):", background="#c3e898", font="candara 11")
week_weight_loss_label.grid(row=11, column=0, padx=5, pady=5, sticky=W)

week_weight_loss_entry = Entry(frame1, width=8)   # Creates weekly Weight Loss entry box with its button that stores the input with a function.
week_weight_loss_entry.grid(row=12, column=0, padx=5, pady=5, sticky=W)

week_weight_loss_button = Button(frame1 , text = "SUBMIT" , command = submit_weekWeightLoss, font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
week_weight_loss_button.grid(row=12, column=1, padx=5, pady=5)

calculate_label = Label(frame1, text = "Calculate Diet Daily Calorie Intake:", background="#c3e898", font="candara 11 bold")
calculate_label.grid(row=13, column=0, padx=5, pady=5, sticky=W)
calculate_button = Button(frame1, text="Calculate", command= lambda: calculate_dailyCalIntake(gender, weight, height, age, katchMult, weekWeightLoss), font="candara 10 bold", background="#1d812d", fg="white", borderwidth=3)
calculate_button.grid(row=14, column=1, padx=5, pady=5)

result_label = Label(frame1, text= "", background="#c3e898", font="candara 11")
result_label.grid(row=15, column=1, padx=5, pady=5)

#TAB 2:
tab2 = Frame(notebook)   # Creates second tab
notebook.add(tab2, text = "Food")

frame2 = Frame(tab2)
frame2.pack(expand = True , fill = "both")
frame2.config(background="#c3e898", borderwidth=2)

list_button = Button(frame2, text = "FOOD LIST", command=open_list_window, font="candara 16 bold", background="#1d812d", fg="white", borderwidth=5)
list_button.grid(row=0, column=0, padx=25, pady=25)

sum_button = Button(frame2, text = "FOOD SUM", command=sum_calories, font="candara 16 bold", background="#1d812d", fg="white", borderwidth=5)
sum_button.grid(row=1, column=0, padx=25, pady=25)

#TAB 3:
tab3 = Frame(notebook)
notebook.add(tab3, text = "Activity Multiplier")

frame3 = Frame(tab3)
frame3.pack(expand = True , fill = "both")
frame3.config(background="#c3e898", borderwidth=2)

activity_label1 = Label(frame3, text="Choose the value of your Activity Multiplier \n acording to this table:",font="candara 12 bold", background="#c3e898")
activity_label1.pack()
activity_label2 = Label(frame3, text = ("\n\n"
                                        "•Little or no exercise, desk job = 1.2\n\n"
                                        "•Light exercise 1-3 days per week =  1.375\n\n" 
                                        "•Moderate exercise 6-7 days per week = 1.55\n\n" 
                                        "•Hard exercise every day, or exercising 2 times per day = 1.725\n\n" 
                                        "•Hard exercise 2 times per day, or Athlete training = 1.9"), font="candara 11", background="#c3e898", justify=LEFT)
activity_label2.pack()

root.mainloop()

