print("v3.0 | Uncrypter")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

for x in range(0,100):
    print("Entrez un message à crypter")
    chaîneACrypter = input("")
    chaîneACrypter = chaîneACrypter.upper()
    quantitéDécalage = int(input("Entre un nombre entre 1 et 25 pour crypter/décrypter ton message"))
    chaîneCryptée = ""
    for caractèreActuel in chaîneACrypter:
        position = alphabet.find(caractèreActuel)
        nouvellePosition = position + quantitéDécalage
        if caractèreActuel in alphabet:
            chaîneCryptée = chaîneCryptée + alphabet[nouvellePosition]
        else:
            chaîneCryptée = chaîneCryptée + caractèreActuel
    for x in range(0, 2000):
        print("-----------------------")
    print("Message:", chaîneCryptée)
    print("Thanks for use my programm")

