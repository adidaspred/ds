#in edges and out edges of a given graph
n=int(input("give the total number of nodes"))
l=[]
m=[]
l1=[]
l3=[]
for i in range(n):
    l1.append(i)
for i in range(n):
    m.append([])
    print("give the list of elements associated with",i,": ")
    a=eval(input())
    for j in a:
        m[i].append(j)

for i in range(n):
    count=0
    for j in range(n):
        if j==i:
            pass
        else:
            
            for k in m[j]:
                if k==i:
                    count+=1
    l.append(count)
for i in range(n):
    l3.append(len(m[i]))
        
for i in range(n):
    print("the in-degree of ",i," is ",l[i])
for i in range(n):
    print("the out-degree of ",i," is ",l3[i])
