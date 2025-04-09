class SmartLight:
    def __init__ (self, ID, Status, Brightness):
        self.ID = ID
        self.Status = Status
        self.Brightness = Brightness

    def turnOn(self):
        self.Status = "ON"
        # self.SetBrightness = 50
        print("turned on the light")

    def turnOff(self):
        self.Status = "OFF"
        #reset brightness when off
        self.SetBrightness = 0
        print("turned off the light")

    def setBrightness(self, Brightness):
        if self.Status == "ON":
            self.Brightness = max(0, min(Brightness, 100))

    def controlBrightness(self):
        if self.Status == "ON" and self.Brightness > 0:
            self.Brightness -= 10
            self.Brightness = max(0, self.Brightness)
            print(f"brightness decreased to {self.Brightness}%")
        else:
            print("light is off")