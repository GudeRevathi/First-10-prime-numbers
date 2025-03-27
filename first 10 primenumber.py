def prime(n1,n2):
    c=0
    if n1<n2:
        for i in range(n1,n2):
            for j in range(2,i):
                if i%j==0:
            
                    break
            else:
                print(i)
                c=c+1
            if c==10:
                break
n1=int(input("enter 1st number:"))
n2=int(input("enter 2nd number"))
prime(n1,n2)