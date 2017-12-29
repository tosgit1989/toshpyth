from math import exp
def rit(x, y): return pow(2 * 3.14159265, -1) * exp(-0.5 * (x * x + y * y))
v = 0
for x_i in range(-100, 101):
  for y_i in range(-100, 101):
    v += 0.01 * rit(x_i * 0.1, y_i * 0.1)

print(v)