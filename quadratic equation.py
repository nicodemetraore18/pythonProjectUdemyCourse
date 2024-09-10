import cmath

# Demande des coefficients a, b, c
a = float(input("Entrez le coefficient a: "))
while(a==0):
    print("Le coefficient 'a' doit être différent de zéro pour une équation quadratique.")
    a = float(input("Entrez le coefficient a: "))
b = float(input("Entrez le coefficient b: "))
c = float(input("Entrez la constante c: "))

# Vérification si a n'est pas égal à 0 (sinon, ce n'est pas une équation quadratique)

    # Calcul du discriminant
# Calcul du discriminant
discriminant = b ** 2 - 4 * a * c

# Calcul des racines en utilisant cmath.sqrt pour les racines complexes
root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

# Affichage des résultats
print(f"Les racines sont : x1 = {root1}, x2 = {root2}")