import random

names = input("Wer ist alles dabei?\n").split(", ")
count = len(names)

rand_number = random.randint(0, count - 1)

print(f"{names[rand_number]} muss heute die Rechnung bezahlen!")