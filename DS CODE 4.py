#linear combinations

n=int(input("give total number of terms "))
c=int(input("provide the sum "))
l=[]
for i in range(0,c+1):
    l.append(str(i))
def perm2(x,n):
        final = [[]]
        l = len(x)
        groups = [list(x)] * l
        for i in groups:
            if len(final[0])>n:
                 break
            else:
                final = [x+[y] for x in final for y in i] 
        for k in final:
            for m in range(len(k)-n):
                 k.pop()
        s={"none"}
        for k in final:
            s.add(str(''.join(k)))
        s.remove("none")
        return (s)

def dig_sum(i):
    l=[]
    for k in i:
        l.append(int(k))
    return sum(l)       
s=perm2(''.join(l),n)
print('''The following are the possible values of a1,a2,a3,...,an
for the linear equation a1*x1+ a2*x2+ a3*x3+...+ an*xn = ''',c)
for i in s:
     if dig_sum(i)==c:
          print(i,end=',') 
