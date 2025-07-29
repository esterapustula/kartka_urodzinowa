magazyn = {
    "spodnie": {"cena": 70, "ilość": 5},
    "swetry": {"cena": 50, "ilość": 7},
    "koszulki": {"cena": 30, "ilość": 3},
    "szorty": {"cena": 40, "ilość": 4},
}

historia = []

konto = 0

while True:
    komenda = input("Witaj, napisz 'POKAŻ' a wyświetlę dostępne opcje ").upper()
    print(f"Wpisałeś komendę: {komenda}")

    if komenda == "KONIEC":
        print("Zakończenie programu.")
        break

    elif komenda == "SALDO":
        historia.append(komenda)
        operacja = input("DODAĆ czy ODJĄĆ: ").upper()
        kwota = int(input("Kwota: "))
        if operacja == "DODAĆ":
            konto += kwota
            print(f"Stan konta wynosi: {konto}")
        elif operacja == "ODJĄĆ":
            if konto >= kwota:
                konto -= kwota
                print (f"Stan konta wynosi: {konto}")
            else:
                print("Błąd: niewystarczające środki.")


    elif komenda == "SPRZEDAŻ":
        historia.append(komenda)
        towar = input("Jaki produkt chcesz sprzedać?: ").lower()
        ilosc = int(input(f"Ile sztuk chcesz sprzedać? "))

        if towar in magazyn and magazyn[towar]["ilość"] >= ilosc:
            magazyn[towar]["ilość"] -= ilosc
            if magazyn[towar]["ilość"] == 0:
                del magazyn[towar]

            print(f"Sprzedano towar: '{towar}', liczba sztuk: {ilosc}")
        else:
            print(f"Brak wystarczającej liczby sztuk '{towar}', bądź nie ma go w magazynie")



    elif komenda == "ZAKUP":
        historia.append(komenda)
        zakup = input("Co chcesz dodać do magazynu?: ").lower()
        liczba_sztuk = int(input("Ile sztuk chcesz zakupić?: "))

        if zakup in magazyn:
            print(f"Produkt '{zakup}' już istnieje w magazynie.")
            zmien_cene = input("Czy chcesz zmienić cenę? (tak/nie): ").lower()
            if zmien_cene == "tak":
                nowa_cena = int(input("Podaj nową cenę: "))
                magazyn[zakup]["cena"] = nowa_cena

            magazyn[zakup]["ilość"] += liczba_sztuk
        else:
            cena = int(input("Podaj cenę nowego produktu: "))
            magazyn[zakup] = {"cena": cena, "ilość": liczba_sztuk}

        print(f"Wprowadzono towar: '{zakup}', liczba sztuk: {liczba_sztuk}, cena: {magazyn[zakup]['cena']} zł")


    elif komenda == "KONTO":
        historia.append(komenda)
        towar = input("Podaj nazwę towaru (np. spodnie, swetry): ").lower()
        if towar in magazyn:
            cena = magazyn[towar]["cena"]
            ilosc = magazyn[towar]["ilość"]
            zarobek = cena * ilosc
            konto += zarobek
            print(f"Zarobiono {zarobek} zł. Nowy stan konta: {konto}")
        else:
            print("Nie ma takiego towaru w magazynie.")


    elif komenda == "LISTA":
        historia.append(komenda)
        print ("Oto przedmioty w magazynie wraz z ich ceną i ilością sztuk.")
        for produkt, dane in magazyn.items():
            print (f" {produkt.title()}: cena: {dane['cena']} zł, ilość: {dane['ilość']} szt.")

    elif komenda == "MAGAZYN":
        historia.append(komenda)
        stan_magazynu = input("Wybierz nazwę produktu, aby wyświetlić jego ilość").lower()
        if stan_magazynu in magazyn:
            ilosc = magazyn[stan_magazynu]['ilość']
            print(f"Produkt '{stan_magazynu}' - ilość w magazynie: {ilosc} szt.")
        else:
            print(f"Produkt '{stan_magazynu}' nie znajduje się w magazynie. ")

    elif komenda == "PRZEGLĄD":
        historia.append(komenda)
        od = int(input("Podaj przedział od: "))
        do = int(input("Podaj przedział do: "))
        if od >= 0 and do <= len(historia):
            print ("Historia operacji: ")
        else:
            print("Na podstawie wykonanych komend, podaj odpowiedni zakres. ")
            print (historia)
        for wpis in historia[od:do]:
            print(f" - {wpis}")

    elif komenda == "POKAŻ":
        print("""
        Dostępne komendy:
        1. Saldo - Pobranie kwoty do dodania lub odjęcia z konta.
        2. Sprzedaż - Pobranie nazwy produktu, ceny i liczby sztuk z magazynu.
        3. Zakup - Pobranie nazwy produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do maga
        4. Konto - Wyświetlenie stanu konta.
        5. Lista - Wyświetlenie całkowitego stan magazynu wraz z cenami produktów i ich ilością.
        6. Magazyn - Wyświetlenie stanu magazynu dla konkretnego produktu. Należy podać jego nazwę.
        7. Przegląd - Wyświetlenie historii operacji z ich indeksami.
        8. Koniec - Zakończenie programu.
        """)

