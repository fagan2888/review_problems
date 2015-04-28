def find_missing(seq):
	i = 0
	exp = '0'
	while i < len(seq):
		if seq[i][-1] != exp:
			return i
		if exp == '1': 
			exp = '0'
		else:
			exp = '1'
		i += 1

seq = ['0','1','10','11','100','101','111','1000','1001','1010','1011','1100','1101','1110','1111','10000']

print find_missing(seq)



