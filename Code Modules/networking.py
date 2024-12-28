import time
import network

# Wi-Fi credentials
ssid = 'SHAW-323D'
password = 'eighty3134alert'  # This should be ‘airuc-guest’ on campus Wi-Fi

def connect():
    """
    This function connects the Raspberry Pi Pico W to the specified Wi-Fi network.
    It waits until the device is connected to the network.
    """
    wlan = network.WLAN(network.STA_IF)  # Create a station interface (client mode)
    wlan.active(True)  # Activate the WLAN interface
    wlan.connect(ssid, password)  # Connect to the Wi-Fi network
    while not wlan.isconnected():
        print('Waiting for connection...')
        time.sleep(1)  # Wait for 1 second before checking again

    print('Connected:', wlan.ifconfig())  # Print the device's IP configuration once connected
