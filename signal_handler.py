import sys

def signal_handler(sig, frame):
    print("\nProcess interrupted. Program will now Exit...")
    sys.exit(0)
