#Chapter 3 - Exercise 6
#You now only have space for 2 guests
#The program from exercise 4-5
guests = ["Grandfather Santosito", "Anne Hathaway", "Tom Holland"]
def guest_invite():
        for x in guests:
            print(f"\tHello {x}, let's meet for dinner sometime.")
guest_invite()
unavailable_guest = guests[2]
print(f"\n[{unavailable_guest} is unable to make it.]")
guests[2] = "new guy"
print("The new messages will be handed out: ")
guest_invite()
#The added code:
print("\n[Unfortunately, you are only able to invite two people for dinner.]")
uninvited_guest = guests.pop(1) #The uninvited guest now that there's only space for 2
print(f"\tHello {uninvited_guest}, I apologize but there's no more room on the table.")
guest_invite()
print("Deleting the list...")
del(guests[:]) #code to delete all elements in the list
print(guests) #To print an empty list