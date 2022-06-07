import re
import pandas as pd


def getPositive(file_path):
    with open(file_path, 'r') as f:
        text = f.read()

        new_line = re.compile('\n')

        lines = re.split(new_line, text)
        tmp = []
        for line in lines:
            q = line.split()
            if len(q) == 0:
                continue
            tmp.append(q)

        df = pd.DataFrame(tmp, columns=['qid', 'docId', 'precision', 'recall'])
        return df


def save(res):
    res.to_csv('relevance/out.csv', index=False)


def saveCacm(res):
    res.to_csv('relevance/cacmOut.csv', index=False)
