#' find common substring between two strings 
# Recursive solution
def abbr(a, b, n, m):
	if n ==0 or m ==0:
		result =0
	elif a[n-1] == b[m-1]:
		result = 1+abbr(a, b, n-1, m-1)
	else:
		temp1 = abbr(a, b, n-1, m)
		temp2 = abbr(a, b, n, m-1)
		result = max(temp1, temp2)
	return result

a,b = 'abcde'.lower(),'afde'.lower()
n,m= len(a), len(b)
abbr(a, b, n, m)
 
 # Recursive solution with memoization
 def abbr(a, b, n, m, memo):
	Key = str(n)+str(m)
	if Key in memo:
		return memo[Key]
	if n == 0 or m ==0:
		result= 0
	elif a[n-1] == b[m-1]:
		result= abbr(a, b, n-1, m-1, memo)+1
	else:
		temp1 = abbr(a, b, n-1, m, memo)
		temp2 = abbr(a, b, n, m-1, memo)
		result = max(temp1, temp2)
	memo[Key] = result
	return result
 
a,b = 'abcde'.lower(),'afde'.lower()
n,m= len(a), len(b)
memo ={}
abbr(a, b, n, m, memo)
