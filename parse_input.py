import os
from load_ips import load_ips_from_file # Function to load IPs from a file or file paths provided by the user.

def parse_input(ip_input):
    if os.path.isfile(ip_input):
        print(f"Detected file input: {ip_input}") # Check if the input is a file path, and detect the file.
        return load_ips_from_file(ip_input)
    elif ',' in ip_input: # Check if the input contains commas, indicating multiple IPs.
        print("Detected multiple IPs")
        return [ip.strip() for ip in ip_input.split(',') if ip.strip()] # Split the input by commas and strip whitespace, ensuring no empty strings are included.
    else:
        print("Detected single IP") #check if the input is a single IP address.
        return [ip_input.strip()]
