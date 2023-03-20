"""
Python: continue e break
"""
for i in range(10):
    if i >= 5 and i <= 8:
        continue
    print(i)

print("\n")

for i in range(10):
    if i >= 5 and i <= 8:
        break
    print(i)