# IoT Simulator

In this project, I developed a Python-based IoT simulator for a smart home automation system. The simulator emulates the behavior of three common smart devices: SmartLight, Thermostat, and SecurityCamera. Each device was implemented as a separate class using object-oriented programming (OOP), with attributes such as device_id, status (on/off), and device-specific properties like brightness for lights, temperature for thermostats, and motion_detected status for cameras. Methods were added to allow users to change the device status and properties. Device behavior is periodically randomized to simulate real-time changes.

I also created a central automation system class, AutomationSystem, which is responsible for managing all devices. It includes functionality to add and discover devices and to periodically update their state using a simulation loop that runs every few seconds. The system checks for automation rules and modifies device behavior accordingly to simulate smart decision-making.

To provide user interaction and monitoring, I developed a Tkinter-based GUI dashboard. This dashboard displays the current status of all devices in real time. It allows users to toggle smart lights, adjust thermostat temperatures, and arm/disarm security cameras. The GUI reflects both manual and automated changes instantly, simulating a functional smart home interface.

I applied key Python concepts such as classes, static methods, file handling, exception handling, randomization, pip modules, and modular design using packages. Extensive comments and documentation are included throughout the codebase to describe how each component works. I also wrote test cases to validate device behavior and automation rules, ensuring the correctness and reliability of the system.

How to Use:
To use the smart home IoT simulator, ensure you have Python 3 installed along with required libraries like tkinter (which is typically included in standard Python installations). Start by running the main Python file, which will launch both the simulation loop and the Tkinter-based dashboard GUI. Upon launching, you’ll see a visual display of all available smart devices, such as lights, thermostats, and security cameras.

Each device panel shows current states such as whether a light is on and its brightness level, the current temperature from a thermostat, or motion status from a camera. You can toggle devices on or off, adjust settings, and observe their status in real time. The GUI will continuously update as the simulation loop modifies device behavior randomly over time, reflecting automated and natural changes within a smart home.

If you’re an advanced user, you can extend or modify automation rules by editing the AutomationSystem class. Any changes in device state made by automation or manual control are instantly reflected on the GUI. The system is modular and scalable—additional devices or automation features can be added with minimal code modifications.

To stop the simulator, simply close the GUI window. Make sure to refer to the code comments and accompanying documentation for further information on device classes, simulation logic, and GUI interaction features.
