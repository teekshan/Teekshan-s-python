def bubblesort(list1):
    for i in range(len(list1)-1,0,-1):
        for j in range(i):
            if list1[j]>list1[j+1]:
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    print(list1)
list1=[1,390,780,88,99,9,54,8]
bubblesort(list1)
