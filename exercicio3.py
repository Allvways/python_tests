a = float(input("escreva o valor de a: "))
b = float(input("escreva o valor de b: "))
c = float(input("escreva o valor de c: "))
delta = (b**2 - 4*a*c)

raiz1 = -b + delta**(1/2)/ (2*a)

raiz2 = -b - delta**(1/2)/ (2*a)

print("essa é a sua primeira raiz:" , raiz1)
print("essa é a sua segunda raiz:" , raiz2)

exit()