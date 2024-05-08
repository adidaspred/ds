#solution to equation
d=int(input("give the degree of the polynomial "))
n=int(input("give the value of n with which the solution is to be computed "))
l=[]
sum=0
for i in range(d+1):
    print("for the degree ",i)
    a=int(input("give value of the term "))
    l.append(a)
print("the terms of the fucntion f(n) are:")
for i in range(d+1):
    print(str(l[i])+"n^"+str(i),end=" ")
for i in range(d+1):
    sum+=(l[i])*(n**i)
print()
print("the solution of the function f(n) for n=",n,"will be: ",sum)

