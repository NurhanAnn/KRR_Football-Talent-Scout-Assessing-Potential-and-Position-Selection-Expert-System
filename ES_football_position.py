#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox

# Define global variables for ability levels
agility_var = None
leg_length_var = None
leg_explosion_var = None
dribbling_var = None
accuracy_var = None
speed_var = None

# Declare position_window as a global variable
position_window = None

def determine_position():
    # Gather input from the user
    age = int(age_entry.get())
    gender = gender_entry.get()
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    sprint_time = float(sprint_entry.get())
    vertical_jump = float(jump_entry.get())

    # Calculate the Body Mass Index (BMI)
    bmi = weight / ((height / 100) ** 2)

    # Analyze the individual based on the gathered data
    talent_score = 0
    explanations = []  # List to store explanations

    if age >= 6 and age <= 18:
        talent_score += 2
        explanations.append("Age between 6 and 18: +2 points")

    if gender.lower() == "male":
        if sprint_time <= 11.0:
            talent_score += 3
            explanations.append("Fast 100m sprint time (<= 11.0 seconds): +3 points")
        if vertical_jump >= 60.0:
            talent_score += 2
            explanations.append("High vertical jump height (>= 60.0 cm): +2 points")
    elif gender.lower() == "female":
        if sprint_time <= 12.0:
            talent_score += 3
            explanations.append("Fast 100m sprint time (<= 12.0 seconds): +3 points")
        if vertical_jump >= 50.0:
            talent_score += 2
            explanations.append("High vertical jump height (>= 50.0 cm): +2 points")

    if bmi >= 18.5 and bmi <= 24.9:
        talent_score += 2
        explanations.append("Normal BMI (18.5-24.9): +2 points")

    # Determine the potential for sports talent
    explanation_text = "\n".join(explanations)  # Combine explanations into a single text

    if talent_score >= 6:
        talent_result = "Congratulations! Based on the analysis, you have a high potential for having sports talent."
    elif talent_score >= 3:
        talent_result = "Based on the analysis, you have a moderate potential for having sports talent."
    else:
        talent_result = "Based on the analysis, you have a low potential for having sports talent."

    # Determine the suitable position based on abilities
    agility_level = agility_var.get()
    leg_length_level = leg_length_var.get()
    leg_explosion_level = leg_explosion_var.get()
    dribbling_level = dribbling_var.get()
    shooting_accuracy_level = accuracy_var.get()
    shooting_speed_level = speed_var.get()

    position_scores = {
        "Goalkeeper": 0,
        "Defender": 0,
        "Midfielder": 0,
        "Forward": 0
    }

    # Update position scores based on ability levels
    if agility_level == "High":
        position_scores["Goalkeeper"] += 2
        position_scores["Defender"] += 1
        position_scores["Midfielder"] += 1
        position_scores["Forward"] += 0
    elif agility_level == "Moderate":
        position_scores["Goalkeeper"] += 1
        position_scores["Defender"] += 1
        position_scores["Midfielder"] += 1
        position_scores["Forward"] += 0

    if leg_length_level == "High":
        position_scores["Goalkeeper"] += 1
        position_scores["Defender"] += 2
        position_scores["Midfielder"] += 1
        position_scores["Forward"] += 0
    elif leg_length_level == "Moderate":
        position_scores["Goalkeeper"] += 1
        position_scores["Defender"] += 1
        position_scores["Midfielder"] += 1
        position_scores["Forward"] += 0

    if leg_explosion_level == "High":
        position_scores["Goalkeeper"] += 1
        position_scores["Defender"] += 2
        position_scores["Midfielder"] += 2
        position_scores["Forward"] += 2
    elif leg_explosion_level == "Moderate":
        position_scores["Goalkeeper"] += 1
        position_scores["Defender"] += 1
        position_scores["Midfielder"] += 1
        position_scores["Forward"] += 1

    # Update position scores for the remaining abilities

    if dribbling_level == "High":
        position_scores["Goalkeeper"] += 0
        position_scores["Defender"] += 1
        position_scores["Midfielder"] += 2
        position_scores["Forward"] += 2
    elif dribbling_level == "Moderate":
        position_scores["Goalkeeper"] += 0
        position_scores["Defender"] += 1
        position_scores["Midfielder"] += 1
        position_scores["Forward"] += 1

    if shooting_accuracy_level == "High":
        position_scores["Goalkeeper"] += 0
        position_scores["Defender"] += 1
        position_scores["Midfielder"] += 2
        position_scores["Forward"] += 2
    elif shooting_accuracy_level == "Moderate":
        position_scores["Goalkeeper"] += 0
        position_scores["Defender"] += 1
        position_scores["Midfielder"] += 1
        position_scores["Forward"] += 1

    if shooting_speed_level == "High":
        position_scores["Goalkeeper"] += 0
        position_scores["Defender"] += 1
        position_scores["Midfielder"] += 2
        position_scores["Forward"] += 2
    elif shooting_speed_level == "Moderate":
        position_scores["Goalkeeper"] += 0
        position_scores["Defender"] += 1
        position_scores["Midfielder"] += 1
        position_scores["Forward"] += 1

    # Determine the best position based on the position scores
    best_position = max(position_scores, key=position_scores.get)

    # Show the results to the user
    messagebox.showinfo("Talent Identification and Position Determination",
                        f"{talent_result}\n\nExplanations:\n{explanation_text}\n\n"
                        f"Based on your abilities, the best position for you is: {best_position}")

def show_position_determination():
    global agility_var, leg_length_var, leg_explosion_var, dribbling_var, accuracy_var, speed_var

    # Hide the main window and create the position determination window
    window.withdraw()

    global position_window  # Declare position_window as a global variable

    position_window = tk.Tk()
    position_window.title("Position Determination")
    position_window.geometry("400x300")

    # Create labels and option menus for ability levels
    agility_label = tk.Label(position_window, text="Agility:")
    agility_label.pack()
    agility_var = tk.StringVar(position_window)
    agility_var.set("Low")
    agility_menu = tk.OptionMenu(position_window, agility_var, "Low", "Moderate", "High")
    agility_menu.pack()

    leg_length_label = tk.Label(position_window, text="Leg Length:")
    leg_length_label.pack()
    leg_length_var = tk.StringVar(position_window)
    leg_length_var.set("Low")
    leg_length_menu = tk.OptionMenu(position_window, leg_length_var, "Low", "Moderate", "High")
    leg_length_menu.pack()

    leg_explosion_label = tk.Label(position_window, text="Leg Explosion:")
    leg_explosion_label.pack()
    leg_explosion_var = tk.StringVar(position_window)
    leg_explosion_var.set("Low")
    leg_explosion_menu = tk.OptionMenu(position_window, leg_explosion_var, "Low", "Moderate", "High")
    leg_explosion_menu.pack()

    dribbling_label = tk.Label(position_window, text="Dribbling:")
    dribbling_label.pack()
    dribbling_var = tk.StringVar(position_window)
    dribbling_var.set("Low")
    dribbling_menu = tk.OptionMenu(position_window, dribbling_var, "Low", "Moderate", "High")
    dribbling_menu.pack()

    accuracy_label = tk.Label(position_window, text="Shooting Accuracy:")
    accuracy_label.pack()
    accuracy_var = tk.StringVar(position_window)
    accuracy_var.set("Low")
    accuracy_menu = tk.OptionMenu(position_window, accuracy_var, "Low", "Moderate", "High")
    accuracy_menu.pack()

    speed_label = tk.Label(position_window, text="Shooting Speed:")
    speed_label.pack()
    speed_var = tk.StringVar(position_window)
    speed_var.set("Low")
    speed_menu = tk.OptionMenu(position_window, speed_var, "Low", "Moderate", "High")
    speed_menu.pack()

    # Create a button to determine the best position
    determine_button = tk.Button(position_window, text="Determine Position", command=determine_position)
    determine_button.pack()

    # Create a "Back" button to go back to the main window
    back_button = tk.Button(position_window, text="Back", command=show_main_window)
    back_button.pack()

    # Start the position determination window's event loop
    position_window.mainloop()

def show_main_window():
    # Show the main window and destroy the position determination window (if it exists)
    window.deiconify()
    if position_window is not None:
        position_window.destroy()

# Create the UI window
window = tk.Tk()
window.title("Identification of Sports Talent")
window.geometry("400x300")

# Create labels and entry fields for user input
age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

gender_label = tk.Label(window, text="Gender:")
gender_label.pack()
gender_entry = tk.Entry(window)
gender_entry.pack()

height_label = tk.Label(window, text="Height (cm):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

sprint_label = tk.Label(window, text="100m Sprint Time (seconds):")
sprint_label.pack()
sprint_entry = tk.Entry(window)
sprint_entry.pack()

jump_label = tk.Label(window, text="Vertical Jump Height (cm):")
jump_label.pack()
jump_entry = tk.Entry(window)
jump_entry.pack()

# Create a button to trigger talent identification and position determination
identify_button = tk.Button(window, text="Determine Position", command=show_position_determination)
identify_button.pack()

# Start the UI window's event loop
window.mainloop()


# In[ ]:




