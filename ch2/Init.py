def And(x1,x2):
    [w1,w2] = [1]*2
    b = -1
    temp = w1*x1 + w2*x2 + b
    if temp > 0:
        return 1
    else:
        return 0
def Nand(x1,x2):
    [w1,w2] = [-1]*2
    b = 1.5
    temp = w1*x1 + w2*x2 + b
    if temp > 0:
        return 1
    else:
        return 0
def Or(x1,x2):
    [w1,w2] = [1]*2
    b = -0.5
    temp = w1*x1 + w2*x2 + b
    if temp > 0:
        return 1
    else:
        return 0
def xor(x1,x2):
    s1 = Nand(x1,x2)
    s2 = Or(x1,x2)
    s3 = And(s1,s2)
    if s3 > 0:
        return 1
    else:
        return 0
ans = [And(1,1),And(1,0),And(0,1),And(0,0)]
print(ans)
ans = [Nand(1,1),Nand(1,0),Nand(0,1),Nand(0,0)]
print(ans)
ans = [Or(1,1),Or(1,0),Or(0,1),Or(0,0)]
print(ans)
ans = [xor(1,1),xor(1,0),xor(0,1),xor(0,0)]
print(ans)