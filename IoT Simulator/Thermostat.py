class Thermostat:
    def __init__(self, ID, Status, Temperature):
        self.ID = ID
        self.Status = Status
        self.Temperature = Temperature

    def turnOn(self):
        self.Status = "ON"
        #set default brightness when on
        self.SetTemperature = 20
        print("turned on the thermostat")

    def turnOff(self):
        self.Status = "OFF"
        #reset brightness when off
        self.SetTemperature = 10
        print("turned off the thermostat")

    def setTemperature(self, Temperature):
        if self.Status == "ON":
            self.Temperature = max(10, min(Temperature, 30))

    def controlTemperature(self):
        if self.Status == "ON" and self.Temperature > 0:
            self.Temperature -= 10
            self.Temperature = max(0, self.Temperature)
            print(f"temperature decreased to {self.Temperature}%")
        else:
            print("thermostat is off")
