import ping3
import time

def ping_ip(ip):  #function to ping an IP address from the input provided by the user. 
    try:
        response = ping3.ping(ip, timeout=2)
        time.sleep(1)
        return response
    except Exception as e:
        print(f"There is an error pinging {ip}: {e}") #print the error message if there is an error pinging the IP address.
        return None
