from utils.constants import IP_REACHABLE_FILE, IP_UNREACHABLE_FILE #importing the constants from the utils/constants.py file

def log_result(ip, reachable):
    filename = IP_REACHABLE_FILE if reachable else IP_UNREACHABLE_FILE
    with open(filename, 'a') as f:
        f.write(f"{ip}\n") # Append the IP address to the file in a new line. 
        
