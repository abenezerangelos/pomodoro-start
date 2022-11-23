array = [1,2,3,4,5]
array.index(2)

dicter={"play":1,"set":2,"love":3}
print(dicter.items())
newarray=array
i=0
j=0
while j<len(array):
    n=array[i]
    m=newarray[j]
    if (n+m)%5==0:
        print(n,m)
        break
    elif i==len(array)-1:
        j+=1
    i+=1
for i in range(7):
    if i not in array:
        print(i)

