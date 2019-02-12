def fib(n):
	if n < 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)
memo={}
def fib(n, memo):
	if n in memo:
		return memo[n]
	if n < 2:
		memo[n] = 1
	else:
		memo[n] = fib(n-1, memo)+fib(n-2, memo)
	return memo[n]
