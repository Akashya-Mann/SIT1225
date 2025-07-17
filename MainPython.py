import serial
import time
import random
from datetime import datetime

ser = serial.Serial('COM5', 9600)
time.sleep(2) 
while True:
    try:
        delay_time
        print(f"{datetime.now().strftime('[%M:%S]')} Sleeping for {delay_time} seconds before sending.")
        time.sleep(delay_time)
        print(f"{datetime.now().strftime('[%M:%S]')}  sleeping finsihed .")
    except NameError:
        pass 
    number = random.randint(1, 5)
    timestamp = datetime.now().strftime("[%M:%S]")
    print(f"{timestamp} Sent: {number}")
    ser.write(f"{number}\n".encode())
    while ser.in_waiting == 0:
        pass

    response = ser.readline().decode().strip()
    timestamp = datetime.now().strftime("[%M:%S]")
    print(f"{timestamp} Received: {response}")

    try:
        delay_time = int(response)
    except ValueError:
        print("Invalid No skipping sleep.")
        delay_time = 1
