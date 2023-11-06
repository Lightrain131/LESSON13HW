def quadraticFormula1(a,b,c):
    x = (-b+(b**2-4*a*c)**0.5)/(2*a)
    return(x)
def quadraticFormula2(a,b,c):
    y = (-b-(b**2-4*a*c)**0.5)/(2*a)
    return(y)
print(quadraticFormula1(1,8,9))
print(quadraticFormula2(1,8,9))
quit()
