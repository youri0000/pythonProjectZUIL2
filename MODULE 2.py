import csv
import psycopg2
import datetime
#modules importeren zodat ze te gebruiken zijn.#

#functie om als moderator een bericht goed te keuren#
def berichtgoedkeuren():

    #inputs om in te loggen als moderator#.
    modnaam = input('Wat is uw naam? ')
    modmail = input('Wat is uw email? ')

    #goedkeuringsmoment toevoegen aan het bericht#
    goedkeuringsdatum = str(datetime.datetime.now())

    #txt bestand omzetten naar csv bestand om elke variabel te splitsen met komma's.#
    with open('project.txt', 'r') as csvfile:
        reader = csv.reader(csvfile)

        #per rij lezen om te keuren.#
        for row in reader:
            keuring = input('Welkom ' + modnaam + ' wilt U dit bericht van, ' + row[0] + ': ' + row[1] +' , goedkeuren? (True of False)\n')

            if keuring == 'True':
                print('Het bericht is goedgekeurd, op {}\n'.format(goedkeuringsdatum))

                #database laat de functie database() runnen met alle variabelen van database erachter, row[0] is de naam, row[1] is het bericht etc.#
                database(row[0], row[1], row[2], row[3], "true", modmail, goedkeuringsdatum)

            elif keuring == 'False':
                print('Het bericht is afgekeurd, op {}\n'.format(goedkeuringsdatum))
                database(row[0], row[1], row[2], row[3], "False", modmail, goedkeuringsdatum)

            #elif statements, als je verkeerde inloggegevens invoert krijg je een foutmelding en een mogelijkheid het opnieuw te proberen.#
            elif modnaam != 'youri':
                print('Uw moderatornaam is fout.')
            elif modmail != 'yourijansen01@gmail.com':
                print('uw moderator email is fout')
            else:
                break


#functie om een bericht dat is goed- of afgekeurd is naar de database te schrijven(PostgreSQL).#
def database(naam, bericht, datum, station, goedgekeurd, modmail, goedkeuringsdatum):

    #statement om de database te openen, en alle kolommen in te voeren.#
    try:
        sql = f"INSERT INTO berichten(naam, bericht, datum, station, goedgekeurd, modmail, goedkeuringsdatum)values('{naam}' , '{bericht}' , '{datum}', '{station}', '{goedgekeurd}' , '{modmail}' , '{goedkeuringsdatum}');"
        conn = psycopg2.connect("host='localhost' dbname='projectzuil' user='postgres' password='12Ysma34!' port=5432")
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

berichtgoedkeuren()
