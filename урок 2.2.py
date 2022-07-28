a = 10
b = 9
buf = a
a = b
b = buf
print(f"a = {a}", f"b = {b}")

a = 10
b = 9
c = 12
a,b,c = c,b,a
print(f"a = {a}", f"b = {b}", f"c = {c}")