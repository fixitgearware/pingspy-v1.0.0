def load_ips_from_file(file_path):   # Function to load IPs from a file or file paths provided by the user.
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError: # Handle the case where the file does not exist. 
        print(f"File not found: {file_path}")
        return []
