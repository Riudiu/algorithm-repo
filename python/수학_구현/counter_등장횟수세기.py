from collections import Counter

counter = Counter(['red', 'green', 'blue', 'red', 'blue', 'blue'])

print(counter['green'])
print(counter['blue'])
print(dict(counter))