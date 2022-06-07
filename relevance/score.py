def scoreRecall(real, predicted):
    intersect = [val for val in real if val in predicted]
    # recall = predicted positive / real positive
    recall = len(intersect) / len(real)
    return recall


def scorePrecision(real, predicted):
    intersect = [val for val in real if val in predicted]
    precision = len(intersect) / len(predicted)
    return precision


def scorePrecision_rank(r, real, predicted):
    predicted_rank = [predicted[i] for i in range(len(predicted)) if i <= r]
    intersect = [val for val in real if val in predicted_rank]
    precision = len(intersect) / len(predicted_rank)
    return precision


def averagePrecision(real, predicted):
    ranksSum = 0.0
    counter = 0
    for i in range(len(predicted)):
        counter += 1
        if predicted[i] not in real:
            continue
        ranksSum += scorePrecision_rank(i, real, predicted)
    return ranksSum / counter


def meanAveragePrecision(query_result, df):
    sumAvgPrecision = 0.0
    queryId = 0

    for val in query_result:
        queryId += 1

        predictPositive = val[0]
        result = val[1]

        realPositive = df.loc[df['qid'] == str(queryId), 'docId'].tolist()
        if len(realPositive) == 0:
            continue

        for i in range(0, len(predictPositive)):
            predictPositive[i] += 1

        for i in range(0, len(realPositive)):
            realPositive[i] = int(realPositive[i])

        sumAvgPrecision += averagePrecision(realPositive, predictPositive)

    return sumAvgPrecision / queryId
