
class Controller:

    def __init__(self, model, view):

        self.__view = view
        self.__model = model
        self.__CELSIUS = "°C"
        self.__FARENHEIT = "°F"
        self.__KELVIN = "°K"

        #Binding
        self.__view.update(str(self.__model.getTemperature()) + self.getUnit())

        #callback
        self.__view.increase_btn.config(command = self.increase)
        self.__view.decrease_btn.config(command = self.decrease)
        self.__view.celsius_btn.config(command = self.celsius)
        self.__view.farenheit_btn.config(command = self.farenheit)
        self.__view.kelvin_btn.config(command = self.kelvin)

    def increase(self) -> None:
        self.__model.increase()
        self.__view.update(str(self.__model.getTemperature()) + self.getUnit())
    
    def decrease(self) -> None:
        self.__model.decrease()
        self.__view.update(str(self.__model.getTemperature()) + self.getUnit())
    
    def celsius(self) -> None:
        if self.getUnit() == self.__FARENHEIT:
            self.__model.celsius()
            self.__view.update(str(self.__model.getTemperature()) + self.getUnit())
        elif self.getUnit() == self.__KELVIN:
            self.__model.celsius()
            self.__view.update(str(self.__model.getTemperature()) + self.getUnit())
        else:
            pass

    def farenheit(self) -> None:
        if self.getUnit() == self.__CELSIUS:
            self.__model.farenheit()
            self.__view.update(str(self.__model.getTemperature()) + self.getUnit())
        elif self.getUnit() == self.__KELVIN:
            self.__model.farenheit()
            self.__view.update(str(self.__model.getTemperature()) + self.getUnit())
        else:
            pass
        
    def kelvin(self) -> None:
        if self.getUnit() == self.__CELSIUS:
            self.__model.kelvin()
            self.__view.update(str(self.__model.getTemperature()) + self.getUnit())
        elif self.getUnit() == self.__FARENHEIT:
            self.__model.kelvin()
            self.__view.update(str(self.__model.getTemperature()) + self.getUnit())
        else:
            pass

    def getUnit(self) -> str:
        return self.__model.getUnit()
