def result(user_answers, data_file, rank_array):
    #winners_alt = []
    rankings = [0, 0, 0, 0, 0, 0]

    # Summerer opp poengene
    for e in range(0, len(user_answers)):
        if user_answers[e] == 'Ja':
            for i in range(0, len(rankings)):
                rankings[i] += data_file['spm'][e]['vekt'][0][i]
        elif user_answers[e] == 'Nei':
            for i in range(0, len(rankings)):
                rankings[i] += data_file['spm'][e]['vekt'][2][i]
        else:
            for i in range(0, len(rankings)):
                rankings[i] += data_file['spm'][e]['vekt'][1][i]

    # Kopierer rankings[] til winners[] for å sortere winners[]
    winners = []
    for k in rankings:
        winners.append(k)
    winners.sort(reverse=True)

    # Sorterer svaralternativstringene
    for x in range(0, len(winners)):
        for y in range(0, len(rankings)):
            if winners[x] == rankings[y] and data_file['alt'][y] not in rank_array:
                rank_array.append(data_file['alt'][y])
                break
            elif winners[x] == rankings[y] and data_file['alt'][y] in rank_array:
                rank_array.append(data_file['alt'][y + 1])

    #return winners_alt