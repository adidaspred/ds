#complete graph check(adjacency matrix)
n=int(input("give the total no. of nodes: "))
p=eval(input("give the ordered pair of all the edges: "))
b=0
m=[]
l=[]
for i in range(n):
   m.append([])
   for j in range(n):
       m[i].append(0)
      
for i in p:
    j=i[0]
    k=i[1]
    m[k][j]=1
    m[j][k]=1

print("the adjacency matrix is: ")
for i in m:
    print(i)
for i in range(n):
    for j in range(n):
        if(i==j and m[i][j]==1) or (i!=j and m[i][j]==0) :
            print("the given graph is not a complete graph")
            b=1
            break
    if b==1:
        break   
else:
    print("yes the given graph is a complete graph")
