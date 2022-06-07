from relevance import readRel
import pandas as pd
import relevance.score as score
from CacmDataQyery import queryCacmHandler


# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


df = pd.DataFrame()


def execute():
    global df
    df = readRel.getPositive("relevance/qrels.text")

    # ['qid', 'docId', 'precision', 'recall']

    query_result = queryCacmHandler.execute()
    qid = 0
    print("checkRel")
    for val in query_result:
        qid += 1
        predictPositive = val[0]
        result = val[1]

        for i in range(0, len(predictPositive)):
            predictPositive[i] += 1

        realPositive = df.loc[df['qid'] == str(qid), 'docId'].tolist()
        if len(realPositive) == 0:
            continue

        for i in range(0, len(realPositive)):
            realPositive[i] = int(realPositive[i])

        precision = score.scorePrecision(realPositive, predictPositive)
        recall = score.scoreRecall(realPositive, predictPositive)
        precision_10 = score.scorePrecision_rank(10, realPositive, predictPositive)

        print(precision, " ,,, ", recall)

        df.loc[df['qid'] == str(qid), 'precision'] = str(precision)
        df.loc[df['qid'] == str(qid), 'recall'] = str(recall)

    # print(df)
    score.meanAveragePrecision(query_result, df)
    readRel.saveCacm(df)
