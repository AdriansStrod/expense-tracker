#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#

expenses = []
import json
# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)
pass

while True:
    command = input("\nChoose command:")
    if command == "1":
        name= input("name:")
        category= input("Kadi izdevumi:")
        sum= int(input("cik izdevumi:"))
        vardnica ={ 
            "name": name,
            "category" : category,
            "sum": sum
        }
        print(vardnica)
        expenses.append(vardnica)
    
    elif command == "2":
        print(expenses)
    elif command == "3":
        print("10 lielakie izdevumi:")
        def sort_total(expense):
            return int(expense['total'])
        expenses.sort(key = sort_total)
        (expenses[-11:])
    elif command == "3":
        print("10 lielakie izdevumi:")
        def sort_total(expense):
            return int(expense['total'])
        expenses.sort(key = sort_total)
        (expenses[:11])
    if command == "e":
        print("Exiting...")
    break


with open("expenses.json", "w") as outfile:
    json.dump(expenses, outfile)
        # https://www.w3schools.com/python
        # https://www.w3schools.com/python

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
pass

