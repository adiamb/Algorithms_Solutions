def SubSequences(Str, n):
	temp=set()
	for e in range(n):
		temp.add(Str[e])
		for i in range(e+1, n):
			print Str[e]
			j = i
			out = Str[e]
			while j < n:
				out += Str[j]
				j += 1
				temp.add(out) 
	return temp
  
Str='orange'
n = len(Str)
SubSequences(Str, n)
