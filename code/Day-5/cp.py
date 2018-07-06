def compound_interest(P,R,T):
     CI = P * (pow((1 + R / 100), T))
     print("Compound interest is", CI)
P=float(input("Enter the value of principle"))
R=float(input("Enter the value of rate"))
T=float(input("Enter the value of time"))

compound_interest(P,R,T)
