import json

with open('./static/data.json') as data:
    j = json.load(data)

answers = []
winners_alt = []


def result(user_answers):
    rankings = [0, 0, 0, 0, 0, 0]

    # Summerer opp poengene
    for e in range(0, len(user_answers) - 1):
        if user_answers[e] == 'Ja':
            for i in range(0, len(rankings) - 1):
                rankings[i] += j['spm'][e]['vekt'][0][i]
        elif user_answers[e] == 'Nei':
            for i in range(0, len(rankings) - 1):
                rankings[i] += j['spm'][e]['vekt'][2][i]
        else:
            for i in range(0, len(rankings) - 1):
                rankings[i] += j['spm'][e]['vekt'][1][i]

    # Kopierer rankings[] til winners[] for å sortere winners[]
    winners = []
    for k in rankings:
        winners.append(k)
    winners.sort(reverse=True)

    # Sorterer svaralternativstringene
    for x in range(0, len(winners) - 1):
        for y in range(0, len(rankings) - 1):
            if winners[x] == rankings[y] and j['alt'][y] not in winners_alt:
                winners_alt.append(j['alt'][y])
                break
            elif winners[x] == rankings[y] and j['alt'][y] in winners_alt:
                winners_alt.append(j['alt'][y + 1])

    # Endrer på plasseringsnummerene hvis det er flere svaralternativer som har like mange poeng
    for f in range(0, len(winners_alt) - 1):
        if f < len(winners_alt) - 1 and winners_alt[f] == winners_alt[f + 1]:
            # sett plasseringstallet til winners_alt[f + 1] til winners_alt[f]
            print("")

'''
    --== NOTES ==--
    winners_alt[] inneholder j['alt'] stringene i sortert rekkefølge
    Bytt navn på rankings[] til winners_alt[] i app.py og fjern alle verdiene.
    rankings[] blir definert som et lokalt array inne i result().
    rankings i done.html må byttes ut med winners_alt
    Fungerer som den skal, bortsett fra æ, ø og å.
    --== END ==--
'''
