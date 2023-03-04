def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = power(x, n/2)
        return y * y
    else:
        return x * power(x, n-1)

x = int(input("Veuillez entrer un nombre entier x : "))
n = int(input("Veuillez entrer un nombre entier n : "))
print(x, "à la puissance", n, "est", power(x, n))