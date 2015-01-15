import itertools, math
def getDivisors(n):
	return itertools.chain((i for i in range(1, int(n/2+1)) if n%i==0),[n])
def pow(n):
	return n**2
def sigma2(n):
	return sum(map(pow, getDivisors(n)))
	pass
def SIGMA2(n):
	return sum((sigma2(i) for i in range(1,n+1)))
if __name__ == "__main__":
	print(SIGMA2(10**15)%10**9)
