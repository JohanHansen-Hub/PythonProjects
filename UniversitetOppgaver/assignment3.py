#Oppgave 1
#Inspirasjon og kilde: https://www.youtube.com/watch?v=g_xesqdQqvA
def BubbleSortPasses(liste, passes):
    index_lengde = len(liste) - 1
    for i in range(passes):
        for i in range(0, index_lengde):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
    return liste

liste_av_tall = [1900, 100, 900, 700, 300, 1000, 1300, 1500, 800, 1200]
print(BubbleSortPasses(liste_av_tall, 3))
#Som vi ser så samsvarer dette med listen i b)


# Oppgave 2

# Svaret er c)

# Avhenger av mengden arbeid datamaskinen må gjennomføre for å sortere listen
# Ved merge sort blir listen delt opp i mindre lister som blir videre delt og sortert
# Til slutt setter mann sammen listene igjen, bare denne gangen sortert
# Siden algoritmen ikke avhengiger av mange iterasjoner, tar sorteringen mindre tid.
# Big O notasjon beskriver funksjonen for mengden iterasjoner som må gjennomføres
# eks: en dobbel for løkke vil bety O(n^2) naturligvis osv.

# Oppgave 3

# Bruker bubblesort:
def sort_and_print(tuple_liste):
    liste = [i[1] for i in tuple_liste]
    liste_navn = [i[0] for i in tuple_liste]
    index_lengde = len(liste) - 1
    sorter = True
    while sorter:
        sorter = False
        for i in range(0, index_lengde):
            if liste[i] > liste[i+1]:
                sorter = True
                liste[i], liste[i+1] = liste[i+1], liste[i]
                liste_navn[i], liste_navn[i + 1] = liste_navn[i + 1], liste_navn[i]
    ny_liste = []
    for i in range(len(liste)):
        tuple = (liste_navn[i], liste[i])
        ny_liste.append(tuple)
    movie_title = ny_liste[-1][0]
    print("\nThe movie with the largest budget is:\n"+movie_title)

list_of_tuples = [('Birds of Prey', 97.1), ('Dolittle', 175.0), ('The Gentlemen', 7.0), ('Falling', 22.0)]
sort_and_print(list_of_tuples)