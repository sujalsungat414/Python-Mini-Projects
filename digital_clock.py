import tkinter as tk  # Import tkinter for GUI creation
from time import strftime  # Import strftime to format time strings

root = tk.Tk()  # Create the main application window
root.title("⏰ Digital Clock")  # Set the window title
root.geometry("300x100")  # Set fixed window size (width x height)
root.resizable(False, False)  # Disable resizing of the window
root.configure(bg="black")  # Set the background color of the window to black

# Create a Label widget to display the time
# - font is Arial, size 40, bold style
# - background color matches the window black
# - text color (foreground) is cyan for contrast and style
label = tk.Label(root, font=("Arial", 40, "bold"), background="black", foreground="cyan")
label.pack(anchor="center")  # Center the label in the window

def update_time():
    # Function to get the current time and update the label
    time_string = strftime("%H:%M:%S")  # Format current time as HH:MM:SS (24-hour)
    label.config(text=time_string)  # Update the label text with the current time
    label.after(1000, update_time)  # Schedule this function to be called again after 1000ms (1 second)

update_time()  # Call the update_time function once to start the clock
root.mainloop()  # Run the tkinter event loop, keeping the window open and responsive
