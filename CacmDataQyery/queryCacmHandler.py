import preprocess
import tf_idf
from textblob import Word
import pandas as pd

from CacmDataQyery import read_cacm_query
from DataSet import readData


def execute():
    print("check query")
    query_list = read_cacm_query.get_cacm_query("CacmDataQyery/query.text")
    print("cacm qry len  = ", len(query_list))
    query_list = preprocess.preprocess(query_list)

    return [tf_idf.transform_query(query, False) for query in query_list]


def singleQuery(query):
    query = " ".join(Word(word).correct() for word in query.split())
    preProcessedQuery = preprocess.preprocess_query(query)

    results = tf_idf.transform_query(query, False)

    df = pd.DataFrame(list(zip(results[0], results[1])), columns=['idx', 'result'])

    docs = [readData.getDoc(idx) for idx in results[0]]

    return pd.DataFrame(list(zip(results[0], docs)), columns=['idx', 'doc']).to_json(orient='index')
