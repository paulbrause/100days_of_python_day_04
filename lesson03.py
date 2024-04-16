line1 = ["O", "O", "O"]
line2 = ["O", "O", "O"]
line3 = ["O", "O", "O"]

map = [line1, line2, line3]

position = input("Wo soll der Schatz versteckt werden?\n")
chars = ["a", "b", "c"]

x = chars.index(position[0].lower())
y = int(position[1]) - 1

map[y][x] = "X"

print(f"{line1}\n{line2}\n{line3}")