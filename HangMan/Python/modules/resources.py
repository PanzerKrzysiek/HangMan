##################################
# resources.py by PanzerKrzysiek #
##################################

"""   This module contains the additional informations.   """

loop_choice_message = \
"""Wybierz opcję:
  1. Odgadnij spółgłoskę.
  2. Kup samogłoskę.
  3. Odgadnij hasło.
  4. Rozpocznij nową grę.
  5. Informacje o programie."""

vowel_buying_message = \
"""Którą samogłoskę chcesz kupić? Wprowadź numer:
  1. A – 150 zł.
  2. Ą – 50 zł.
  3. E – 120 zł.
  4. Ę – 50 zł.
  5. I – 100 zł.
  6. O – 100 zł.
  7. Ó – 40 zł.
  8. U – 90 zł.
  9. Y – 100 zł."""

keyword_guess_message = \
"""\
Odgadnij hasło.
Zostaw puste miejsce i naciśnij Enter, aby wyjść.
"""

game_ended_message = \
"""\
1. Zagraj jeszcze raz.
2. Wyjdź z gry.
"""

generate_new_game_message = \
"""\
Czy na pewno chcesz rozpocząć nową grę?
1. Tak.
2. Nie.\
"""

program_informations = \
"""\
HangMan 1.0 by PanzerKrzysiek.

Rozpoczęcie pisania programu: czwartek, 20 stycznia 2022 r.
Zakończenie pisania programu: niedziela, 27 lutego 2022 r.

INSTRUKCJA GRY.
Na początku gry, użytkownik dostaje 200 zł, które może wydawać w dalszej
części rozgrywki i zostawać nagradzany poprzez dodanie pieniędzy.
Następnie, gra losuje jedno z pięćdziesięciu sześciu słów. Zadaniem gracza
jest odgadnięcie hasła. Ma trzy możliwości odgadnięcia:
  1. Odgadnięcie spółgłosek w haśle (jest darmowe). Jeżeli poprawnie wybierze
     spółgłoskę, otrzymuje 100 zł, jeżeli źle – traci 20 zł.
  2. Kupienie samogłoski. Gracz ma możliwość kupienia dziewięć
     polskich samogłosek (A, Ą, E, Ę, I, O, Ó, U oraz Y). Każdej samogłosce
     przypada następująca cena:
       A – 150 zł, Ą – 50 zł, E – 120 zł,
       Ę – 50 zł, I – 100 zł, O – 100 zł,
       Ó – 40 zł, U – 90 zł, Y – 100 zł.
     Jeżeli gracz wybierze samogłoskę, która znajduje się w haśle, jej koszt
     zostaje pokryty. Na dodatek, gracz dostaje wtedy dodatkowe 10 zł.
     Jeżeli gracz źle wybierze samogłoskę, traci dodatkowo 10 zł.
  3. Bezpośrednie odgadnięcie hasła. Jeśli gracz pomyślnie odgadnie hasło,
     gra kończy się zwycięstwem. W przeciwnym wypadku, traci 50 zł.
Gra kończy się zwycięstwem, gdy gracz odgadnie hasło.
Jeżeli budżet gracza pod koniec gry wyniesie 0 zł lub będzie mniejszy,
gra zakończy się porażką.\
"""