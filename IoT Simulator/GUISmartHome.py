import tkinter as tk
from tkinter import ttk
from style import Style

from SecurityCamera import SecurityCamera
from Thermostat import Thermostat
from SmartLight import SmartLight

#creating window
root = tk.Tk()
root.title("Smart Home IoT Simulator")
Style(root)

root.grid_columnconfigure(0, weight=1) 
root.grid_columnconfigure(1, weight=1) 

#initializing simulated devices
light = SmartLight("light1", "OFF", 0)
thermostat = Thermostat("thermo1", "OFF", 20)
camera = SecurityCamera("cam1", "OFF", "idle")

# Toggle Light
def toggle_light():
    if light.Status == "OFF":
        light.turnOn()
    else:
        light.turnOff()
    light_brightness_var.set(light.Brightness) # Reset the slider position when turned off
    updateStatus()

# Toggle Thermostat
def toggle_thermostat():
    if thermostat.Status == "OFF":
        thermostat.turnOn()
    else:
        thermostat.turnOff()
    updateStatus()

# Toggle Camera
def toggle_camera():
    if camera.Status == "OFF":
        camera.turnOn()
    else:
        camera.turnOff()
    updateStatus()

#updating device statuses on the GUI
def updateStatus():
    light_status_var.set(f"Light: {light.Status} - Brightness: {light.Brightness}%")
    thermostat_status_var.set(f"Thermostat: {thermostat.Status}  - Temperature: {thermostat.Temperature}°C")
    camera_status_var.set(f"Security Camera: {camera.Status}")
    light_brightness_var.set(light.Brightness)
    thermostat_temp_var.set(thermostat.Temperature)
    camera_motion_var.set(f"Motion: {'YES' if camera.MotionDetected else 'NO'}")
    # Schedule the update_device_status function to run every 1000ms
    root.after(1000, updateStatus)

def update_light_brightness(val):
    light.setBrightness(round(float(val)))
    updateStatus()

def update_thermostat_temperature(val):
    thermostat.setTemperature(round(float(val)))
    updateStatus()

# Randomly detect motion (this would be part of a more complex simulation in a real app)
def detect_motion():
    camera.detectMotion(light) 
    updateStatus()

# Create status labels
light_status_var = tk.StringVar()
thermostat_status_var = tk.StringVar()
camera_status_var = tk.StringVar()
light_status_label = ttk.Label(root, textvariable=light_status_var)
thermostat_status_label = ttk.Label(root, textvariable=thermostat_status_var)
camera_status_label = ttk.Label(root, textvariable=camera_status_var)

# Create controls for Light Brightness and Thermostat Temperature

light_brightness_var = tk.IntVar(value=light.Brightness)
thermostat_temp_var = tk.IntVar(value=20)


light_brightness_var = tk.IntVar()
thermostat_temp_var = tk.IntVar()
light_brightness_scale = ttk.Scale(root, from_=0, to=100, variable=light_brightness_var, orient='horizontal', command=update_light_brightness)
thermostat_temp_scale = ttk.Scale(root, from_=10, to=30, variable=thermostat_temp_var, orient='horizontal', command=update_thermostat_temperature)

# Create buttons to toggle devices
toggle_light_button = ttk.Button(root, text="Toggle Light", command=toggle_light)
toggle_thermostat_button = ttk.Button(root, text="Toggle Thermostat", command=toggle_thermostat)
toggle_camera_button = ttk.Button(root, text="Toggle Security Camera", command=toggle_camera)

# Motion detection label and button
camera_motion_var = tk.StringVar()
camera_motion_label = ttk.Label(root, textvariable=camera_motion_var)
detect_motion_button = ttk.Button(root, text="Random Detect Motion", command=detect_motion)

# Grid layout for all widgets
padding = 2
button_width = 10  # Define a consistent button width

# Define the rows and columns layout
root.grid_columnconfigure(0, weight=1)  # Makes the column expand to fill available space
root.grid_columnconfigure(1, weight=1)

light_status_label.grid(row=0, column=0, columnspan=2, padx=padding, pady=padding, sticky="ew")
thermostat_status_label.grid(row=1, column=0, columnspan=2, padx=padding, pady=padding, sticky="ew")
camera_status_label.grid(row=2, column=0, columnspan=2, padx=padding, pady=padding, sticky="ew")

light_brightness_scale.grid(row=3, column=0, padx=padding, pady=padding, sticky="ew")
toggle_light_button.grid(row=3, column=1, padx=padding, pady=padding, sticky="ew")

thermostat_temp_scale.grid(row=4, column=0, padx=padding, pady=padding, sticky="ew")
toggle_thermostat_button.grid(row=4, column=1, padx=padding, pady=padding, sticky="ew")

camera_motion_label.grid(row=5, column=0, padx=padding, pady=padding, sticky="ew")
toggle_camera_button.grid(row=5, column=1, padx=padding, pady=padding, sticky="ew")

detect_motion_button.grid(row=6, column=0, columnspan=2, padx=padding, pady=padding, sticky="ew")

# Initialize the device status updater
updateStatus()

# Start the GUI loop
root.mainloop()
