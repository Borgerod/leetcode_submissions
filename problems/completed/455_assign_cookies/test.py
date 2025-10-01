
_g=[100,20,2,1]
print(_g)
for i in range(len(_g)):
	print(i)
	print(_g[i])
	_g.pop(i)
	break
_g.remove(max(_g))
print(_g)