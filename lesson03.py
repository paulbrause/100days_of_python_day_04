line1 = ["O", "O", "O"]
line2 = ["O", "O", "O"]
line3 = ["O", "O", "O"]

map = [line1, line2, line3]

position = input("Wo soll der Schatz versteckt werden?\n")

x = ord(position[0].lower()) - 96
y = int(position[1])

map[y-1][x-1] = "X"

print(f"{line1}\n{line2}\n{line3}")