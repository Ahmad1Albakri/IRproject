from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

import documentClustering

vectorizer = TfidfVectorizer()
docs = None
cacmDocs = None


def index(corpus):
    print("index data set")
    global docs
    docs = vectorizer.fit_transform(corpus)
    docs = docs.todense()


def indexCacm(corpus):
    print("index cacm")
    global cacmDocs
    cacmDocs = vectorizer.fit_transform(corpus)
    cacmDocs = cacmDocs.todense()


def transform_query(query, isCisi):
    query_tfidf = vectorizer.transform([query])
    pair = documentClustering.queryCluster(query_tfidf.todense(), isCisi)
    cluster = pair[0]
    idx = pair[1]
    result = cosine_similarity(cacmDocs, query_tfidf).flatten()

    df = pd.DataFrame(list(zip(idx, result)), columns=['idx', 'result'])
    # df = pd.DataFrame(list(zip(result)), columns=['result'])
    # df['idx'] = list(range(len(df['result'])))
    df = df.sort_values(by=['result'], ascending=False)

    idxRet = list(df.loc[df['result'] > 0.0, 'idx'])
    resultRet = df.loc[df['result'] > 0.0, 'result'].tolist()

    # ret = ([idxRet[x] for x in range(len(idxRet)) if x < 10], [resultRet[x] for x in range(len(resultRet)) if x < 10])
    ret = (idxRet, resultRet)
    return ret


