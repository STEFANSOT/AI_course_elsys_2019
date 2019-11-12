from pylab import *
from numpy import *

# sudo apt install python3 python3-pip
# pip(3) install numpy matplotlib pytk

# моделът е y = ax + b и се опитваме да намерим параметрите 

dsize = 500 # размер на данните (по него се определя точността при изчислението на параметрите на модела)

x = linspace(0, 1, dsize) # Генерира 500 числа на равни разстояния и ги записва в масив - х-овете
y = x * 2 + 1 + random.normal(size = dsize) / 3 # модел, random.normal(size) / num е разпределяща функция, която изчислява вероятността да има число на разстояние от 0 - колкото е по - далеч, толкова е по - малко вероятно да го има като при скалата с оценките - масово ще има четворки, но много рядко двойки и шестици - у-ците

a = sum((x - mean(x)) * (y - mean(y))) / sum((x - mean(x)) ** 2) # изчисляване на параметър, mean е средно аритметично
b = mean(y) - a * mean(x) # аналогично на a

print("a is ", a)
print("b is ", b)

model_x = linspace(0, 1, 2) # абсцисна ос - от 0 до 1
scatter(x, y) # изписване на точките
plot(model_x, model_x * a + b, 'r-', linewidth = 2) #  model_x * a + b е динамично сметната ординатна ос, с цел да влезнат всички точки в графиката
show()

# email for contact - teodorvb@gmail.com
