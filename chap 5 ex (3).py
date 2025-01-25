glossary = {
    'string': 'Used for representing textual data.',
    'comment': 'Used for representing textual data.',
    'list': 'A data structure in Python that is a mutable, or changeable, ordered sequence of elements.',
    'loop': 'Repeating something over and over until a particular condition is satisfied',
    'dictionary': "A mutable collection of key-value pairs that allows for efficient data retrieval using unique keys.",
    'key': 'analogous to indexes of a list.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")