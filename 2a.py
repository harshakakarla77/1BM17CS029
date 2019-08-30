def check1(a,k,n):
    beg=0
    end=n-1
    flag=0
    while(beg<=end):
        mid=(beg+end)//2
        if(a[mid]==k):
            flag=1
            break
        elif(a[mid]<k):
            beg=mid+1
        else:
            end=mid-1

    
    if(flag==1):
        return (mid+1)
    else:
        return -1


list1=[]
n=int(input("No of elements:"))
print("Enter the elements:")
for i in range(n):
    a=int(input())
    list1.append(a)

k=int(input("Element to search:"))
x=check1(list1,k,n)
if(x!=-1):
    print("Element found at position:",x)
else:
    print("Element not found")



