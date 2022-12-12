#Chapter 3 - Exercise 5
guests = ["Grandfather Santosito", "Anne Hathaway", "Tom Holland"]
def guest_invite(): # a function to easily repeat the program of inviting the people
        for x in guests:
            print(f"\tHello {x}, let's meet for dinner sometime.")
guest_invite()
unavailable_guest = guests[2] #The guest that is unavailable for the dinner
print(f"[{unavailable_guest} is unable to make it.]")
guests[2] = "new guy" #The new guest to replace the unavailable guest
print("The new messages will be handed out: ")
guest_invite() #The new list of invitations