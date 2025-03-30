# WiFi-based-Localization
Created By     : x_4rch4n63l_x
Created On     : 3/30/2025 - 3:40AM
Script Purpose : To scan and analyze available WiFi networks, providing real-time
                 signal strengths and estimated distances to each router.
Description    : This script fetches WiFi network data using the 'netsh wlan' command,
                 parses the output to extract SSID and signal strength details, 
                 calculates approximate distances based on signal strength, 
                 and displays the information in a tabulated format.
                 The script is platform-dependent and intended for Windows systems. 
                 It also includes error handling and uses the 'tabulate' library 
                 for a clean presentation of data.
Features       : - Fetches available WiFi network details (SSID, Signal Strength).
                 - Calculates approximate distances to routers based on signal strength.
                 - Displays information in a user-friendly tabular format.
                 - Provides basic error handling for enhanced robustness.
Requirements   : - Operating System: Windows
                 - Python 3.x 
                 - Required Libraries: 'subprocess', 'tabulate'
                 - Command-line access and permissions to execute 'netsh' commands.
                 To install the required libraries, run the following command:
                 pip install tabulate
