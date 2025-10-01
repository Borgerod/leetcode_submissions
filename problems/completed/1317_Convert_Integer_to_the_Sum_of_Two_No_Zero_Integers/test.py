# def isNonZero(num:int) -> bool:
# 	print(f"num={str(num)}:")
# 	if "0" not in str(num):
# 		print(f'	Invalid; "0" IS in "{str(num)}"')
# 	else:
# 		print(f'	Valid; "0" NOT in "{str(num)}"')
# 	return "0" in str(num)



# num = 10
# # print(isNonZero(num))
# print("")
# isNonZero(num)
# print("")
# print("")
# print("")

# if isNonZero(num):
# 	print("print CONTINUES")
# else:
# 	print("print CONTINUES")


n = 11
_n = n/2
is_odd = True
# if _n.is_integer():
if (n/2).is_integer():
	# is int / even number
	is_odd = False
	print("True")
else: 
	print("False")

n = 11
if (n/2).is_integer:
	print("True")
else:
	print("False")