glossary = {
    'list': 'A collection of items in a particular order.',
    'tuple': 'A collection of items similar to a list, but immutable.',
    'dictionary': 'A collection of key-value pairs.',
    'variable': 'A reserved memory location to store a value.',
    'function': 'A block of code that only runs when it is called.'
}

# Print each word and its meaning
for word, meaning in glossary.items():
    print(f"{word.title()}:\n    {meaning}\n")