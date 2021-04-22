import sys
import numpy
import pandas as pd

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


print(greet('World'))
print(greet('Luke'))

# print "World"

x = 0
z = 0
if x < 1:
    #print("x is less than 1")
    msg = "z is less than 1"
else:
    msg = "x is more than 1"

print(msg)

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

print(df)

print(df.dtypes)
