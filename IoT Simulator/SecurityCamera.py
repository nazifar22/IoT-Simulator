import random

class SecurityCamera:
    def __init__(self, ID, Status, Security):
        self.ID = ID
        self.Status = Status
        self.MotionDetected = False

    def turnOn(self):
        self.Status = "ON"
        print("turned on the security camera")

    def turnOff(self):
        self.Status = "OFF"
        self.MotionDetected = False
        print("turned off the security camera")
            
    def detectMotion(self, light):
        if self.Status == "ON":
            self.MotionDetected = random.choice([True, False])
        else:
            self.MotionDetected = False
        motion_stat = "YES" if self.MotionDetected else "NO"
        print(f"Security camera - motion: {motion_stat}")
        if self.Status == "ON" and self.MotionDetected and light.Status == "OFF":
            light.turnOn()
    
    def automationRule(self, SmartLight):
        #instance of SmartLight is passed as an argument
        if self.Status == "ON" and self.MotionDetected:
            SmartLight.turnOn()
            print("Automation rule: light turned on due to motion detected")
        else:
            print("Automation rule: no action taken as no motion detected")