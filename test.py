a = [1, 2, 3, 4, 'a', 'b', 5, 6]
b = []
for i in a:
    try:
        b.append((i+1))
    except Exception as e:
        print(e)
        continue
print(b)
