import signal
import argparse
from parse_input import parse_input
from ping_ip import ping_ip
from log_result import log_result
from signal_handler import signal_handler

def cli():
    signal.signal(signal.SIGINT, signal_handler)

    parser = argparse.ArgumentParser(
        description="PingSPY CLI Tool - A simple tool to ping IP addresses and logs results.",
        epilog="Example usage:\n"
               "  pingspy --ip 10.0.0.1\n"
               "  pingspy --ip 10.0.0.1,10.0.0.2,10.0.0.3\n"
               "  pingspy --file iplist.txt",
        formatter_class=argparse.RawTextHelpFormatter
    )

    group = parser.add_mutually_exclusive_group(required=True) # Ensure that either --ip or --file is provided, but not both.
    group.add_argument(
        '--ip',
        type=str,
        help="A single IP or multiple IPs separated by commas.\nExample: --ip 10.0.0.1 or --ip 10.0.0.1,10.0.0.2"
    )
    group.add_argument(
        '--file',
        type=str,
        help="Path to text file containing a list of IPs (one IP address per line).\nExample: --file iplist.txt"
    )

    args = parser.parse_args() # Parse the command line arguments provided by the user.

    ip_input = args.file if args.file else args.ip
    ip_list = parse_input(ip_input)

    for ip in ip_list:
        if not ip:
            print(f"This IP address is invalid, skipping: '{ip}'") # Check if the IP address is empty or invalid or white spaces.
            continue

        print(f"Pinging {ip}...")
        response = ping_ip(ip)

        if response is not None:
            print(f" ✅ {ip} is reachable. Response time: {response:.2f} ms")
            log_result(ip, reachable=True)
         
        else:
            print(f" ❌ {ip} is not reachable.")
            log_result(ip, reachable=False)
            
    print("\nIP results logged. use 'cat reachable_ips.txt' for reachable 'cat unreachable_ips.txt' for unreachable IP's \n")

# call the cli function to start the program.
# The cli function is the entry point of the program. It handles command line arguments,
# parses the input, pings the IP addresses, and logs the results.
if __name__ == "__main__":
    cli()