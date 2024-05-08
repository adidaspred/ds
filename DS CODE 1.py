class SET:

    def __init__(self, Set, univ):

        self.Set = Set

        self.univ = univ



    def ismember(self, a):

        if a in self.Set:

            return True

        else:

            return False



    def __str__(self):

        return str(self.Set)



    def powerset(self):

        import math

        l=list(self.Set)

        ps=[{}]

        for i in range(1,pow(2,len(l))):

            a=set()

            for j in range(0,len(l)):

                if i&1==1:

                    a.add(l[j])

                i=i>>1

            ps.append(a)

        return ps



    def subset(self, seT):

        for i in seT:

            if i not in self.Set:

                return "not a subset"

                break

        else:

            return "subset"



    def union(self, other_set):
         return set(self.Set).union(other_set.Set)
   

    

    def intersection(self, obj1, obj2):
        s = {'emp'}
        obj1 = list(obj1)  # Convert obj1 to a list
        for i in obj1:
            if i in obj2 and i in obj1:
                s.add(i)
        s.remove('emp')
        return s



    



    def complement(self):

        f = []

        for i in self.univ:

            if i not in self.Set:

                f.append(i)



        return f



    def difference(self, set1):
        s = list(self.Set)  # Convert to list
        for i in s:
            if i in set1:
                s.remove(i)
        return s


    def symmetric_difference(self, set1):
        s1 = set(self.Set).copy()
        s = set(self.Set).union(set1)
        for i in s1:
            if i in set1 and i in self.Set:
                s.remove(i)
        return s



    def cartesian_product(self, set1):

        cp = {0}

        for i in self.Set:

            for j in set1:

                cp.add((i, j))

        cp.remove(0)

        return cp

choice = 'y'
print("S E T   O P E R A T I O N   M E N U")
a = eval(input("Enter a set on which operations shall be performed "))

u = eval(input("enter the universal set "))

s = SET(a, u)

while choice.lower() == "y":
    ch = int(input('''S E T   O P E R A T I O N   M E N U")
1.to check if the a value is a member or not
2.for powerset
3.subset
4.union
5.intersection
6.compliment
7.difference
8.symmetrc difference
9.cartisian product'''))

    while choice.upper() == 'Y':

        b = int(input("ENTER the function to be performed").split(',')[0])
        if b == 1:

            c = int(input("ENTER the number to be checked"))

            print(s.ismember(c))

        elif b == 2:

            print(s.powerset())

        elif b == 3:

            set1 = eval(input("ENTER the subset to be verified"))

            print(s.subset(set1))

        elif b == 4:
            set1 = eval(input("ENTER the set with which the union is to be found"))
            set1_obj = SET(set1, u)
            print(s.union(set1_obj))
        elif b == 5:
            set1 = eval(input("ENTER the set with which the intersection is to be found"))
            set2 = eval(input("ENTER the set with which the intersection is to be found"))
            print(s.intersection(set1, set2))

        elif b == 6:

            set1 = eval(input("ENTER the set with which the symmetric difference is to be found"))

            print(s.symmetric_difference(set1))

        elif b == 7:

            set1 = eval(input("ENTER the set with which the difference is to be found"))

            print(s.difference(set1))

        elif b == 8:

            print(s.complement())

        elif b == 9:

            set1 = eval(input("ENTER the set with which the cartesian product is to be found"))

            print(s.cartesian_product(set1))



        else:

            print("operation INVALID")

        choice = str(input("TO CONTINUE WITH THE PROGRAM PRESS Y"))




