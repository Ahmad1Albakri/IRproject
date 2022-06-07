from sklearn.cluster import KMeans
import pandas as pd
import tf_idf

Sum_of_squared_distances = []
clusters = None
# 280
km = KMeans(n_clusters=10, init='k-means++', random_state=0)
cacmKm = KMeans(n_clusters=50, init='k-means++', random_state=0)
df = pd.DataFrame()
cacmDf = pd.DataFrame()


def kMeans(docs,cisiFlag):
    global clusters
    global df
    global cacmDf
    if cisiFlag:
        clusters = km.fit(docs)
        labels = clusters.labels_
        df = pd.DataFrame(list(zip(docs, labels)), columns=['vector', 'cluster'])
        df = df.sort_values(by=['cluster'])
    else:
        clusters = cacmKm.fit(docs)
        labels = clusters.labels_
        cacmDf = pd.DataFrame(list(zip(docs, labels)), columns=['vector', 'cluster'])
        cacmDf = cacmDf.sort_values(by=['cluster'])
    print("end cluster")


def queryCluster(query, cisiFlag):
    if cisiFlag:
        k = km.predict(query)
        tmp = df.loc[df['cluster'] == k[0], 'vector'].tolist()
        idx = df.index[df['cluster'] == k[0]]
        ret = []
        for i in range(0, len(tmp)):
            ret.append(tmp[i].getA()[0])
        return [ret, idx]
    else:
        k = cacmKm.predict(query)
        tmp = cacmDf.loc[cacmDf['cluster'] == k[0], 'vector'].tolist()
        idx = cacmDf.index[cacmDf['cluster'] == k[0]]
        ret = []
        for i in range(0, len(tmp)):
            ret.append(tmp[i].getA()[0])
        return [ret, idx]
