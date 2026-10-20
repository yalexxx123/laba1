import math
 
a = float(input("Введите а: "))
b = float(input("Введите b: "))

z1 = (math.cos(a) - math.cos(b)) ** 2 - \
     (math.sin(a) - math.sin(b)) ** 2

z2 = -4 * math.sin((a - b) / 2) ** 2 * \
     math.cos(a + b)

print("z1 =", round(z1, 6))
print("z2 =", round(z2, 6))