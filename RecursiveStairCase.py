'''Problem Statement :Davis has a number of staircases in his house and he likes to climb each staircase 1,2 or 3  steps at a time. Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.'''

def stepPerms(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        result =1
    elif n ==2:
        result =2
    else:
        result=stepPerms(n-1, memo)+stepPerms(n-2, memo)+stepPerms(n-3, memo)
        memo[n] = result
    return result
