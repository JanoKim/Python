"""import .. as...
	from ... import..
	from ... import *
	from ... import ... as
"""
#from math import sin as s
#print(s(55))
import turtle as t
t.pensize(3)
colors=["red","pink","green","purple"]
for x in range(50):
	t.fd(3*x)
	t.color(colors[x%4])
	t.left(92)
t.done()