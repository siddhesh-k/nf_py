import os
import string

def string_methods():
    string1 = "hello world!"
    string2 = "hello,split,on,COMMAS"
    string3 = "Replace every ace with !!!"

    print(string1.capitalize())
    print(string1.upper())
    print(string2.lower())
    print(string3.strip())
    print(string1.strip(), string2.strip())
    print(string3.replace("ace", "!!!", 2))
    print(string1.startswith("hello"))
    print(string2.endswith("COMMAS"))
    print(string1.count("l"))
    print(string2.isalpha())
    print(string3.isalnum())
    print(string2.isdigit())
    print(string2.isspace())
    string4 = "**".join([string1, string2, string3])
    print(string4)


def check_if_sorted_list():
    integers = input("Enter integers separated by space: ")
    integers = integers.split(" ")
    previous = integers[0]
    for integer in integers:
        if previous > integer:
            return print(f"Integers are not in increasing order at index.")
    return print("Integers are in increasing order.")


def exception_handling():
    integers = input("Enter integers separated by space: ")
    integers = integers.split(",")
    previous = integers[0]
    try:
        for integer in integers:
            # print(integer, previous)
            if int(previous) > int(integer):
                return print(f"Integers are not in increasing order at index.")
            previous = integer
        return print("Integers are in increasing order.")
    except Exception as e:
        print("Invalid input.\n", e)


def permutation():
    integers1 = input("Integer Sequence1 (separated by comma): ")
    integers2 = input("Integer Sequence2 (separated by comma): ")
    method=input("1: Permutation using sort\n2: Permutation using dictionary\nEnter1 or 2: ")
    integers1 = integers1.split(",")
    integers2 = integers2.split(",")
    if method == 1:
        integers1= integers1.sort()
        integers2 = integers2.sort()
        if integers1 == integers2:
            print("Sequence 2 is permutation of Sequence 1")
        else:
            print("Sequence 2 is not permutation of Sequence 1")
    else:
        int1Dict=dict()
        int2Dict=dict()
        for integer in integers1:
            if integer not in int1Dict.keys():
                int1Dict[integer]=integers1.count(integer)
        for integer in integers2:
            if integer not in int2Dict.keys():
                int2Dict[integer]=integers2.count(integer)
            # if integer2 not in int2Dict.keys():
            #     int1Dict[integer2]=integers2.count(integer2)
        print(int1Dict,int2Dict)
        if int1Dict == int2Dict:
            print("Sequence 2 is permutation of Sequence 1")
        else:
            print("Sequence 2 is not permutation of Sequence 1")

def caesar_cipher():
    plain_text = input("Enter a message to be encrypted: ")
    encrypt_by = int(input("Enter inter to encrypt with: "))
    # plain_text=plain_text.split("")
    # for letter in plain_text:
    # encryption = "".join([chr(ord(letter)+encrypt_by) if letter in string.ascii_letters else letter for letter in plain_text ])
    encryption = "".join([
        chr((ord(char) - ord('A') + encrypt_by) % 26 + ord('A')) if char in string.ascii_uppercase else
        chr((ord(char) - ord('a') + encrypt_by) % 26 + ord('a')) if char in string.ascii_lowercase else
        char
        for char in plain_text
    ])
    print("Your encrypted message is:", encryption)
    decryption = "".join([
        chr((ord(char) - ord('A') - encrypt_by) % 26 + ord('A')) if char in string.ascii_uppercase else
        chr((ord(char) - ord('a') - encrypt_by) % 26 + ord('a')) if char in string.ascii_lowercase else
        char
        for char in encryption
    ])
    print("Your decrypted message is:", decryption)

def supperMarket_inventory_system():
    inventory = {
        "Apple": {"price": 0.5, "quantity": 100},
        "Banana": {"price": 0.3, "quantity": 150},
        "Orange": {"price": 0.8, "quantity": 80}
    }

    while True:
        # os.system("cls")
        print("""Supermarket Inventory System
1- Display Inventory 
2- Add a new item 
3- Update an existing item 
4- Delete an item 
5- Get total worth of inventory 
6- Exit """)
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                print("Name, Price, Quantity")
                for item in inventory.keys():
                    print(item.title(),',',inventory[item]["price"],',',inventory[item]["quantity"],)
            case 2:
                try:
                    os.system("cls")
                    print("Add: -")
                    name =input("Enter item name: ")
                    price = float(input("Enter price: "))
                    quantity= int(input("Enter quantity: "))
                    inventory[name.title()] = {}
                    inventory[name.title()]["price"]=price
                    inventory[name.title()]["quantity"]=quantity
                    print(f"{name.title()} added successfully.")
                except:
                    print("Please enter numeric value")
            case 3:
                os.system("cls")
                print("Update: -")
                name = input("Enter item name: ")
                price = float(input("Enter new price: "))
                quantity = int(input("Enter new quantity: "))

                inventory[name.title()]["price"] = price
                inventory[name.title()]["quantity"] = quantity
                print(f"{name.title()} updated successfully.")
            case 4:
                os.system("cls")
                print("Delete: -")
                name = input("Enter item name: ")
                inventory.pop(name.title())
                print(f"{name.title()} deleted successfully.")
            case 5:
                os.system("cls")
                inventory_worth=0

                for item in inventory.keys():
                    inventory_worth += (float(inventory[item]["price"]) * int(inventory[item]['quantity']))
                print(f"Total worth of inventory: {inventory_worth}$")
            case 6:
                return False


while True:
    user_input = input("Enter exercise number (1-6) or 'q' to exit: ")

    if user_input != "q":
        if user_input == "1":
            string_methods()
        if user_input == "2":
            check_if_sorted_list()
        if user_input == "3":
            exception_handling()
        if user_input == "4":
            permutation()
        if user_input == "5":
            caesar_cipher()
        if user_input == "6":
            supperMarket_inventory_system()


    elif user_input == "q":
        exit()
