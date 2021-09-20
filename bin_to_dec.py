def conversion():
    bin_or_dec= int(input("enter 1 for converting binary into decimal and enter 0 for converting decimal into binary: "))
    for i in range(1,100):
        if (bin_or_dec==1):
            print("will convert binary into decimal: ")
            n=input("enter no.: ")
            decimal = int(n,2)
            print(f' decimal no. is: {decimal}')
            break
        elif bin_or_dec==0:
            print("will convert decimal into binary")
            n2=int(input("enter no.: "))
            binary = bin(n2)
            print(f'binary no. is : {binary}')
            break
        else:
            print("wrong choice return to the loop")
            continue
						
						
conversion()
