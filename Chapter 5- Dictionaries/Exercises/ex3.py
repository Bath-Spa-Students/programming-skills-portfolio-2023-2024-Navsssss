glossary = {
    'String': 'It is a series of characters.',
    'Comment': 'Its to note in a program that the Python interpreter ignores.',
    'List': 'Its a collection of items in a particular order.',
    'Loop': 'Working through a collection of items, one at a time.',
    'Dictionary': "collection of key-value pairs.",
    'Key': 'The first item in a key-value pair in a dictionary.',
    'Value': 'An item associated with a key in a dictionary.',
    'Conditional test': 'A comparison between two values.',
    'Float': 'A numerical value with a decimal component.',
    'Boolean expression': 'An expression that evaluates to True or False.',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")