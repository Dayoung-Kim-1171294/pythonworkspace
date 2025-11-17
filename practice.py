# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "Black Widow", "Hulk"]
# students = [i.upper() for i in students]
# print(students)


import random

clients = 0
for number in range(1, 51):
    mins = random.randint(5, 50)
    
    if 5 <= mins <= 15:
        print(f"[o] {number} clients (time : {mins} mins)")
        clients += 1
    else:
        print(f"[ ] {number} clients (time : {mins} mins)")

print(f"\ntotal clients : {clients}")