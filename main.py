def Verificare_nr_prim(n):
    """
    Functia verifica dac un numar dat este prim
    :param n: Numarul care se verifica
    :return: True daca nr este prim si False in caz contrar
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for d in range(2, n // 2 + 1):
            if n % d == 0:
                return False
    return True


def toate_nr_prime(list):
    for x in list:
        if not Verificare_nr_prim(x):
            return False
    return True


def get_longest_all_primes(list):
    """
    Determina cea mai lunga subsecventa de numere prime
    :param list: lista de numere intregi
    :return:una din cele mai lungi subsecvente de nr prime
    """
    secventaMax = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if toate_nr_prime(list[i:j + 1]) and len(list[i:j + 1]) > len(secventaMax):
                secventaMax = list[i:j + 1]
    return secventaMax


def test_get_longest_all_primes():
    assert get_longest_all_primes([2, 3, 18, 5, 47, 61]) == [5, 47, 61]
    assert get_longest_all_primes([6, 18, 56]) == []
    assert get_longest_all_primes([14, 5, 22]) == [5]


def cifre_prime(n):
    """
    Verifica daca cifrele unui numar sunt nr prime
    :param n: numarul verificat
    :return: True daca cifrele sale sunt prime si False in caz contrar
    """
    if n < 10:
        if n == 2 or n == 3 or n == 5 or n == 7:
            return True
        else:
            return False
    elif n > 10:
        while n != 0:
            if n % 10 == 1 or n % 10 == 4 or n % 10 == 6 or n % 10 == 8 or n % 10 == 9:
                return False
            n = n//10
    return True


def get_longest_prime_digits(list):
    """
    Functia verifica daca toate numerele sunt formate din cifre prime
    :param list: lista de numere intregi
    :return: True daca sunt doar nr alcatuite din cifre prime si False in caz contrar
    """
    for x in list:
        if not cifre_prime(x):
            return False
    return True


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([2, 22, 75]) is True
    assert get_longest_prime_digits([61, 7]) is False
    assert get_longest_prime_digits([83, 77, 55, 5]) is False


def Citire_lista():
    list = []
    vector = input("dati lista: ")
    numere = vector.split(" ")
    for x in numere:
        list.append(int(x))
    return list


def printMenu():
    print("1.Citire date ")
    print("2.Determina cea mai lunga secventa in care numerele sunt prime ")
    print("3.Verifica daca toate numerele sunt formate din cifre prime ")
    print("4.Iesi ")


def main():
    test_get_longest_all_primes()
    test_get_longest_prime_digits()
    list = []
    while True:
        printMenu()
        optiune = input("Alegeti o optiune: ")
        if optiune == "1":
            list = Citire_lista()
        elif optiune == "2":
            print(get_longest_all_primes(list))
        elif optiune == "3":
            if get_longest_prime_digits(list):
                print("Toate numerele sunt formate din cifre prime ")
            else:
                print("Nu toate numerele sunt formate doar din cifre prime ")
        elif optiune == "4":
            break
        else:
            print("Optiune invalida! Reincercati ")


if __name__ == "__main__":
    main()
