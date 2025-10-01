# # # print((1*8)+(0*4)+(1*2)+(1*1))

# # '''
# # 123 =1011


# # 1: 1
# # 2: 10
# # 3: 11
# # '''

# # # bin_list =[]
# # # bin_list = [int(i) for i in str(bin)]
# # # print(bin_list)

# # # # iterate a binary:
# # # for i in str(bin):
# # # 	i=int(i)
# # # 	print(type(i))

# # # bin = 1011
# # # bin =  str(bin)
# # # lenB = i = len(bin)-1
# # # # i = len(bin)-1

# # # # print(lenB)
# # # # print(i)
# # # i = 0
# # # while i<len(bin):

# # # 	print(f"i : {i}")
# # # 	b = int(bin[i])
# # # 	print(f"i:{i}, b:{b}, lenB:{lenB} --> b*2^lenB = {b}*2^{lenB} = {b*(2**lenB)}")

# # # 	lenB-=1
# # # 	i += 1 #placing



# # 1. experimental
# def bin_to_num(bin, i=0):
#     bin = str(bin)
#     return 0 if i == len(bin) else int(bin[i]) * (2 ** (len(bin) - 1 - i)) + bin_to_num(bin, i + 1)

# # 2. 
# def bin_to_num(bin, i=0, num=0):
# 	''' using while '''
# 	bin = str(bin)
# 	lenB = len(bin)-1
# 	while i<len(bin):
# 		num += int(bin[i])*(2**lenB)
# 		lenB -= 1 
# 		i += 1
# 	return num

# # # 3.
# # def bin_to_num(bin):
# # 	''' using for '''
# # 	bin = str(bin); lenB = len(bin)-1
# # 	return sum(int(b)*(2**(lenB-i)) for i, b in enumerate(bin))
# # # 4.
# # def bin_to_num(bin):
# # 	bin = str(bin)
# # 	return sum(int(bin[i]) * (2 ** (len(bin) - 1 - i)) for i in range(len(bin)))
	

# bin = 1011
# x = bin_to_num(bin)
# print(x)

# # # 1=1*2^3=8
# # # 1=0*2^2=0
# # # 1=1*2^1=2
# # # 1=1*2^0=8


# # # 123=(1*100)+(2*10)+(3*1)
# # # 1011=(1*8)+(0*4)+(1*2)+(1*1)

# # # print((1*100)+(2*10)+(3*1))


# # num = 123
# # _num = str(num); lenN = len(_num)-1
# # x=10
# # for i, n in enumerate(_num):
# # 	print(i)
# # 	print(f"x**(lenN-i) = {x}**({lenN}-{i}) = {x**(lenN-i)}")
# # 	# i+=1
	
# # bin = sum(int(n)*(x**(lenN-i)) for i, n in enumerate(_num))
# # # print(bin)





# # num = 123
# # num = str(num)
# # # bin = sum(nums)
# # nums = [
		
# # 		int(num[i]) 
# # 		* 
# # 		(2 ** (len(num) - 1 - i)) 
# # 		for i in range(len(num))

# # 		]

# # import math
# # # get exp
# # result = 8
# # base = 2
# # exponent = math.log(result, base) # -> 3.0


# # # get base
# # result = 8
# # exp = 3
# # base = result ** (1/exp)   # 8 ** (1/3) -> 2.0


# # '''	1 = 1*(2**3) = 8 '''
# # bit = 1
# # num = bit*(2**3)
# # num = 8


# # num/(2**3) = bit
# # # __________________________________________________

# # bin=10
# # 1=1*2^1=8
# # 0=0*2^0=0



# # num = 7
# # bin = 0
# # bin = [False] #represents 'num = 0'
# # for i in range(num):
# # 	print(f"i:{i}")
# # 	if bin[-1]: #last item is true
# # 		print("	last item is True -> appending False")
# # 		bin.append(False)
# # 		print("	",bin)

# # 	elif len(bin) > 1 and all(bin):
# # 		''' if len(bin)>1 and all items are true -> reset all but first to False '''
# # 		print("	all item is True -> appending False")
# # 		bin.append(False)
# # 		print("	",bin)

# # 	elif not bin[-1]: #last item is false
# # 		print("	last item is False -> change to True")
# # 		bin[-1] = True
# # 		print("	",bin)
# # 	print("\n")

# # print(bin)

# '''
# 	my answer: 
# 		3 : [True, True, True]
# 	should be: 
# 		3 : [True, False]
# '''


# def resetBin(bin):
# 	print("		","in resetBin:")
# 	print("		","before",bin)
# 	# for i in range(1, len(bin)):
# 	# 	bin[i] = False
# 	# 	# print("		",bin)
# 	i = len(bin) - 1
# 	while i > 0:  # skip index 0
# 		bin[i] = False
# 		i -= 1
# 	bin.append(False)
# 	print("		","after",bin)
# 	return bin


# # def num_to_bin(num):
# # 	bin = 0
# # 	bin = [False] #represents 'num = 0'

# # 	for i in range(num-1):
# # 		print(f"i : {i}")
# # 		print(f"start: {bin}\n")
# # 		if all(bin):
# # 			''' reset to false '''
# # 			print("	all in bin is true, resetting")
# # 			# print(f"start: {bin}")
# # 			resetBin(bin)
# # 		else:
# # 			''' change last item to true '''
# # 			# for _i in range(len(bin), 0, -1):	
# # 			# 	print(_i)
# # 			if len(bin)==1:
# # 				print("	len(bin)==1 -> changin to True")
# # 				bin[0]=True
# # 				print(f"	{bin}")
# # 			else:
# # 				print("	find and change first false into true ")
# # 				i = len(bin) - 1  # start at the last index
# # 				while i >= 0:
# # 					if bin[i]==True:
# # 						print("		bin[i]==True -> change next into True")
# # 						print("		","before: ",bin)
# # 						bin[i+1]=True
# # 						print("		","after: ",bin)
# # 						break

# # 					i -= 1  # move backwards
# # 	print(f"\n\nend: {bin}\n")


# def num_to_bin(num):
# 	bin = 0
# 	bin = [False] #represents 'num = 0'

# 	for i in range(num-1):
# 		print(f"i : {i}")
# 		print(f"start: {bin}\n")
# 		if all(bin):
# 			''' reset to false '''
# 			print("	all in bin is true, resetting")
# 			# print(f"start: {bin}")
# 			resetBin(bin)
# 		else:
# 			''' change last item to true '''
# 			# for _i in range(len(bin), 0, -1):	
# 			# 	print(_i)
# 			if len(bin)==1:
# 				print("	len(bin)==1 -> changin to True")
# 				bin[0]=True
# 				print(f"	{bin}")
# 			# else:
# 			# 	print("	find and change first false into true ")
# 			# 	i = len(bin) - 1  # start at the last index
# 			# 	while i >= 0:
# 			# 		if bin[i]==True:
# 			# 			print("		bin[i]==True -> change next into True")
# 			# 			print("		","before: ",bin)
# 			# 			bin[i+1]=True
# 			# 			print("		","after: ",bin)
# 			# 			break
# 			# 		i -= 1  # move backwards
# 			else:
# 				print("	find last 'true' and move it up\n")
# 				# i = len(bin) - 1  # start at the last index
# 				# while i >= 0:
					
# 				# 	if bin[i]:
# 				# 		if bin[i+1]:
# 				# 			break
# 				# 		bin[i+1]=True
# 				# 		bin[i]=False
# 				# 		print("		","after: ",bin)
# 				# 		break
# 				# 	i-=1

# 				i=0
# 				while i < len(bin):
# 					print(f"	i:{i} -> bin[i]:{bin[i]}")
# 					# if bin[i] and not bin[i-1]:
# 					# 	print("		*found the last true")
# 					if bin[-1]==True:# and i==len(bin):
# 						print("		*last one it true")
# 						print("		*	move up")
# 						bin[-1]=False
# 						bin[-2]=True
# 						print(f"		{bin}")
# 						# i+=1
# 						break

# 					if bin[i]==True and not bin[i+1] and bin[i-1]==False and i!=0:
# 						print("		*has false infront and behind it")
# 						print("		*move up")
# 						print(f"		{bin[i]}, {bin[i+1]}, {bin[i-1]}")
# 						bin[-1]=False
# 						bin[-2]=True
# 						print(f"		{bin}")
# 						# i+=1
# 						break
# 					else:
# 						i+=1

# 					# if bin[-1]==True and i==0:
# 					# 	print("		*first one it true")
# 					# 	print("		*	move up")
# 					# 	print(f"		{bin}")
					
# 				# print(f"	{bin}")
# 				print("		found none, add change last false to true")
# 				bin[-1]=True
# 				print(f"	{bin}")



			








# 				# i = len(bin) - 1
# 				# while i >= 0:
# 				# 	print(f"		{i}:{bin[i]}")
# 				# 	print(f"		{i-1}:{bin[i-1]}")

# 				# 	if bin[i]==False:
# 				# 		i-=1
# 				# 	if bin[i]==True:
# 				# 		if i==0:
# 				# 			print("	add new")
# 				# 			''' add new'''
# 				# 			bin[-1] = True
# 				# 			print(f"	{bin[-1]}={True}")
# 				# 		if bin[i-1]==True:
# 				# 			print("	add new")
# 				# 			''' add new'''
# 				# 			bin[-1] = True
# 				# 			print(f"	{bin[-1]}={True}")
# 				# 		break
# 				# 		# else:
# 				# 		# 	print("error")

# 				# 	# if bin[i]==True:
# 				# 	# 	print(f"		found first true: {i}: {bin[i]} in {bin}")

# 				# 	# 	if bin[i-1] == True:
# 				# 	# 		''' add new true at the end '''
# 				# 	# 		print("		add new true")
# 				# 	# 		bin[-1] = True
# 				# 	# 		break

# 				# 	# 	elif bin[i-1] != True:
# 				# 	# 		''' move up'''
# 				# 	# 		print("		move up")
# 				# 	# 		bin[i], bin[i-1] = bin[i-1], bin[i]
# 				# 	# 		break
# 				# 	# else:
# 				# 	# 	''' check next'''
# 				# 	# 	i -= 1









# 				# # while i > 0 and bin[i] != True:
# 				# # 		''' check next'''
# 				# # 		i -= 1
				
# 				# # if i > 0 and bin[i] == True and bin[i-1] == True:
# 				# # 	''' add new true at the end '''
# 				# # 	print("		add new true")
# 				# # 	bin[-1] = True
# 				# # 	break

# 				# # elif i > 0 and bin[i] == True and bin[i-1] != True:
# 				# # 	''' move up'''
# 				# # 	print("		move up")
# 				# # 	bin[i], bin[i-1] = bin[i-1], bin[i]
# 				# # 	break

# 				# 	# if bin[i] == True and bin[i-1] == True:
# 				# 	# 	print("_______")
# 				# 	# 	print("		bin:", bin)
# 				# 	# 	print("		bin[i-1]:", bin[i-1])
# 				# 	# 	print("		bin[i]:", bin[i])
# 				# 	# 	print("		bin[-1]:", bin[-1])
# 				# 	# 	# print("		bin[1]:", bin[1])
# 				# 	# 	# print("		bin[i+1]:", bin[i+1])
# 				# 	# 	print("_______")
# 				# 	# 	bin[-1]=True
# 				# 	# 	break
					
# 				# 	# if i > 0:
# 				# 	# 	bin[i], bin[i-1] = bin[i-1], bin[i]
# 				# 	# 	break

# 				# print("	",bin)
# 				# if bin[-1]:

					
				
# 				''' 
# 				1. check if last item is true
# 				2. if so: move up
# 				3. if not (is false): change to true
# 				'''
			
# 	print(f"\n\nend: {bin}\n")



# def num_to_bin(num):

# 	''' Divide N by 2 '''
# 	N = num
# 	i=0
# 	r=[]
# 	q=10
# 	print("!!!NUM: ", num)
# 	# while N>0:
# 	# while i>=0:
# 	# print(i, ":", N, q)

# 	def criteria(N, q):
# 		if N<=0 and q<=0:
# 			return False
# 		return True

# 	rep=False
# 	while criteria(N, q):
# 		''' 
# 		Keep dividing the number by 2 untill its 0, adding all remainders to a list. 
# 		The binary is the remainders read backwards
# 		'''

# 		q = N/2
# 		_r=" "
# 		# print(f"start 	  no.{i}: N:[{N}],  q:[{q}], (+r:+{_r}) r:{r}")
# 		if q.is_integer():
# 			# print("	is int")
# 			r.append("0")
# 			_r="0"
# 			rep=False
# 			print(f"end 	  no.{i}: N:[{float(N)}],  q:[{q}], rep:{rep}, (+r:+{_r}) r:{r}")
# 			N=q
# 			# print(q)
# 		elif not q.is_integer():
# 			# print("is float")
# 			# subtract 1 and try again.
# 			rep=True
# 			_r="1"
# 			print(f"end 	  no.{i}: N:[{float(N)}],  q:[{q}], rep:{rep}, (+r:+{_r}) r:{r}")
# 			q = (N-1)/2
# 			N = q
# 			r.append("1")			
		
	
# 		i+=1
		

		

# 	print(f"\nfinal:		N:[{N}],  q:[{q}], (+r:+{_r}) r:{r}")
# 	print(r)
# 	r.reverse()
# 	return ''.join(r)


# # def num_to_bin(num):

# 	''' Divide N by 2 '''
# 	N = num
# 	i=0
# 	r=[]
# 	q=10


# 	def criteria(N, q):
# 		return False if N<=0 and q<=0 else True
# 		# return True if N>0 and q>0 else False

# 	while criteria(N, q):
# 		''' 
# 		Keep dividing the number by 2 untill its 0, adding all remainders to a list. 
# 		The binary is the remainders read backwards
# 		'''

# 		q = N/2
# 		if q.is_integer():
# 			r.append("0")
# 			N = q
# 		r.append("1")			
# 		N -= 1

# 	r.reverse()
# 	return ''.join(r)

# num = 11
# print("final: ",num_to_bin(num))
# # num_to_bin(num)
# '''
# IDEA:

# start with a list if false 
# [false]
# change last item to true:
# [true]
# if all items are true, append a false
# [true, false]
# .
# .
# .
# .
# [true, true, false, false, false]
# change last item to true:
# [true, true, false, false, true]
# if bin[-2]!=bin[-1] -> switch places. 
# [true, true, false, true, false]
# [true, true, true, false, false]
# if bin[-n]==bin[-1],(aka, bin[-1] has reached its destination [true, true, true, false, false] ) next iter. 
# if bin[-2]==bin[-1],(aka, all items are true [true, true, true, true, true]), append a false

# this continues until, the end of the loop. 



# '''



# 1. experimental
def bin_to_num(bin, i=0):
    bin = str(bin)
    return 0 if i == len(bin) else int(bin[i]) * (2 ** (len(bin) - 1 - i)) + bin_to_num(bin, i + 1)

# 2. 
def bin_to_num(bin, i=0, num=0):
	''' using while '''
	bin = str(bin)
	lenB = len(bin)-1
	print("num += int(bin[i])*(2**lenB)")
	step=1
	while i<len(bin):
		# print(f"bin[{i}] : {bin[i]}")
		num += int(bin[i])*(2**lenB)

		print(f"step: {step} | {bin[i]}*(2^{lenB}) = {int(bin[i])*(2**lenB)} 				-> += {num}")
		lenB -= 1 
		i += 1
		step+=1

	return num



def bin_to_num(bin, i=0, num=0):
	''' using while '''
	bin = str(bin)
	lenB = len(bin)-1
	lenB=93
	print("num += int(bin[i])*(2**lenB)")
	step=1
	# while i<len(bin):
	i=len(bin)
	_i = 0 #normal direction.
	# while i > 0:
	# 	print(i)
	# 	print(_i)

	# 	# print(f"bin[{i}] : {bin[i]}")
	# 	num += int(bin[_i])*(2**i)

	# 	print(f"step: {step} | {bin[_i]}*(2^{i}) = {int(bin[_i])*(2**i)} 				-> += {num}")
	# 	lenB -= 1 
	# 	i -= 1
	# 	_i+=1
	# 	step+=1

	# return num
	lenB=len(bin)-1
	lenB=93
	print("****",len(bin))
	for b in bin:
		num += int(b)*(2**lenB)
		print(f"step: {step} | {b}*(2^{lenB}) = {int(b)*(2**lenB)} 				-> += {num}")
		lenB -= 1
	


# # 3.
# def bin_to_num(bin):
# 	''' using for '''
# 	bin = str(bin); lenB = len(bin)-1
# 	return sum(int(b)*(2**(lenB-i)) for i, b in enumerate(bin))
# # 4.
# def bin_to_num(bin):
# 	bin = str(bin)
# 	return sum(int(bin[i]) * (2 ** (len(bin) - 1 - i)) for i in range(len(bin)))


def test(bin):
	#39614081257132168796771975168
	# b=1
	# n=95
	b=int(bin[-1])
	n=len(bin)
	sum=b*(2**n)
	sum=1*(2**94)
	print(sum)
	print(len(bin))

bin = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"
x = bin_to_num(bin)
# x = test(bin)
# print(x)


'''						
num += int(bin[i])*(2**lenB)
19807040628566084398385987584                   = 1*(2^94)              -> += 19807040628566084398385987584
0                       						= 0*(2^93)              -> += 19807040628566084398385987584
4951760157141521099596496896                    = 1*(2^92)              -> += 24758800785707605497982484480
0                       						= 0*(2^91)              -> += 24758800785707605497982484480
0                       						= 0*(2^90)              -> += 24758800785707605497982484480
0                       						= 0*(2^89)              -> += 24758800785707605497982484480
0                       						= 0*(2^88)              -> += 24758800785707605497982484480
0                       						= 0*(2^87)              -> += 24758800785707605497982484480
77371252455336267181195264                      = 1*(2^86)              -> += 24836172038162941765163679744
0                       						= 0*(2^85)              -> += 24836172038162941765163679744
0                       						= 0*(2^84)              -> += 24836172038162941765163679744
9671406556917033397649408                       = 1*(2^83)              -> += 24845843444719858798561329152
0                       						= 0*(2^82)              -> += 24845843444719858798561329152
0                       						= 0*(2^81)              -> += 24845843444719858798561329152
1208925819614629174706176                       = 1*(2^80)              -> += 24847052370539473427736035328
604462909807314587353088						= 1*(2^79)              -> += 24847656833449280742323388416
0                       						= 0*(2^78)              -> += 24847656833449280742323388416
151115727451828646838272						= 1*(2^77)              -> += 24847807949176732570970226688
75557863725914323419136 						= 1*(2^76)              -> += 24847883507040458485293645824
0                       						= 0*(2^75)              -> += 24847883507040458485293645824
0                       						= 0*(2^74)              -> += 24847883507040458485293645824
9444732965739290427392  						= 1*(2^73)              -> += 24847892951773424224584073216
0                       						= 0*(2^72)              -> += 24847892951773424224584073216
0                       						= 0*(2^71)              -> += 24847892951773424224584073216
0                       						= 0*(2^70)              -> += 24847892951773424224584073216
0                       						= 0*(2^69)              -> += 24847892951773424224584073216
0                       						= 0*(2^68)              -> += 24847892951773424224584073216
147573952589676412928   						= 1*(2^67)              -> += 24847893099347376814260486144
0                       						= 0*(2^66)              -> += 24847893099347376814260486144
36893488147419103232    						= 1*(2^65)              -> += 24847893136240864961679589376
0                       						= 0*(2^64)              -> += 24847893136240864961679589376
9223372036854775808     						= 1*(2^63)              -> += 24847893145464236998534365184
4611686018427387904     						= 1*(2^62)              -> += 24847893150075923016961753088
2305843009213693952     						= 1*(2^61)              -> += 24847893152381766026175447040
1152921504606846976     						= 1*(2^60)              -> += 24847893153534687530782294016
0                       						= 0*(2^59)              -> += 24847893153534687530782294016
288230376151711744      						= 1*(2^58)              -> += 24847893153822917906934005760
144115188075855872      						= 1*(2^57)              -> += 24847893153967033095009861632
0                       						= 0*(2^56)              -> += 24847893153967033095009861632
36028797018963968       						= 1*(2^55)              -> += 24847893154003061892028825600
18014398509481984       						= 1*(2^54)              -> += 24847893154021076290538307584
0                       						= 0*(2^53)              -> += 24847893154021076290538307584
0                       						= 0*(2^52)              -> += 24847893154021076290538307584
2251799813685248        						= 1*(2^51)              -> += 24847893154023328090351992832
1125899906842624        						= 1*(2^50)              -> += 24847893154024453990258835456
0                       						= 0*(2^49)              -> += 24847893154024453990258835456
281474976710656         						= 1*(2^48)              -> += 24847893154024735465235546112
140737488355328         						= 1*(2^47)              -> += 24847893154024876202723901440
70368744177664          						= 1*(2^46)              -> += 24847893154024946571468079104
0                       						= 0*(2^45)              -> += 24847893154024946571468079104
17592186044416          						= 1*(2^44)              -> += 24847893154024964163654123520
8796093022208           						= 1*(2^43)              -> += 24847893154024972959747145728
4398046511104           						= 1*(2^42)              -> += 24847893154024977357793656832
2199023255552           						= 1*(2^41)              -> += 24847893154024979556816912384
1099511627776           						= 1*(2^40)              -> += 24847893154024980656328540160
549755813888            						= 1*(2^39)              -> += 24847893154024981206084354048
274877906944            						= 1*(2^38)              -> += 24847893154024981480962260992
137438953472            						= 1*(2^37)              -> += 24847893154024981618401214464
68719476736             						= 1*(2^36)              -> += 24847893154024981687120691200
34359738368             						= 1*(2^35)              -> += 24847893154024981721480429568
0                       						= 0*(2^34)              -> += 24847893154024981721480429568
8589934592              						= 1*(2^33)              -> += 24847893154024981730070364160
0                       						= 0*(2^32)              -> += 24847893154024981730070364160
0                       						= 0*(2^31)              -> += 24847893154024981730070364160
0                       						= 0*(2^30)              -> += 24847893154024981730070364160
0                       						= 0*(2^29)              -> += 24847893154024981730070364160
0                       						= 0*(2^28)              -> += 24847893154024981730070364160
0                       						= 0*(2^27)              -> += 24847893154024981730070364160
67108864                						= 1*(2^26)              -> += 24847893154024981730137473024
0                       						= 0*(2^25)              -> += 24847893154024981730137473024
16777216                						= 1*(2^24)              -> += 24847893154024981730154250240
8388608                 						= 1*(2^23)              -> += 24847893154024981730162638848
4194304                 						= 1*(2^22)              -> += 24847893154024981730166833152
2097152                 						= 1*(2^21)              -> += 24847893154024981730168930304
0                       						= 0*(2^20)              -> += 24847893154024981730168930304
0                       						= 0*(2^19)              -> += 24847893154024981730168930304
262144                  						= 1*(2^18)              -> += 24847893154024981730169192448
131072                  						= 1*(2^17)              -> += 24847893154024981730169323520
65536                   						= 1*(2^16)              -> += 24847893154024981730169389056
0                       						= 0*(2^15)              -> += 24847893154024981730169389056
0                       						= 0*(2^14)              -> += 24847893154024981730169389056
0                       						= 0*(2^13)              -> += 24847893154024981730169389056
4096                    						= 1*(2^12)              -> += 24847893154024981730169393152
2048                    						= 1*(2^11)              -> += 24847893154024981730169395200
1024                    						= 1*(2^10)              -> += 24847893154024981730169396224
512                     						= 1*(2^9)               -> += 24847893154024981730169396736
256                     						= 1*(2^8)               -> += 24847893154024981730169396992
0                       						= 0*(2^7)               -> += 24847893154024981730169396992
0                       						= 0*(2^6)               -> += 24847893154024981730169396992
0                       						= 0*(2^5)               -> += 24847893154024981730169396992
0                       						= 0*(2^4)               -> += 24847893154024981730169396992
8                       						= 1*(2^3)               -> += 24847893154024981730169397000
4                       						= 1*(2^2)               -> += 24847893154024981730169397004
0                       						= 0*(2^1)               -> += 24847893154024981730169397004
1                       						= 1*(2^0)               -> += 24847893154024981730169397005
____________________________________________________________________________________________________________
																		   == 24847893154024981730169397005


'''
# print(f"\n\n {int(110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000)}")
a = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"
b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"
c = "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000"

print(int(a, 2))  # 8830819185367747134418738845
print(int(b, 2))  # 188661059686540054518485900195
print(int(c, 2))  # 129865686257123922436514188544

# bit × 2^position

# "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"  		= 8830819185367747134418738845
# "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011" 	= 188661059686540054518485900195
# "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000"		= 129865686257123922436514188544

# print(8830819185367747134418738845+188661059686540054518485900195)

# 197491878871907801652904639æ040

# 24847893154024981730169397005
# 8830819185367747134418738845