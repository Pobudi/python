#doubled = [n * 2 for n in range(1, 5)]
#print(doubled)


names = ["Alex", "Beth", "Caroline", "Eleanor", "Dave", "Freddie"]
upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)
