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
    
    if mins >= 5 and mins <= 15:
        print(f"[o] {number}번째 손님 (소요시간 : {mins}분)")
        clients += 1
    else:
        print(f"[ ] {number}번째 손님 (소요시간 : {mins}분)")

print(f"\n총 탑승 승객 : {clients}분")