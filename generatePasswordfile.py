# Liste de mots de passe usuels couramment utilisés
common_passwords = [
    "123456", "password", "123456789", "12345678", "12345", "1234567",
    "123123", "qwerty", "abc123", "password1", "111111", "1234", "1q2w3e4r",
    "admin", "letmein", "welcome", "monkey", "sunshine", "iloveyou", "football",
    "000000", "123321", "qwertyuiop", "654321", "superman", "hello", "master",
    "freedom", "whatever", "qazwsx", "trustno1", "jordan23", "test", "baseball",
    "cheese", "chocolate", "shadow", "dragon", "mustang", "starwars", "batman"
]

# Nom du fichier où les mots de passe seront stockés
filename = "common_passwords.txt"

# Écriture de la liste de mots de passe dans le fichier
with open(filename, 'w') as file:
    for password in common_passwords:
        file.write(password + "\n")

print(f"Le fichier '{filename}' a été généré avec succès.")
