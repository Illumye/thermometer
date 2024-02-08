from tkinter import *

class Application():

    def __init__(self):

        self.fenetre = Tk()
        self.fenetre.title("My thermometer")
        self.label = Label(self.fenetre, text="10°C", width='20', height = '5', font = ('Arial', 25), bg='ivory')
        self.label.pack(side=TOP, padx=5, pady=5)

        Button(self.fenetre, text ='Increase', command = self.increase).pack(side=LEFT, padx=5, pady=5)
        Button(self.fenetre, text ='Decrease', command = self.decrease).pack(side=RIGHT, padx=5, pady=5)
        Button(self.fenetre, text ='Celsius', command = self.farenheit_to_celsius).pack(side=TOP, padx=5, pady=5)
        Button(self.fenetre, text ='Farenheit', command = self.celsius_to_farenheit).pack(side=BOTTOM, padx=5, pady=5)
        
        self.fenetre.mainloop()

    def increase(self):
        value = int(self.label['text'][:-2])
        unit = self.label['text'][-2:]
        self.label.config( text = str( value + 1 ) + unit)
    
    def decrease(self):
        value = int(self.label['text'][:-2])
        unit = self.label['text'][-2:]
        self.label.config( text = str( value - 1 ) + unit)
    
    def farenheit_to_celsius(self):
        if self.label['text'][-2:] == '°C':
            pass
        else:
            value_farenheit = int(self.label['text'][:-2])
            value_celsius = round((value_farenheit - 32) * (5/9))
            unit = '°C'
            self.label.config( text = str(value_celsius) + unit)
    
    def celsius_to_farenheit(self):
        if self.label['text'][-2:] == '°F':
            pass
        else:
            value_celsius = int(self.label['text'][:-2])
            value_farenheit = round(value_celsius * (9/5) + 32)
            unit = '°F'
            self.label.config( text = str(value_farenheit) + unit)

if __name__ == '__main__':
    app = Application()