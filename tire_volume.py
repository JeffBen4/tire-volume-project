# I add a funtion to ask a question to the user and add his/her phone number.
import math
from datetime import datetime

current_date_and_time = datetime.now()
current_date = datetime.now().strftime("%Y-%m-%d")

pi = math.pi
width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): ")) 

volume = pi * (width ** 2) * ratio * (width * ratio + 2540 * diameter) / 10000000000

print(f"The approximate volume is {volume:.2f} liters.")
question = input("Do you want to buy a tire with these dimentions?(yes/not): ")
if question.lower() == "yes":
    number = input("OK. Please add your phone number: ")
    with open("volume.txt", "a") as file:
        print(f"{current_date}, {width:.0f}, {ratio:.0f}, {diameter:.0f}, {volume:.2f}, Phone Number: {number}", file=file)
elif question.lower() == "not":
    with open("volume.txt", "a") as file:
        print(f"{current_date}, {width:.0f}, {ratio:.0f}, {diameter:.0f}, {volume:.2f}", file=file)
else:
    print("Please, use yes or not.")