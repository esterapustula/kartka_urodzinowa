imie_nadawcy = input("podaj imie nadawcy: ")
rok_ur = int(input ("podaj rok urodzenia: "))
wiadomosc = input("dodaj wiadomosc: ")
imie_odbiorcy = input("podaj imie odbiorcy: ")

aktualnyrok = 2025
wiek_odbiorcy = aktualnyrok - rok_ur
print("Kartka urodzinowa dla Ciebie")
print(f"Hej, {imie_odbiorcy}!")
print(f"Z okazji Twoich {wiek_odbiorcy} urodzin, {wiadomosc}")
print(f"Miłego dnia, {imie_nadawcy}")