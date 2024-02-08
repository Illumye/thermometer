class Model:

    def __init__(self, temperature : int, unit : str):
        
        self.__temperature = temperature
        self.__unit = unit

    def celsius(self) -> int:
        if self.__unit == "°F":
            self.__temperature = round((self.__temperature - 32) * 5 / 9)
        elif self.__unit == "°K":
            self.__temperature = round(self.__temperature - 273.15)
        self.__unit = "°C"

    def farenheit(self) -> int:
        if self.__unit == "°C":
            self.__temperature =  round(9 / 5 * self.__temperature + 32)
        elif self.__unit == "°K":
            self.__temperature = round((self.__temperature - 273.15) * 9 / 5 + 32)
        self.__unit = "°F"
    
    def kelvin(self) -> int:
        if self.__unit == "°C":
            self.__temperature = round(self.__temperature + 273.15)
        elif self.__unit == "°F":
            self.__temperature = round((self.__temperature - 32) * 5 / 9 + 273.15)
        self.__unit = "°K"

    def increase(self) -> int:
        self.__temperature += 1

    def decrease(self) -> int:
        if self.__unit == "°K" and self.__temperature <= 0:
            pass
        else:
            self.__temperature -= 1

    def getTemperature(self) -> int:
        return self.__temperature
    
    def getUnit(self):
        return self.__unit