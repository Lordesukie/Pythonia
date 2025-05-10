from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        # Get the month abbreviation from the form
        deets = request.form['month'].strip().capitalize()
        
        # Check if input is valid
        if deets in monthConversions and deets in monthOrder:
            full_month = monthConversions[deets]
            position = monthOrder[deets]
            result = f"{full_month} is the {position}"
        else:
            result = "Please enter a valid month abbreviation (e.g., Jan, Feb, etc.)"
    
    return render_template('dictionary.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
