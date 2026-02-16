import random

friends = ["Rohit", "Harsh", "Mohan", "Gandhi", "Tapas", "Mohit"]
random_number = random.randrange(0, len(friends))
# print(random_number)
print(f"Today's Bill will be paid by: {friends[random_number]}")
print(f"Today's Bill will be paid by: {random.choice(friends)}")



