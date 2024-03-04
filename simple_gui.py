# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: October 18, 2023

# Description:
# This file contains the My_GUI class. An object of the class consists
# of a tkinter window containing a text keyin field, an execute button,
# an exit button, and a label. When the user types input into the text
# keyin field, then clicks the execute button, the input text is displayed
# in the label. If the user clicks the exit button, the program terminates.

# Logic:
# import tkinter
# class My_GUI:
#   init:
#       main window = tkinter.Tk
#       title = 'My GUI'
#       initialize top, middle, and bottom frames
#       prompt = Label(top frame, 'Enter text to display: ')
#       field = Entry(top frame)
#       pack prompt and field
#       outText = StringVar
#       output label = Label(middle frame, outText)
#       pack output label
#       execute button = Button(bottom frame, 'Execute', command=getResults)
#       exit button = Button(bottom frame, 'Exit', command=destroy)
#       pack execute button and exit button
#       pack each frame
#       tkinter.mainloop()
#   getResults:
#       text = field.get()
#       if not empty and not whitespace:
#           set outText(text)
#       else: set outText to message
# gui = My_GUI()


# import tkinter module to create GUI
import tkinter

# declare a class for creating GUI
class My_GUI:
    # initialization method for GUI
    def __init__(self):
        # create main window widget
        self.main_window = tkinter.Tk()
        self.main_window.title(f'My GUI')

        # create top frame
        self.top_frame = tkinter.Frame(self.main_window)
        # create middle frame
        self.middle_frame = tkinter.Frame(self.main_window)
        # create bottom frame
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create label in top frame with text prompting for input
        self.prompt = tkinter.Label(self.top_frame,
                                    text='Enter text to display: ')
        # create entry widget for user to type input into
        self.field = tkinter.Entry(self.top_frame, width=10)

        # pack prompt label
        self.prompt.pack(side='left')
        # pack entry widget
        self.field.pack(side='left')
        
        # create string variable object for output text
        self.out_text = tkinter.StringVar()
        # create label to display output in bottom frame
        self.out_label = tkinter.Label(self.middle_frame,
                                       textvariable=self.out_text)

        # pack output label widget
        self.out_label.pack(side='left')

        # create execute button, which will call get_results method
        self.execute_button = tkinter.Button(self.bottom_frame,
                                             text='Execute',
                                             command=self.get_results)
        # create exit button, which will call destroy method and end program
        self.exit_button = tkinter.Button(self.bottom_frame, text='Exit',
                                          command=self.main_window.destroy)

        # pack execute button
        self.execute_button.pack(side='left')
        # pack exit button
        self.exit_button.pack(side='left')

        # pack top frame
        self.top_frame.pack()
        # pack middle frame
        self.middle_frame.pack()
        # pack bottom frame
        self.bottom_frame.pack()
        
        # enter tkinter main loop
        tkinter.mainloop()

    # method to get result output from user input
    def get_results(self):
        # read in user input using get method
        entered_text = str(self.field.get())
        # check if any text was entered and ensure it is not only whitespace
        if entered_text and not entered_text.isspace():
            # if so, call set method to appropriately set string variable
            self.out_text.set(f'You entered: {entered_text.strip()}')
        # if nothing was entered, or only whitespace was entered...
        else:
            # call set method to set string to appropriate message
            self.out_text.set(f'No Text to Display')

# call main to execute program
if __name__ == '__main__':
    # create instance of My_GUI
    gui = My_GUI()
