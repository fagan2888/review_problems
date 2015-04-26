
def unique(s):
	for i in range(len(s)):
		if s[i] in s[:i] or s[i] in s[i+1:]:
			return False
	return True

s = 'asdf'
t = 'asdaf'

print unique(s)
print unique(t)

print t[:2]
print t[2]
print t[3:]
print t[-1]
print t[:-1]

