def c(s):

	st=[];
	l='';
	ct=1;

	for e in s:
		if e==l:
			ct+=1
		else:
			st.append(l + str(ct))
			ct = 1
		l = e	
	st.append(''.join([l, str(ct)]))

	f = ''.join(st)
	if len(f) < len(s):
		return f
	return s

s = 'aaabbbcccddddd'

print c(s)	

