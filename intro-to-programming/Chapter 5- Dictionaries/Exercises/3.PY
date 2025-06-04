glossary = {
    'list': 'A collection of items in a particular order.',
    'tuple': 'A collection of items similar to a list, but immutable.',
    'dictionary': 'A collection of key-value pairs.',
    'variable': 'A reserved memory location to store a value.',
    'function': 'A block of code that only runs when it is called.',
    'loop': 'A sequence of instructions that repeats until a condition is met.',
    'conditional': 'A statement that only executes if a condition is true.',
    'string': 'A sequence of characters.',
    'integer': 'A whole number without decimals.',
    'boolean': 'A data type with two possible values: True or False.'
}

# Loop through the dictionary and print each word and its meaning
for word, meaning in glossary.items():
    print(f"{word.title()}:\n    {meaning}\n")