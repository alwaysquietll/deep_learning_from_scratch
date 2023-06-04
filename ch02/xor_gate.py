import and_gate
import or_gate
import nand_gate

def XOR(x1, x2):
    s1 = nand_gate.NAND(x1, x2)
    s2 = or_gate.OR(x1, x2)
    y = and_gate.AND(s1, s2)
    return y

if __name__ == '__main__':
    for x in [(0,0),(0,1),(1,0),(1,1)]:
        print("{} -> {}".format(str(x),XOR(x[0],x[1])))