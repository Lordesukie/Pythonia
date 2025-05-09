#tk import is required for visual components, time is  required for timing fuctions
import tkinter as tk
import time

class Stopwatch:
  # Inside the class Stopwatch, the constructor called __init__ takes a parameter 'root'.
  # 'root' refers to the main window for the Tkinter app, similar to JFrame in Java for creating a window.
  # This constructor sets up the initial state of the stopwatch app, including variables and UI components.



    def __init__(self, root):
    #self.root.title("Stopwatch") will set the title of the frame to Stopwatch
    #self.root.attributes('-fullscreen', True) will make the app open in full screen, false for no fullview
    #Just like JFrame titles, the name might not display in fullview mode but its there

        self.root = root
        self.root.title("Stopwatch")
        self.root.attributes('-fullscreen', False)  # Make the window fullscreen

        # Variables to track time
         # 'start_time' stores the time when the stopwatch is started. Initially, it's set to 0.
        self.start_time = 0

        # 'elapsed_time' keeps track of the time that has passed since the stopwatch started.
        # It gets updated when the stopwatch is running.
        self.elapsed_time = 0

        # 'running' is a boolean variable that indicates if the stopwatch is currently active.
        # Initially set to 'False' because the stopwatch hasn't started yet.
        self.running = False

        # 'laps' is an empty list that will store lap times.
        # It allows the user to record multiple lap times while the stopwatch is running.
        self.laps = []

        # 'time_label' is a Tkinter Label widget used to display the time 
        # in the format "minutes:seconds.hundredths".
        # It uses a large font size (48) for easy readability.
        # The initial text "00:00.00" represents the time at the start before the stopwatch is activated.
        self.time_label = tk.Label(root, text="00:00.00", font=("Arial", 48))

        # Packs (positions) the time_label into the window using the pack geometry manager.
        # 'pack()' automatically places the label in the center of the available space.
        # 'pady=20' adds 20 pixels of vertical padding above and below the label.
        # This ensures that there is some space between the label and other elements,
        # making the time display visually separated and more readable.
        self.time_label.pack(pady=20)


        # Creates a new frame widget called 'lap_frame' inside the 'root' window.
        # A 'Frame' in Tkinter acts as a container for organizing other widgets, like labels or buttons.
        # It helps group related widgets together, such as displaying lap times in this case.
        # This frame will be used to hold and display lap times separately from the main time label.
        self.lap_frame = tk.Frame(root)

        # Positions the 'lap_frame' inside the window using the 'pack' geometry manager.
        # The 'pady=10' adds 10 pixels of vertical space above and below the 'lap_frame',
        # ensuring that it is not too close to other elements in the window.
        # This creates a visually distinct area for displaying lap times.
        self.lap_frame.pack(pady=10)


# Creates a Listbox widget named 'lap_list' inside the 'lap_frame'.
# A 'Listbox' in Tkinter is used to display a list of items, where each item is displayed as a separate line.
# In this case, it will be used to display recorded lap times.
# The 'font' parameter sets the font style to "Arial" with a size of 20, 
# making the text inside the Listbox larger and more readable.
# 'width=20' sets the width of the Listbox, meaning it can accommodate approximately 20 characters per line.
# 'height=10' sets the height of the Listbox to display up to 10 visible items before requiring scrolling.
        self.lap_list = tk.Listbox(self.lap_frame, font=("Arial", 20), width=20, height=10)

        # Positions the 'lap_list' inside the 'lap_frame' using the 'pack' geometry manager.
        # The 'side=tk.TOP' parameter places the Listbox at the top of the 'lap_frame', 
        # meaning it will be positioned towards the top of the frame container.
        # This helps ensure that lap times are displayed at the top, 
        # leaving space for other potential elements below it.
        self.lap_list.pack(side=tk.TOP)

        # Message label for laps
        self.lap_message = tk.Label(self.lap_frame, text="Any laps display here", font=("Arial", 14))
        self.lap_message.pack(side=tk.BOTTOM)
        # Start, Stop, Reset, Lap, and Exit buttons
        # Creates a Button widget named 'start_button' inside the 'root' window.
        # This button is labeled with the text "Start" and is used to start the stopwatch when clicked.
        # The 'command=self.start' links the button to the 'start' method, meaning when the button is clicked,
        # the 'start' method will be executed, which will initiate the stopwatch's timing mechanism.
        # 'font=("Arial", 14)' sets the font style to "Arial" with a size of 14, making the button text readable.
        self.start_button = tk.Button(root, text="Start", command=self.start, font=("Arial", 14))
        
        # Positions the 'start_button' in the window using the 'pack' geometry manager.
        # The 'side=tk.LEFT' parameter places the button to the left side of its container (the 'root' window in this case).
        # 'padx=10' adds 10 pixels of horizontal padding to the left and right of the button,
        # creating space between this button and other elements, ensuring that the UI is not too cramped.
        self.start_button.pack(side=tk.LEFT, padx=10)



        #A similar setting is given to other buttons, the name just changes
        self.stop_button = tk.Button(root, text="Stop", command=self.stop, font=("Arial", 14))
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset, font=("Arial", 14))
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.lap_button = tk.Button(root, text="Lap", command=self.record_lap, font=("Arial", 14))
        self.lap_button.pack(side=tk.LEFT, padx=10)

        self.exit_button = tk.Button(root, text="Exit", command=self.exit_app, font=("Arial", 14))
        self.exit_button.pack(side=tk.LEFT, padx=10)

    def update_time(self):
        if self.running:
            
            # Calculate elapsed time
            # this method of self is for updating the elapsed time since the timer started running
            # current_time takes the value of time.time() in seconds
            # elapsed_time is gotten from subtracting the current time from the time the timer started
            current_time = time.time()
            self.elapsed_time = current_time - self.start_time
            # Updates the 'time_label' widget to display the current elapsed time of the stopwatch.     
            # The 'config()' method is used to modify the properties of the widget—in this case, the 'text' property.
            # 'self.elapsed_time' holds the current elapsed time since the stopwatch started, in seconds.
            # 'self.format_time()' is a method that formats this elapsed time into a more user-friendly string,
            # typically in a format like "MM:SS.hh" (minutes, seconds, and hundredths of a second).
            # By calling this method, the elapsed time is converted into a readable string, 
            # which is then set as the new text of 'time_label'.
            self.time_label.config(text=self.format_time(self.elapsed_time))

            # Update the time every 10 milliseconds for better accuracy
            # Schedules the 'update_time' method to be called after a delay of 10 milliseconds.
            # The 'after()' method is part of Tkinter's main loop and is used to run a function after a specified amount of time.       
            # In this case, after 10 milliseconds, the 'update_time' method will be executed,
            # which is typically responsible for updating the stopwatch's elapsed time and refreshing the display.
            # This creates a loop-like behavior, allowing the application to remain responsive and continuously update
            # the displayed time without blocking the main GUI thread.
            self.root.after(10, self.update_time)

    def start(self):
    # Begins the stopwatch timing process.
    # This method is called when the user clicks the "Start" button.
        
        # Checks if the stopwatch is currently not running (i.e., it is stopped).
        # The 'self.running' variable is a boolean that tracks whether the stopwatch is active.
        
        if not self.running:
           # Sets 'start_time' to the current time minus any previously elapsed time.
        # This calculation ensures that if the stopwatch is restarted, it continues from where it left off.
        # 'time.time()' gets the current time in seconds since the epoch, 
        # and subtracting 'self.elapsed_time' allows for resuming accurately.
            self.start_time = time.time() - self.elapsed_time

           # Updates 'self.running' to True, indicating that the stopwatch is now active.
            self.running = True

        # Calls the 'update_time' method immediately to start updating the displayed time.
        # This method will likely contain logic to calculate the elapsed time and refresh the UI.
            self.update_time()

    def stop(self):
        #this method checks to see if the self.ruuning boolena is true, then stops it, stopping the timer too
        if self.running:
            self.running = False

    def reset(self):
        
        #This method resets stopwatch components to their beginning states
        #running becomes false, time labels are 0, elapsed time/update time are 0
        #any lap entries are deleted too
        self.running = False
        self.elapsed_time = 0
        self.time_label.config(text="00:00.00")
        self.lap_list.delete(0, tk.END)  # Clear lap list
        self.lap_message.pack(side=tk.BOTTOM)  # Show the lap message again

    def record_lap(self):
        if self.running:
        # Calls 'self.format_time(self.elapsed_time)' to format the current elapsed time into a readable string.
        # 'self.elapsed_time' contains the total time that has elapsed since the stopwatch started.
        # The formatted time is stored in the variable 'lap_time'.
            lap_time = self.format_time(self.elapsed_time)

         # Inserts the formatted lap time into the 'lap_list' Listbox at the end (tk.END).
         # This allows the user to see all recorded lap times sequentially as they are added.
            self.lap_list.insert(tk.END, f"Lap: {lap_time}")

    # Hides the 'lap_message' widget, which could be a temporary message indicating the last lap was recorded.
    # 'pack_forget()' removes the widget from the display, ensuring it does not clutter the user interface.
            self.lap_message.pack_forget()  # Hide the lap message if a lap is recorded

    # A static method does not require access to any instance-specific data or methods 
    # (i.e., it does not take self as the first parameter). 
    # This means it cannot modify object state or access instance attributes.
    @staticmethod
    def format_time(elapsed):
        # Format elapsed time into minutes, seconds, and hundredths of a second
        minutes, seconds = divmod(int(elapsed), 60)
        hundredths = int((elapsed - int(elapsed)) * 100)  # Get hundredths of a second
       # Format the time as a string in the format MM:SS.hh, 
       # ensuring each component is zero-padded to two digits.
        return f"{minutes:02}:{seconds:02}.{hundredths:02}"

    def exit_app(self):
        self.root.quit()  # Exit the application

if __name__ == "__main__":
     # This block of code is executed only when the script is run directly, not when imported as a module.
    # It serves as the entry point for the application.

    # Creates the main application window using Tkinter.
    # 'tk.Tk()' initializes the Tkinter framework and creates a root window,
    # which serves as the main container for all other widgets in the application.
    root = tk.Tk()

    # Creates an instance of the 'Stopwatch' class, passing the 'root' window as an argument.
    # This initializes the stopwatch application, setting up its UI components and functionality.
    # The 'Stopwatch' class likely contains methods for controlling the stopwatch, displaying time, 
    # and handling user interactions.
    stopwatch = Stopwatch(root)
    
    # Enters the Tkinter main event loop, which waits for user interaction and updates the UI accordingly.
    # This loop keeps the application running until the user closes the window.
    # It also processes events like button clicks and redraws the UI when necessary.
    root.mainloop()
