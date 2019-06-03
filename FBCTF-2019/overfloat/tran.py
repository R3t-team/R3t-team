import math
def tran(s):
	base=(bin(s)[2:]).rjust(32,"0")
	sig=base[:1]
	exp=base[1:9]
	man=base[9:32]
	'''
	if exp[0]=='1':
		exp=-int("0b"+exp[1:],2)+127
	else:
		exp=int("0b"+exp[1:],2)
	'''
	exp=int("0b"+exp,2)
	if exp > 127:
		exp=exp-127
		sum=0
		idx=0
		for x in man:
			idx+=1
			if x=="1":
				sum+=math.pow(2.0,-idx)
		sum+=1
		#print sum
		res=sum*pow(2.0,exp)
		if sig=="1":
			return "-"+str(res)
		else:
			return str(res)
	else:
		exp=exp-126
		sum=0
		idx=0
		for x in man:
			idx+=1
			if x=="1":
				sum+=math.pow(2.0,-idx)
		#print sum
		res=sum*pow(2.0,exp)
		if sig=="1":
			return "-"+str(res)
		else:
			return str(res)
	
#print tran(0x7fff)
