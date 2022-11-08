import random #Import statements om de module te kunnen gebruiken.#
import datetime
while True:
    def bericht():
        naam = input('Wat is uw naam? Als u anoniem wilt blijven vult u niks in.\n')
        #als er niks ingevuld wordt zal er bij naam, anoniem ingevuld worden.#
        if len(naam) == (0):
            naam = 'anoniem'
        bericht = input('Hoi {} wat is uw mening over dit station? (max 140 tekens gebruiken.)\n'.format(naam))

        #als de input minder lang is dan 141 tekens voert hij de volgende statements uit.#

        if len(bericht) < (141):
            print('{}\n{}'.format(bericht, naam))

            #geeft de tijd aan van het moment dat het bericht geschreven is.#
            date = datetime.datetime.now()
            print(date)

            #deze functie pakt een random station uit de lijst.#
            station = ['Utrecht Centraal', 'Amsterdam Centraal', 'Amersfoort Centraal']
            a = (random.choice(station))
            print(a)

            #in deze functie schrijft de code het bericht incl de gegevens weg in het txt bestand.#
            file = open('project.txt', 'a')
            file.write('{},{},{},{}\n'.format(naam, bericht, date, a))
            file.close()

        #als het bericht 141 tekens of meer is zal het systeem een error aangeven#
        else:
            print('Uw bericht is te lang!, Probeer opnieuw.')
    bericht()
