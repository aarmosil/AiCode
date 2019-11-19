d = {}
f_file = open("don.txt")
for line in f_file:
    (char, fran) = line.split(';')
    realfran = ""
    for c in fran:
        if c != '\n':
            realfran += c
    char.upper()
    d[char] = realfran
f_file.close()
#===================================================================
print("Welcome to the Fighter Finder!\nTo find out what franchise your favorite Super Smash Brothers Ultimate main is from, just enter their name!")
fighter = 0
while fighter != 'e':
    fighter = input("Enter fighter name here, Enter 'e' to exit: ")
    if fighter == 'e':
        break
    fighter = fighter.lower()
    fighter = fighter.capitalize()
    if fighter in d:
        print(fighter + " is from the" + d[fighter] + " franchise!")
    elif fighter not in d:
        print("Fighter not found.")
print("Thank you for your time! Keep smashing!")
