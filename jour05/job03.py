def length(s, i=0):
    if s == '':
        return i
    else:
        return length(s[1:], i+1)

s = input("Entrez une chaine de caractères : ")
print("La longueur de", s, "est", length(s))