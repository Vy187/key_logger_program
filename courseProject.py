#import class from module
from courseProjectModule import App

#Declare variables that the class App will use
title       = 'Basic Key Logger'
options     = ['1. Start Key Logger', '2. View Log File', '3. Clear Log File', '4. Exit']
file_path   = 'courseProjectLog.txt'

#Define the app
app = App(title, options, file_path)
#Start the app
app.main()
    