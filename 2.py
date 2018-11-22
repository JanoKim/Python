def foo():
	b = 123
	def bar():
		nonlocal b
		b = 456
		print(b)
	bar()
	print(b)
print(foo())
##局部变量
#内嵌
#全局变量 
#内建？？？
#print(""sassds"afasfas'''	"")
print(__name__)
#if __name__ == '__main__':
#	print(globals())
	#print(locals())\
def add(x,y):
	print(id(x),id(y))
	x = 2
	y = 6
	print(id(x),id(y))
	return x+y
a = 1
b = 2
print(id(a),id(b))
add(a,b)
print(id(a),id(b))

for n in range(1,20):
	for x  in range(2,n):
		if n%x == 0:
			print(n,x)
	else:
		print(n,'素数')