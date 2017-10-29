import json

with open('./static/data.json') as data:
    j = json.load(data)

answers = []
rankings = [0, 0, 0, 0, 0, 0]

def result():
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

    for i in range(0, 2):
        for e in range(0, len(rankings) - 1):
            if winners[i] == rankings[e]:
                rankings[i] = j['alt'][e]
                break
    # Denne tar forløpig ikke hensyn til hvis 2 eller flere alternativer har samme score
