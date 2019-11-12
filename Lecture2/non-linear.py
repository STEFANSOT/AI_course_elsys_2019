import pylab as pl
import numpy as np
import tensorflow as tf

dsize = 500 # брой на данните(точките)
msize = 100 # 
x = np.linspace(-1, 1, dsize) # създаване на масив със равномерно подредиени стойности (х абсцисата)
y = x**2 + np.random.normal(size=dsize)/4 # създаване на зависимостта (у абсцисата)

model = tf.keras.Sequential([ # sequential създава невронна мрежа
    tf.keras.layers.Dense(2, activation="tanh", kernel_initializer=tf.keras.initializers.GlorotNormal(), input_shape = (1,)), # Dense е слой на мрежата - първият аргумент е броят неврони в слоя, вторият е активиращата функция, третият аргумент представлява xavier метода, а четвъртият аргумент представлява броят на входовете
    tf.keras.layers.Dense(1, activation="linear", kernel_initializer=tf.keras.initializers.GlorotNormal()) # kernel_initializer е xavier метода
])

model.compile(optimizer="adam",
              loss = tf.keras.losses.MeanSquaredError()) # функция на грешката

model.fit(x, y, epochs=1000)
pl.plot(np.linspace(-1, 1, msize), model.predict(np.linspace(-1, 1, msize)), "r-")

pl.scatter(x, y) # изчертава данните(точките)
pl.show()

# xavier method, adam algorithm - той сам си настройва learning rate-a
