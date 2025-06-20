import os
import time
import math

def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    print("\033[0;32m\n===BMI CALCULATOR===")
    print("\033[0;37mPlease, choose the measurement system:")
    print("1 - Imperial ")
    print("2 - Metric")
    print("3 - Leave")

def round_bmi(bmi, places=2, mode="normal"):
    if mode == "up":
        return math.ceil(bmi * (10**places)) / (10**places)
    elif mode == "down":
        return math.floor(bmi * (10** places)) / (10** places)
    else:
        return round(bmi, places)

def bmi_category(BMI):
    if BMI < 16.0:        
        print("\033[0;31mYou are Severely UnderWeight.")
    elif 16.0 <= BMI < 18.5:
        print("\033[0;31mYou are UnderWeight.")
    elif 18.5 <= BMI < 24.9: 
        print("\033[0;34mYou are in Normal Range.")
    elif 25 <= BMI < 29.9:
        print("\033[0;31mYou are OverWeight.")
    elif 30 <= BMI < 34.9:
        print("\033[0;31mYou have obesity class I.")
    elif 35 <= BMI < 39.9:
        print("\033[0;31mYou have obesity class II.")
    elif BMI >= 40:
        print("\033[0;31mYou have obesity class III.")

while True:
    clean_screen()
    menu()
    choice = input("\033[0;32mPlease, choose one option:")

    if choice == "1":
        clean_screen()
        try:
            Height = float(input("\033[0;37mInput your Height(In): "))
            Weight = float(input("Input your Weight(Lbs): "))
            BMI = (Weight * 703) / (Height * Height)
            BMI = round_bmi(BMI, 2, mode="normal") #Round to 2 decimal numbers
            print(f"\033[0;32mYour BMI index is {BMI}.")
        
            bmi_category(BMI)
                
            print("\033[0;32mPress ENTER to return to the menu.")
            input()

        except ValueError:
            print("\033[0;31mInvalid input! Please enter numeric values.")
            input("\033[0;31m\nPress ENTER to continue...")
                

    elif choice == "2":
        clean_screen()
        try:
            Height = float(input("\033[0;37mInput your Height(M): "))
            Weight = float(input("Input your Weight(KG): "))
            BMI = Weight / (Height ** 2)
            BMI = round_bmi(BMI, 2, mode="normal") #Round to 2 decimal numbers
            print(f"\033[0;32mYour BMI index is {BMI}.")

            bmi_category(BMI)
        
            print("\033[0;32mPress Enter to return to the menu.")
            input()

        except ValueError:
            print("\033[0;31mInvalid input! Please enter numeric values.")
            input("\033[0;31m\nPress ENTER to continue...")

    elif choice == "3":
        print("\033[0;31mClosing tab...")
        time.sleep(2)
        break
            


    
    

    
