arr1=[]
arr2=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(n):
    a=int(input(f'Enter {i+1} element:' ))
    arr1.append(a)
print(arr1)
for i in arr1:
    if(i%2==0):
        arr2.append(i)
for i in arr2:
        print(i)
    
    
