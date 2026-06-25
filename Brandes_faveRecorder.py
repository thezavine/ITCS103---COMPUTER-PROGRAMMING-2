import os
from openpyxl import Workbook

print("\nHello, This is Azeth's Fave Recorder")
print("\nPress ENTER to continue...")

while True:
    start = input()
    if start == "":
        break
    else:
        print("Invalid input. Please press ENTER only.")

os.system("cls")

workbook = Workbook()
sheet = workbook.active

sheet.append(["ID", "First Name", "Last Name", "Birth Year", "Age"])

records = []

print("\n===============================")
print("   FAVORITE PEOPLE RECORDER")
print("===============================")

for person_id in range(1, 4):

    print(f"\n-------- Person {person_id} ---------")

    fname = input("First Name: ")

    lname = input("Last Name: ")

    birth = int(input("Birth Year: "))

    age = 2026 - birth

    records.append([person_id, fname, lname, birth, age])

    sheet.append([person_id, fname, lname, birth, age])

workbook.save("favorite_people.xlsx")

print("\n===========================")
print("      SAVED RECORDS")
print("===========================")

for data in records:

    print("\n----------------------")
    print("ID:", data[0])
    print("First Name:", data[1])
    print("Last Name:", data[2])
    print("Birth Year:", data[3])
    print("Age:", data[4])

print("\n========================================")
print("   FILE HAS BEEN SAVED SUCCESSFULLY")
print("========================================")