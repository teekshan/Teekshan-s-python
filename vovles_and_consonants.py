#to finding the number of vovels and consonants in a string

def counting(str):
    count=0
    count2=0
    vovels =set('aeiouAEIOU')
    consonants= set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    for alphabet in str:
        if alphabet in vovels:
            count +=1
        elif alphabet in consonants:
            count2 +=1
    print(f"No. of vovels: {count} and no. of consonants= {count2}")

counting("hello this is my world")
            
