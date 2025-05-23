import json
import sys

coins = {
    "200p": {
        "value": "20",
        "weight": 12.00,
        "coinweight": 1.2000
    },
    "100p": {
        "value": "20",
        "weight": 8.75,
        "coinweight": 0.4375
    },
    "50p": {
        "value": "10",
        "weight": 8.00,
        "coinweight": 0.4000
    },
    "20p": {
        "value": "10",
        "weight": 5.00,
        "coinweight": 0.1000
    },
    "10p": {
        "value": "5",
        "weight": 6.50,
        "coinweight": 0.1300
    },
    "5p": {
        "value": "5",
        "weight": 2.35,
        "coinweight": 0.0235
    },
    "2p": {
        "value": "1",
        "weight": 7.12,
        "coinweight": 0.1424
    },
    "1p": {
        "value": "1",
        "weight": 3.56,
        "coinweight": 0.0356
    }
}

database = {
    "Abena": {
        "correct": 0,
        "incorrect": 0,
        "total": 0,
        "accuracy": 0,
    },
    "Malcolm": {
        "correct": 0,
        "incorrect": 0,
        "total": 0,
        "accuracy": 0,
    },
    "Jane": {
        "correct": 0,
        "incorrect": 0,
        "total": 0,
        "accuracy": 0,
    },
    "Andy": {
        "correct": 0,
        "incorrect": 0,
        "total": 0,
        "accuracy": 0,
    },
    "Sandlip": {
        "correct": 0,
        "incorrect": 0,
        "total": 0,
        "accuracy": 0,
    },
    "Liz": {
        "correct": 0,
        "incorrect": 0,
        "total": 0,
        "accuracy": 0,
    }
}

with open("coincount.txt", "r") as file:    
    temp = file.readline()        
    if temp != "":                        
        temp = json.loads(temp)               
        database = temp

fulline = "-----------------------------------------------"
line = "------------------------------------------------------------"
display = input("would you like to view all users coin counting data (y/n): ")
if display.lower() == "y":
    acc = sorted(database.items(), key=lambda x: (x[1]["accuracy"], x[0]), reverse=True)
    for x in acc:
        print(line)
        print(x[0], ":", "correct:", database[x[0]]["correct"], "incorrect:", database[x[0]]["incorrect"], "total:", database[x[0]]["total"], "accuracy:", database[x[0]]["accuracy"], "%")   
    sys.exit()

print("")
print("------------Please select coin type------------")
for key, value in coins.items():
    print(key, "value:", value["value"], "weight:", value["weight"],"coin weight:", round(value["coinweight"], 3))
    print(fulline)

name = str(input("Please can you now input your user name : ")).title()
if name not in database:
    print(f"{name} is not a valid name please try again.")
    sys.exit()
else:
    print(f"--------------{name}'s statistics.--------------")
    print("correct   : ", database[name]["correct"], "        incorrect : ", database[name]["incorrect"])
    print("")
    print("total     : ", database[name]["total"], "        accuracy  : ", database[name]["accuracy"], "%")
    print(fulline)

coinselect = input("Please select the coin contained in the bag: ")
if coinselect not in coins:
    print(f"your coin type is invalid {name}.")
    sys.exit()
else:
    print(f"Thank you {name} for choosing a valid coin type. ") 

bagvalue = coins[coinselect]["value"]
coinweight = coins[coinselect]["weight"]
singlecoin = coins[coinselect]["coinweight"]
inputweight = float(input(f"please can you enter the bags weight {name} : ")) 
if coinweight == inputweight:
    print("good job your coin weight is correct")
    database[name]["correct"] += 1
    database[name]["total"] += 1 
elif coinweight > inputweight:
    combined1 = coinweight - inputweight
    finalnumber1 = (coinweight - inputweight) / singlecoin
    rounded1 = round(combined1)
    rounded2 = round(finalnumber1)
    print(f"weight you entered is {rounded1}g too light add {rounded2} coins.")
    database[name]["incorrect"] += 1
    database[name]["total"] += 1    
else:
    combined2 = inputweight - coinweight
    finalnumber2 = (inputweight - coinweight) / singlecoin
    rounded3 = round(combined2)
    rounded4 = round(finalnumber2)
    print(f"weight you entered is {rounded3}g to heavy remove {rounded4} coins.")
    database[name]["incorrect"] += 1
    database[name]["total"] += 1
    percentage = database[name]["correct"] / database[name]["incorrect"] * 100
    per = round(percentage)
    database[name]["accuracy"] = per
    database[name]["total"] = database[name]["correct"] + database[name]["incorrect"]
    with open("coincount.txt", "w") as file:
        file.write(json.dumps(database))
    print("All database information saved to coincount.txt.")
        