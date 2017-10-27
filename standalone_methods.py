
# Må finne en måte å sortere rankings[] på samtidig som man vet hvilken verdi som tilhører hvilket alternativ ("alt" i json filen)

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
  
