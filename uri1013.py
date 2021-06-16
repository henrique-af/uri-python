A, B, C = input().split(" ")
A = int(A)
B = int(B)
C = int(C)
TesteMaior = (A + B + abs(A - B))/2
print("{:.0f} eh o maior".format(((TesteMaior + C + abs(TesteMaior - C))/2)))
