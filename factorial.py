def fac(n):
        if(n==0):
            return 1
        elif(n==1):
            return 1
        else:
            return n * fac(n-1)

def  turn():
	t = int(input("how many factorilas you want to get: "))
	while(t):
			t=t-1
			for i in range(1,100):
					n = int(input("number you want to get factorlia of: "))
					if (n>=0):
							p = fac(n)
							print(p)
							break
					else:
							print("enter a positive interger")
							continue
						
turn()
