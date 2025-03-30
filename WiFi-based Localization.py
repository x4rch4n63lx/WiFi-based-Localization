# ===================================================================================
# Created By     : x_4rch4n63l_x
# Created On     : 3/30/2025 - 3:40AM
# Script Purpose : To scan and analyze available WiFi networks, providing real-time
#                  signal strengths and estimated distances to each router.
# 
# Description    : This script fetches WiFi network data using the 'netsh wlan' command,
#                  parses the output to extract SSID and signal strength details, 
#                  calculates approximate distances based on signal strength, 
#                  and displays the information in a tabulated format.
# 
#                  The script is platform-dependent and intended for Windows systems. 
#                  It also includes error handling and uses the 'tabulate' library 
#                  for a clean presentation of data.
# 
# Features       : - Fetches available WiFi network details (SSID, Signal Strength).
#                  - Calculates approximate distances to routers based on signal strength.
#                  - Displays information in a user-friendly tabular format.
#                  - Provides basic error handling for enhanced robustness.
# 
# Requirements   : - Operating System: Windows
#                  - Python 3.x 
#                  - Required Libraries: 'subprocess', 'tabulate'
#                  - Command-line access and permissions to execute 'netsh' commands.
#
#                  To install the required libraries, run the following command:
#                  pip install tabulate
# ===================================================================================

import subprocess
from tabulate import tabulate

def fetch_wifi_data():
    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "networks", "mode=bssid"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print("Failed To Retrieve WiFi Networks. Are You Sure You're On Windows?")
            return None
        
        return result.stdout
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def parse_wifi_data(raw_data):
    wifi_data = []
    lines = raw_data.split("\n")
    current_network = {}
    
    for line in lines:
        line = line.strip()
        if line.startswith("SSID"):
            if current_network:  
                wifi_data.append(current_network)
            current_network = {"Router": line.split(":", 1)[1].strip()}
        elif line.startswith("Signal"):
            current_network["Signal Strength"] = line.split(":", 1)[1].strip()
    
    if current_network:
        wifi_data.append(current_network)
    
    return wifi_data

def calculate_distance(signal_strength):
    tx_power = -30  
    path_loss_exponent = 2.7  
    
    try:
        signal = int(signal_strength.replace("%", ""))  
        rssi = -100 + (signal / 100) * 100  
        distance = 10 ** ((tx_power - rssi) / (10 * path_loss_exponent))
        return round(distance, 2)
    except ValueError:
        return None

def display_wifi_data():
    raw_data = fetch_wifi_data()
    if not raw_data:
        print("No WiFi Data Available.")
        return
    
    wifi_data = parse_wifi_data(raw_data)
    results = []
    for network in wifi_data:
        signal_strength = network.get("Signal Strength", "N/A")
        distance = calculate_distance(signal_strength) if signal_strength != "N/A" else "Invalid"
        results.append([
            network["Router"],
            signal_strength,
            f"{distance} meters" if isinstance(distance, float) else distance
        ])
    
    print("\n 🌐 Real-Time Signal Strengths An Distances 🌐")
    print(tabulate(results, headers=["Router", "Signal Strength", "Distance"], tablefmt="fancy_grid"))

if __name__ == "__main__":
    display_wifi_data()
    input("\nPress Enter To Exit...")