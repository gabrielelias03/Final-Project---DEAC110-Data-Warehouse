import tkinter as tk
import time
import datetime
import socket

# Simulating a login system
def login(username, password):
    # Simulating a login process with a delay for security checks
    print(f"Attempting login for user: {username}")
    time.sleep(1)  # Simulating security checks
    if username == "admin" and password == "password123":
        return True  # Successful login
    else:
        return False  # Failed login attempt

# Simulating a brute force attack on the login system
def brute_force_attack():
    attack_info = []  # List to store attack information

    print("Initiating brute force attack on the login system...")
    time.sleep(1)
    
    # Simulating two login attempts with different passwords
    for attempt in range(1, 3):
        username = "admin"
        password = f"password{attempt}"
        print(f"Attempt {attempt}: Trying password - {password}")
        time.sleep(1)  # Simulating delay between attempts
        login_successful = login(username, password)
        if login_successful:
            print(f"Login successful! Username: {username}, Password: {password}")
            attack_info.append(f"Attempt {attempt}: Login successful - Username: {username}, Password: {password}")
            break
    else:
        print("Brute force attack unsuccessful.")
        attack_info.append("Brute force attack unsuccessful.")

    return attack_info

# Function to register attack information in a log file
def register_attack_info(attack_info):
    # Get date and time information
    current_time = datetime.datetime.now()

    # Get local host information (IP, hostname, etc.)
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    # Recording attack information in a log file
    log_file_name = "attack_log.txt"
    with open(log_file_name, "a") as file:
        file.write(f"Attacks recorded at {current_time}.\n")
        file.write(f"IP: {local_ip}\n")
        file.write("Attack Details:\n")
        for info in attack_info:
            file.write(f"{info}\n")
        file.write("=" * 50 + "\n")

    print(f"Attack information registered in '{log_file_name}'.")

# Function to open a new window using Tkinter after a delay
def open_new_window():
    time.sleep(3)  # Wait for 3 seconds before opening the window
    new_window = tk.Tk()
    new_window.title("Attack Detector")
    new_window.geometry("400x300")
    label = tk.Label(new_window, text="Attack detected! Registering information...")
    label.pack()
    new_window.mainloop()

# Perform brute force attacks
all_attack_info = []
for _ in range(175):
    attack_info = brute_force_attack()
    all_attack_info.extend(attack_info)

# Register all attack information in a single log file
register_attack_info(all_attack_info)

# Open the window after the attacks and information registration
open_new_window()
