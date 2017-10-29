import json

with open('./static/data.json') as data:
    j = json.load(data)

answers = []
winners_alt = []


def result():
    rankings = [0, 0, 0, 0, 0, 0]
    
    # Summerer opp poengene
    for e in range(0, len(answers) - 1):
        if answers[e] == 'Ja':
            for i in range(0, len(rankings) - 1):
                rankings[i] += j['spm'][e]['vekt'][0][i]
        elif answers[e] == 'Nei':
            for i in range(0, len(rankings) - 1):
                rankings[i] += j['spm'][e]['vekt'][2][i]
        else:
            for i in range(0, len(rankings) - 1):
                rankings[i] += j['spm'][e]['vekt'][1][i]

    winners = rankings
    winners.sort
    
    # Sorterer svaralternativstringene
    for x in range(0, len(winners) - 1):
        for y in range(0, len(rankings) - 1):
            if winners[x] == rankings[y]:
                winners_alt.append(j['alt'][y])
                break
    
    # Endrer på plasseringsnummerene hvis det er flere svaralternativer som har like mange poeng           
    for f in range(0, len(winners_alt) - 1):
        if f < len(winners_alt) - 1 and winners_alt[f] == winners_alt[f + 1]:
            # sett plasseringstallet til winners_alt[f + 1] til winners_alt[f]
    '''
    --== NOTES ==--
    winners_alt[] inneholder j['alt'] stringene i sortert rekkefølge
    Bytt navn på rankings[] til winners_alt[] i app.py og fjern alle verdiene. 
    rankings[] blir definert som et lokalt array inne i result().
    rankings i done.html må byttes ut med winners_alt
    '''  
