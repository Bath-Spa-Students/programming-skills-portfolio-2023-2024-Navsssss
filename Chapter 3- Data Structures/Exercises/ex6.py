guests = ['Ryan reynolds', 'The Rock', 'Mohanlal']

name = guests[0].title()
print(name + ", i would love for you to come to my dinner.")

name = guests[1].title()
print(name + ",i would love for you to come to my dinner.")

name = guests[2].title()
print(name + ", i would love for you to come to my dinner.")

del(guests[1])
guests.insert(1, 'Dulqur Salman')

name = guests[0].title()
print("\n" + name + ", i would love for you to come to my dinner.")

name = guests[1].title()
print(name + ", i would love for you to come to my dinner.")

name = guests[2].title()
print(name + ", i would love for you to come to my dinner.")

print("\nSorry for the unfortunate news but the dinner reservations has been limited to 2 people.")

name = guests.pop()
print("Sorry, " + name.title() + " The table is having limited seats.")

name = guests.pop()
print("Sorry, " + name.title() + " The table is having limited seats.")

name = guests.pop()
print("Sorry, " + name.title() + " The table is having limited seats.")

name = guests.pop()
print("Sorry, " + name.title() + " The table is having limited seats.")

name = guests[0].title()
print(name + ", i would love for you to come to my dinner.")

name = guests[1].title()
print(name + ",i would love for you to come to my dinner.")

del(guests[0])
del(guests[0])

print(guests)