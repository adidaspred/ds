#perfect graph usign adjacent list
import copy as c
n=int(input("give the total no. of nodes: "))
l=[]
l1=[]
for i in range(n):
    l1.append(i)
for i in range(n):
    l.append([])
    print("give the list of elements associated with",i,": ")
    a=eval(input())
    for j in a:
        l[i].append(j)
print("the following graph has the adjacency list:")
print(l)


for i in range(len(l)):
    l2=c.copy(l1)
    if ((i in l[i]) or (l2.remove(i)!=l[i].sort())):
        print("the given graph isn't a perfect graph ")
        break
else:
    print("the given graph is a perfect graph")    
