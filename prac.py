num : int = 5

print(num)
methods : list[str] = list(dir(num))

for method in methods:
    print(method)