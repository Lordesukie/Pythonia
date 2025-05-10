import tkinter as tk
from tkinter import messagebox
import wikipedia

# Dictionaries with month abbreviations
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

# Function to get Wikipedia summary
def get_wikipedia_summary(month_name):
    try:
        # Get 2 sentences about the month
        summary = wikipedia.summary(month_name, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return "Wikipedia page has multiple meanings. Please refine the search."
    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found for this month."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Function to handle button click
def show_month_details():
    deets = month_entry.get().strip().capitalize()
    if deets in monthConversions and deets in monthOrder:
        full_month = monthConversions[deets]
        position = monthOrder[deets]
        result_label.config(text=f"{full_month} is the {position}")
        
        # Fetch and show Wikipedia details
        wiki_summary = get_wikipedia_summary(full_month)
        wiki_text.delete(1.0, tk.END)  # Clear previous text
        wiki_text.insert(tk.END, wiki_summary)
        
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid month abbreviation (e.g., Jan, Feb, etc.)")

# Creating the main window
root = tk.Tk()
root.title("Month Lookup with Wikipedia")
root.geometry("500x500")
root.config(bg="sky blue")

# Creating the entry widget for month abbreviation
month_entry_label = tk.Label(root, text="Enter a short abbreviation for any month:", bg="sky blue", font=("Arial", 12))
month_entry_label.pack(pady=10)

month_entry = tk.Entry(root, font=("Arial", 14))
month_entry.pack(pady=10)

# Creating the button to trigger the lookup
lookup_button = tk.Button(root, text="Search a month abbreviation", font=("Arial", 14), command=show_month_details)
lookup_button.pack(pady=10)

# Creating a label to display the month and order
result_label = tk.Label(root, text="", font=("Arial", 12), bg="sky blue")
result_label.pack(pady=10)

# Text box to display Wikipedia details
wiki_text = tk.Text(root, wrap="word", font=("Arial", 10), height=10, width=50)
wiki_text.pack(pady=10)

# Running the application
root.mainloop()

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

