class MorseTree:

    info = None
    left = None
    right = None

    def __init__(self,info=None,left=None,right=None):
        self.info = info
        self.left = left
        self.right = right


class MorseDecoder:

    root = None
    def __init__(self):
        root = MorseTree("start")
        A = MorseTree("A")
        B = MorseTree("B")
        C = MorseTree("C")
        D = MorseTree("D")
        E = MorseTree("E")
        F = MorseTree("F")
        G = MorseTree("G")
        H = MorseTree("H")
        I = MorseTree("I")
        J = MorseTree("J")
        K = MorseTree("K")
        L = MorseTree("L")
        M = MorseTree("M")
        N = MorseTree("N")
        O = MorseTree("O")
        P = MorseTree("P")
        Q = MorseTree("Q")
        R = MorseTree("R")
        S = MorseTree("S")
        T = MorseTree("T")
        U = MorseTree("U")
        V = MorseTree("V")
        W = MorseTree("W")
        X = MorseTree("X")
        Y = MorseTree("Y")
        Z = MorseTree("Z")

        one = MorseTree("1")
        two = MorseTree("2")
        three = MorseTree("3")
        four = MorseTree("4")
        five = MorseTree("5")
        six = MorseTree("6")
        seven = MorseTree("7")
        eight = MorseTree("8")
        nine = MorseTree("9")
        zero = MorseTree("10")

        ques = MorseTree("ques")
        dot = MorseTree("dot")
        dash = MorseTree("dash")

        root.left,root.right = T,E
        T.left,T.right = M,N
        E.left,E.right = A,I
        M.left,M.right = O,G
        N.left,N.right = K,D
        A.left,A.right = W,R
        I.left,I.right = U,S
        O.left,O.right = ques,dot
        G.left,G.right = Q,Z
        K.left,K.right = Y,C
        D.left,D.right = X,B
        W.left,W.right = J,P
        R.left,R.right = None,L
        U.left,U.right = dash,F
        S.left,S.right = V,H
        ques.left,ques.right = zero,nine
        dot.left,dot.right = None,eight
        Z.left,Z.right = None,seven
        B.left,B.right = None,six
        J.left,J.right = one,None
        dash.left,dash.right = two, None
        V.left,V.right = three,None
        H.left,H.right = four,five

        self.root = root

    def decodeSymbol(self,symbols):
        root = self.root
        info = root.info
        for symbol in symbols:
            try:
                root = root.right if symbol == "." else root.left
                info = root.info
            except Exception as e:
                return info

        return info





