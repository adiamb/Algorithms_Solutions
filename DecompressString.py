def decompress(Str, Ind):
"""Take a nested string in the format '2[ab2[c]d]' and expand it into 'abccdabccd'"""
	i = Ind
	Sub = ''
	CurStr = ''
	while i < len(Str): ## base case exit 
		if Str[i].isdigit(): ### add the digit
			Sub += Str[i]
		elif Str[i].isalpha(): 
			CurStr += Str[i]
		elif Str[i] == ']':
			return CurStr, i
		else:## start recursion here
			NCurStr, i = decompress(Str, i+1)
			CurStr += NCurStr*int(Sub)
			Sub = ''
		i += 1
	return CurStr
