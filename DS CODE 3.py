#Permutation
def perm1(l):
    if len(l)==0:
        return [] 
    elif len(l)==1:
        return [l]
    else:
        l1=[]
        for i in range(len(l)):
            x=l[i]
            x1=l[:i]+l[i+1:]
            for j in perm1(x1):
                l1.append(x+''.join(j))
        return l1
def perm2(x):
        final = [[]]
        l = len(x)
        groups = [list(x)] * l
        
        for i in groups:
            final = [x+[y] for x in final for y in i]
        print("for total permutations ",len(final)) 
        for k in final:
            print(''.join(k),end=',')
a=str(input("give a sequence of elements: "))
l=list(a)
choice='y'
while choice.lower()=='y':
    ch=int(input('''for permutation with repetition press 1
for permutation without repetition press 2\n'''))
    if ch==2:
        print("for total permutations ",len(perm1(l)))
        for i in perm1(l):
            print(i,end=',')
    elif ch==1:
        perm2(l)
    else:
        print("invalid operation")
    print()
    choice=str(input("do u wanna continue?(y/n) "))

else:
    print("thanks for using the program!")


    

