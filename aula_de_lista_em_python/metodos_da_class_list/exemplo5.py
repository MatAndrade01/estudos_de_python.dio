liguagens = ['Python', 'Java', 'C', 'Java', 'Charp']

print(sorted(liguagens, key=lambda x: len(x)))
print(sorted(liguagens, key=lambda x: len(x), reverse=True))

print(sorted(liguagens))