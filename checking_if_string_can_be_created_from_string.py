n = int(input())
str1 = input(" ")
for i in range(n+1):
    message = input(" ")
    for t in str1.split():
        for m in message.split():
            if m in t:
                print("yes")
                break
print("no")
