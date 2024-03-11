guests = ['Ryan reynolds', 'The Rock', 'Mohanlal']

name = guests[0].title()
print(name + ", i would love for you to come to my dinner.")

name = guests[1].title()
print(name + ",i would love for you to come to my dinner.")

name = guests[2].title()
print(name + ", i would love for you to come to my dinner.")

# The rock can't make it! Let's invite Dulqur Salman instead.
del(guests[1])
guests.insert(1, 'Dulqur Salman')

# Print the invitations again.
name = guests[0].title()
print("\n" + name + ", i would love for you to come to my dinner.")

name = guests[1].title()
print(name + ", i would love for you to come to my dinner.")

name = guests[2].title()
print(name + ", i would love for you to come to my dinner.")