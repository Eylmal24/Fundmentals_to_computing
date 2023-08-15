def main():
    import math

    L = eval(input("what is the length of of the box? " ))
    W = eval(input("what is the width of the box? " ))
    P = 2*L + 2*W
    X = P/12
    Q = math.ceil(X)
    T = (Q - X)*12
    K = Q*1.88
    V = (Q - X)*1.88
    print("the perimeter of the box is" , P)
    print("you'll need" ,Q , "segments")
    print("this will cost", round(K,2))
    print("you will waste" , round(T,2), "inches trim, which equates to a waste of $", round(V,2), "cents")
main()
