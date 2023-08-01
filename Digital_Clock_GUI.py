from tkinter import *
from time import strftime

# Creating tkinter window
digital_clock = Tk()
digital_clock.geometry("450x120")
digital_clock.title('My Digital Clock')

# Display time in 12-hour format on the label using this function
def time():
    string = strftime('%I:%M:%S %p')  # %I=hour in 12-hour format, %M=Minute, %S=second, %p=AM or PM
    label.config(text=string)
    label.after(1000, time)

# Increase the user experience by designing the label widget
label = Label(digital_clock, font=('calibri', 60, 'bold'), background='black', foreground='sky blue', borderwidth=8, relief="groove")

# Clock at the center of the tkinter window
label.pack(anchor='center')

time()  # Function calling

mainloop()  # Start the main event loop
