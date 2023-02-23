import csv
import os
import signal

# Define a signal handler function to handle the timeout
def handler(signum, frame):
    print('Timeout exceeded')
    raise Exception('Timeout exceeded')

# Register the signal handler for SIGALRM signal
signal.signal(signal.SIGALRM, handler)

# Set the timeout to 60 seconds
signal.alarm(60)

# Open the CSV file and read the data
with open('new_names.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')  # Specify semicolon delimiter
    header = next(reader)  # Read the header row
    print(header)
     for row in reader:
        print(row)
        old_name = row[0]
        new_name = row[1]
        _, ext = os.path.splitext(old_name)
        new_name = os.path.join(os.path.dirname(old_name), os.path.splitext(new_name)[0]) + ext
        os.rename(old_name, new_name)
        print('Renamed {} to {}'.format(old_name, new_name))

# List the files in the directory
files = os.listdir('.')
print('Renamed files:')
for file in files:
    if file.endswith(('.jpg', '.jpeg', '.png')):
        print(file)

# Disable the alarm
signal.alarm(0)
