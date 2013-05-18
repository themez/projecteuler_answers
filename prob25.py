def main():
	max = 10**999
	m1,m2=1,1
	i=2
	while(m2<max):
		m1,m2 = m2, m1+m2
		i+=1
	m = (m2,i)
	print(i)
if __name__ == "__main__":
	main()
