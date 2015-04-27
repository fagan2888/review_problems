def bin_dec(val):
	print val
	if val >= 1 or val <= 0:
		return "invalid input"
	if val == 0 or val == 1: 
		return val
	bin_val = 0
	output = []
	current_place = .5
	while bin_val <> val and len(output) < 32:
		if (bin_val + current_place) < val:
			output.append('1')
			bin_val = bin_val + current_place
		elif (bin_val + current_place) > val:
			output.append('0')
		else:
			output.append('1')
			return '0.' +''.join(output)
		current_place = current_place * .5
	return "ERROR"

print bin_dec(0.7509765625)
