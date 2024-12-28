# Bank-Vault-Engineering-Art-Project
This project simulates a 3D printed bank vault with interactive features controlled by a Raspberry Pi Pico. This project was in collaboration with 3 other individuals. 

## Project Overview

The project involves setting up various components on a Raspberry Pi Pico W to achieve the following functionalities:
1. **Wi-Fi Connection**: The Pico connects to a Wi-Fi network and retrieves data from an exchange rate API.
2. **LCD Display**: Displays exchange rate data.
3. **Button Interaction**: A button triggers an event to fetch exchange rate data and control hardware components.
4. **Servo Motor Control**: Moves the servo motor to different angles in response to button presses.
5. **NeoPixels**: A NeoPixel array that can be controlled to display different colors.
6. **LED Toggle**: A simple LED that toggles on and off with button presses.

---

## Materials & Components

### Hardware
1. **Raspberry Pi Pico W**  
   - The main microcontroller used for this project.
   
2. **LCD Display (I2C)**  
   - 16x2 LCD display using I2C protocol for easy communication with the Raspberry Pi Pico.

3. **Button**  
   - A simple push button to trigger actions like fetching data and controlling hardware components.
   
4. **SG90 Servo Motor**  
   - A small servo motor to demonstrate motor control capabilities.

5. **NeoPixel LEDs**  
   - An array of addressable RGB LEDs to demonstrate lighting effects.

6. **LED**  
   - A basic LED for toggling on and off with button presses.

7. **Breadboard & Jumper Wires**  
   - For connecting the components without soldering.

8. **I2C Wires**  
   - For connecting the LCD to the Raspberry Pi Pico over I2C protocol.

9. **Power Supply**  
   - A 5V power supply or USB cable to power the Raspberry Pi Pico W.

---

## Software Requirements
- **MicroPython**: Firmware for the Raspberry Pi Pico W to run Python code.
- **uRequests library**: To make HTTP requests to fetch data from external APIs.
- **PWM & Servo libraries**: For controlling the servo motor.
- **I2C Libraries**: For communicating with the LCD over I2C.
- **NeoPixel Library**: For controlling the NeoPixel LED array.

### Install Libraries
You can install the required libraries via the Thonny IDE or directly by downloading them:
- **uRequests**: This is included in MicroPython by default.
- **NeoPixel**: Use the `neopixel` module available in MicroPython.
- **PWM/Servo Libraries**: Available in MicroPython for controlling PWM devices like servos.
- **I2C Libraries**: The `machine` module for I2C control is built-in.

---

## Wiring Instructions

### Raspberry Pi Pico W Pinout
1. **Button**:
   - Connect the button to **GPIO 1** (pin 2).
   - One side of the button goes to **GPIO 1**, and the other side connects to **GND**. 
   - Enable **Pull-Down Resistor** on the button pin.

2. **LCD Display** (using I2C):
   - Connect the **SDA** (Data) pin of the LCD to **GPIO 26** (pin 10).
   - Connect the **SCL** (Clock) pin of the LCD to **GPIO 27** (pin 11).
   - Connect the **VCC** and **GND** of the LCD to 5V and GND on the Pico.

3. **SG90 Servo Motor**:
   - Connect the servo control pin to **GPIO 5** (pin 9).
   - Connect the **VCC** and **GND** of the servo motor to 5V and GND on the Pico.

4. **NeoPixel LEDs**:
   - Connect the **Data Input** pin of the NeoPixel strip to **GPIO 28** (pin 12).
   - Connect the **VCC** and **GND** to 5V and GND respectively.

5. **LED**:
   - Connect the **positive leg** (longer) of the LED to **GPIO 15** (pin 21).
   - Connect the **negative leg** (shorter) to GND.

---

## Setup and Usage

### 1. Install MicroPython on Raspberry Pi Pico
- Follow the instructions on the [Raspberry Pi Pico MicroPython guide](https://www.raspberrypi.org/documentation/microcontrollers/micropython.html) to install MicroPython on your Raspberry Pi Pico W.

### 2. Connect Raspberry Pi Pico to the PC
- Use a USB cable to connect your Raspberry Pi Pico to your PC.

### 3. Upload Code
- Open the `main.py` file and upload it to your Raspberry Pi Pico using Thonny or your preferred IDE.
- Ensure that the necessary libraries are available on your Raspberry Pi Pico.

### 4. Run the System
- After uploading, the system will connect to the Wi-Fi network and continuously wait for button presses.
- When the button is pressed:
  - The servo will move to 0° and then to 90°.
  - The NeoPixel array will light up.
  - The LCD will display a random exchange rate fetched from an API.

---

## Code Overview

### **main.py**
- Initializes all the necessary hardware components (LCD, button, servo, NeoPixel).
- Connects the Raspberry Pi Pico W to Wi-Fi and retrieves data from an external API.
- Displays exchange rates on the LCD and controls hardware components based on button presses.

### **Networking (networking.py)**
- Handles Wi-Fi connection and ensures the Raspberry Pi Pico W stays connected to the network.

### **LCD Display (lcd_display.py)**
- Initializes and controls the 16x2 LCD display to show the data fetched from the API.

### **Button Control (button_control.py)**
- Detects button presses and triggers actions, including servo movement and fetching exchange rates.

### **Servo Control (servo_control.py)**
- Controls the SG90 servo motor, allowing it to move to different positions (0° and 90°).

### **NeoPixel Control (neopixel_control.py)**
- Initializes and controls a NeoPixel array, allowing it to display different colors based on system conditions.

### **Exchange Rate (exchange_rate.py)**
- Fetches exchange rate data from an external API (ExchangeRate-API) and selects a random conversion rate to display.

---

## Future Improvements
- **User Interface (UI)**: Enhance the LCD display to show more detailed information or even a graphical UI.
- **Error Handling**: Add better error handling for API requests and hardware malfunctions.
- **Additional Hardware**: Integrate more sensors or control more hardware components like motors or displays.

---
