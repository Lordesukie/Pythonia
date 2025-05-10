
import tkinter as tk
from tkinter import messagebox
#You can also use numbers for keys 

monthConversions = {  
                   
                   "Jan": "January",
                   "Feb": "February",
                   "Mar": "March",
                   "Apr": "April",
                   "May": "May",
                   "Jun": "June",
                   "Jul": "July",
                   "Aug": "August",
                   "Sep": "September",
                   "Oct": "October",
                   "Nov": "November",
                   "Dec": "December",
                   
                    
                    
                    }


monthOrder = {
    
    
                   "Jan": "First Month of the Year",
                   "Feb": "Second Month of the Year",
                   "Mar": "Third Month of the Year",
                   "Apr": "Fourth Month of the Year",
                   "May": "Fifth Month of the Year",
                   "Jun": "Sixth Month of the Year",
                   "Jul": "Seventh Month of the Year",
                   "Aug": "Eighth Month of the Year",
                   "Sep": "Ninth Month of the Year",
                   "Oct": "Tenth Month of the Year",
                   "Nov": "Eleventh Month of the Year",
                   "Dec": "Twelfth Month of the Year",
    
    
}



# Function to handle button click
def show_month_details():
    deets = month_entry.get().strip().capitalize()    # Check if input is valid
    if deets in monthConversions and deets in monthOrder:
        full_month = monthConversions[deets]
        position = monthOrder[deets]
        result_label.config(text=f"{full_month} is the {position}")
    else:
        # If invalid month abbreviation
        messagebox.showerror("Invalid Input", "Please enter a valid month abbreviation (e.g., Jan, Feb, etc.)")



# Creating the main window
root = tk.Tk()
root.title("Month Lookup")
root.geometry("400x200")
root.config(bg="sky blue")

# Creating the entry widget for month abbreviation
month_entry_label = tk.Label(root, text="Enter a short abbreviation for any month:")
month_entry_label.pack(pady=10)

month_entry = tk.Entry(root, font=("Arial", 14))
month_entry.pack(pady=10)

# Creating the button to trigger the lookup
lookup_button = tk.Button(root, text="Search a month abbreviation", font=("Arial", 14), command=show_month_details)
lookup_button.pack(pady=10)

# Creating a label to display results
result_label = tk.Label(root, text="", font=("Arial", 12), bg="sky blue")
result_label.pack(pady=10)

# Running the application
root.mainloop()


