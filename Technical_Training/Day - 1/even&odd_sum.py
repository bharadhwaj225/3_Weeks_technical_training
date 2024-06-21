def even_odd_sum(i,a1,b1):
    if(i==len(a)):
        return a1,b1
    if(a[i]%2==0):
        a1=a1+a[i]
    if(b[i]%2!=0):
        b1=b1+b[i]
    return even_odd_sum(i+1,a1,b1)

a = [3, 8, 5, 4, 3]
b = [5, 0, 9, 3, 2]
x,y=even_odd_sum(0,0,0)
print(x,y)