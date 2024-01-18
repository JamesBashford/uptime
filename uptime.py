import subprocess
import time
import csv
import os
import sys

hostname = "www.google.com"  # Use a well-known server for pinging
file_name = "uptime.csv"  # Name of the CSV file
start_time = time.time()  # Get the current time in seconds

if not os.path.isfile(file_name):
    with open(file_name, "w") as file:  # Create the CSV file if it doesn't exist
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Status"])  # Write the header row

while True:  # Run the loop indefinitely until escape key is pressed
    response = subprocess.call(["ping", "-c", "1", hostname])  # Send a ping request
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")  # Get the current timestamp

    with open(file_name, "a") as file:  # Open the CSV file in append mode
        writer = csv.writer(file)
        if response == 0:
            print(f"{hostname} is up!")
            writer.writerow([current_time, "Up"])  # Write the timestamp and status to the CSV file
        else:
            print(f"{hostname} is down!")
            writer.writerow([current_time, "Down"])  # Write the timestamp and status to the CSV file

    time.sleep(5)  # Wait for 5 seconds before pinging again
    
    # Check for escape key press
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = input()
        if line == "escape":
            break

print("Program terminated by escape key.")
