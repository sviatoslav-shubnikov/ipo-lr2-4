import math

x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

h = ((x**(y+1) + math.exp(y-1)) * (1+abs(y-x)))/(1+x*abs(y-math.tan(z))) + ((abs(y-x)**2)/2) + ((abs(y-x)**3)/3)

print(f"h = {h}")
