import sys
import operator

n = 6
temperatures = ['6', '3', '10', '-4', '17', '14' ]
min=sys.maxsize
for i in temperatures:
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if t < min:
        if t >= 0:
            min = t
        else:
            if (str(operator.neg(t)) not in temperatures):
                min = t
            else:
                min = -t

print(min)
