class Relation:
    def __init__(self, matrix):
        self.matrix = matrix

    def is_reflexive(self):
        n = len(self.matrix)
        for i in range(n):
            if self.matrix[i][i] != 1:
                return False
                break
        else:
            return True

    def is_symmetric(self):
        n1 = 0
        n = len(self.matrix)
        m = len(self.matrix[0])
        for i in range(n):
            if n1 == 1:
                break
            for j in range(m):
                try:
                    if self.matrix[i][j] != self.matrix[j][i]:
                        n1 = 1
                        break
                except:
                    continue
        if n1 == 1:
            return False
        else:
            return True

    def is_transitive(self):
        n1 = 0
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] == 1:
                    for k in range(n):
                        if self.matrix[j][k] == 1 and self.matrix[i][k] != 1:
                            n1 = 1
                            break
                    if n1 == 1:
                        break
            if n1 == 1:
                break
        if n1 == 1:
            return False
        else:
            return True

    def is_antisymmetric(self):
        n1 = 0
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if ((i != j) and self.matrix[i][j] == 1 and self.matrix[i][j] == self.matrix[j][i]):
                    n1 = 1
                    break
            if n1 == 1:
                break
        if n1 == 1:
            return False
        else:
            return True

    def is_equivalence(self):
        if (self.is_reflexive() != False and self.is_symmetric() != False and self.is_transitive() != False):
            return True
        else:
            return False

    def is_partialorder(self):
        if (self.is_reflexive() != False and self.is_antisymmetric() != False and self.is_transitive() != False):
            return True
        else:
            False


rel = eval(input("ENTER a relation "))
dom = eval(input("ENTER the domain "))
cdom = eval(input("ENTER the co-domain "))
dom.sort()
cdom.sort()
matrix = []
for i in range(len(dom)):
    matrix.append([])
for i in range(len(dom)):
    for j in range(len(cdom)):
        matrix[i].append(0)
for i in rel:
    matrix[dom.index(i[0])][cdom.index(i[1])] = 1
relation = Relation(matrix)
print("the relation matrix of the following is:")
print(matrix)
choice = "y"
while choice.lower() == "y":
    ch = int(input('''R E L A T I O N   O P E R A T I O N   M E N U :
press 1 to check if the relation is reflexive or not
press 2 to check if the relation is symmetric or not
press 3 to check if the relation is transitive or not
press 4 to check if the relation is antisymmetric or not
press 5 to check if the relation is equivalence or not
press 6 to check if the relation is partial order or not
enter the FUNCTION : '''))
    if ch == 1:
        if relation.is_reflexive() == False:
            print("not reflexive")
        else:
            print("reflexive")
    elif ch == 2:
        if relation.is_symmetric() == False:
            print("not symmetric")
        else:
            print("symmetric")

    elif ch == 3:
        if relation.is_transitive() == False:
            print("not transitive")
        else:
            print("transitive")
    elif ch == 4:
        if relation.is_antisymmetric() == False:
            print("not antisymmetric")
        else:
            print("antisymmetric")
    elif ch == 5:
        if relation.is_equivalence() == True:
            print("equivalence")
        else:
            print("not equivalence")
    elif ch == 6:
        if relation.is_partialorder == True:
            print("partial order")
        else:
            print("not partial order")
    else:
        print("invalid operation")
    choice = str(input("PRESS Y TO CONTINUE WITH THE PROGRAM"))





