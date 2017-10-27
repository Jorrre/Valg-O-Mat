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
  
