import preprocess
import tf_idf
from query import readQuery
from textblob import Word
import pandas as pd
from DataSet import readData


def execute():
    print("check query")
    query_list = readQuery.get_data("query/CISI.QRY")
    query_list = preprocess.preprocess(query_list)

    return [tf_idf.transform_query(query, True) for query in query_list]


def singleQuery(query):
    query = " ".join(Word(word).correct() for word in query.split())
    preProcessedQuery = preprocess.preprocess_query(query)

    results = tf_idf.transform_query(query, True)

    df = pd.DataFrame(list(zip(results[0], results[1])), columns=['idx', 'result'])

    docs = [readData.getDoc(idx) for idx in results[0]]

    return pd.DataFrame(list(zip(results[0], docs)), columns=['idx', 'doc']).to_json(orient='index')
