import json
import os
def load_guests():
    if not os.path.exists("guests.json"):
        return []
    with open("guests.json","r",encoding="utf-8") as file:
        return json.load(file)
    
def save_guests(guests):
    with open("guests.json","w",encoding="utf-8") as f:
        json.dump(guests,f,ensure_ascii=False,indent=4)
        
def add_guests():
    guests = load_guests()
    print("Current guests count",len(guests),"\n")
    name = input("Please, Enter your name: ")
    if not name.strip():
        print("Name cannot be empty!")
        return
    try:
        room = int(input("Please, Enter room number: "))
        if room <=0:
            print("Please, Enter a room number higher than 0")
            return
    except ValueError:
        print("Room number should be a number!")
        return
    telefon = input("Please, Enter your phone number: ")
    
    if guests:
        new_id = max(g["id"] for g in guests) + 1
    else:
        new_id = 1
    for i in guests:
        if room == i["room_number"]:
            print("This room is booked. Please Enter another room")
            return
        
    if telefon.startswith("+998") and len(telefon) == 13 and telefon[4:].isdigit():
        guests.append({
        "id":new_id,
        "name":name,
        "room_number":room,
        "phone":telefon
    })
        save_guests(guests)
        print("Successfully added")
    else:
        print("Number should only start with +998")
def remove_guest():
    guests = load_guests()
    if not guests:
        print("List is empty yet!")
        return
    list_guests()
    guest_id = input("Please enter an id you want to remove: ")
    new_guests = [g for g in guests if str(g["id"]) !=guest_id]
    if len(guests) == len(new_guests):
        print("ID is not found!")
    else:
        save_guests(new_guests)
        print("Guest is successfully removed")
def list_guests():
    guests = load_guests()
    
    if not guests:
        print("There are no guests at the moment")
        return
    else:
        print("\n----Guests list ----")
        for g in guests:
            print(f"ID: {g['id']} | Name: {g['name']} |  Room number: {g['room_number']} |  Phone number: {g['phone']}")
            
        print("-----------------------\n")
        

while True:
    print("""
    Welcome to Astronum plaza hotel

    1 - Add a guest
    2 - Remove a guest
    3 - Guests list 
    
    0 - Leave the app
    """)
    try:
        choice = int(input("Please choose: "))
        if choice == 1:
            add_guests()
        elif choice == 2:
            remove_guest()
        elif choice == 3:
            list_guests()
        elif choice == 0:
            break
    except ValueError:
        print("Please enter a number")
        