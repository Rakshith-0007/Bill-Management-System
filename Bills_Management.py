import datetime
print("Enter a suitable code")
process_code = int(input("1.Drinking water\n2.electric bill\n3.water bill\n"))
date = str(datetime.date.today())

def Drinking_Water():
    global date
    print("Enter suitable code")
    process_code_2 = int(input("1.Purchased new can of water\n2.See history\n"))
    if process_code_2 == 1:
        file_1 = open("Drinking_water.txt", "a")
        file_1.write(f"Took water on {date}\n")
        print("Data saved succesfully")
    elif process_code_2 == 2:
        file_1 = open("Drinking_Water.txt","r")
        print(file_1.readlines())

def electric_bill():
    global date
    print("Enter suitable code")
    process_code_2 = int(input("1.Input bill detail\n2.See bill history\n"))
    if process_code_2 == 1:
        bill_value = input("Enter bill value\n")
        file_1 = open("electric_bill.txt", "a")
        file_1.write(f"Bill paid on date {date} is {bill_value}\n")
        print("Data saved succesfully")
    elif process_code_2 == 2:
        file_1 = open("electric_bill.txt", "r")
        print(file_1.readlines())



def water_bill():
    global date
    print("Enter suitable code")
    process_code_2 = int(input("1.Input Water bill detail\n2.See bill history\n"))
    if process_code_2 == 1:
        bill_value = input("Enter bill value\n")
        file_1 = open("Water_bill.txt", "a")
        file_1.write(f"Bill paid on date {date} is {bill_value}\n")
        print("Data saved succesfully")
    elif process_code_2 == 2:
        file_1 = open("Water_bill.txt", "r")
        print(file_1.readlines())


if process_code == 1:
    Drinking_Water()
elif process_code == 2:
    electric_bill()
elif process_code == 3:
    water_bill()
else:
    print("invalid Code Re-Run the the program")

