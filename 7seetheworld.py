#Chapter 3 - Exercise 7
#5 places in the world I'd like to visit
visit_places = ["Hawaii", "Italy", "Singapore", "Greece", "New Zealand"]
print(visit_places) #print list in origial order
print(f"Using the code sorted() to sort the list without modifying the actual list:", sorted(visit_places)) 
print(f"The original list is still the same: \n\t{visit_places}")
print(f"Using the code sorted(reverse=True) to reverse sort the list without modifying the actual list:", sorted(visit_places, reverse=True))
print(f"The original list is still the same: \n\t{visit_places}")
visit_places.reverse() #Changing the order of the original list
print(f"The list is now reversed: \n\t{visit_places}")
visit_places.reverse() #Changing it back to its original
print(f"The list is now back to its original: \n\t{visit_places}")
visit_places.sort() #Sorting list in alphabetical order
print(f"The list is now in alphabetical order: \n\t{visit_places}")
visit_places.sort(reverse=True) #Sorting list in reverse alphabetical order
print(f"The list is now in reverse alphabetical order: \n\t{visit_places}")