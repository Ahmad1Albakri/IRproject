import documentClustering
import preprocess
from CacmDataSet import read_cacm_data
import tf_idf
from spacy.lang.en import English
import spacy
import datefinder

sp = spacy.load('en_core_web_lg')
sp.add_pipe("merge_entities")

nlp = English()


def execute():
    print("dataset")
    mps = read_cacm_data.get_cacm_data("CacmDataSet/cacm.all")

    idx = 0
    for x in mps:
        z = [jj for jj in sp(x).doc if jj.ent_type_ == "DATE"]
        for zz in z:

            tmp = list(datefinder.find_dates("default " + zz.text + " default"))

            # print(tmp, "   ", zz)
            if len(tmp) > 0:
                mps[idx] += " " + sp(tmp[0].date().strftime("%Y/%m/%d")).text
                # print(mps[idx])
        idx += 1

    # print()
    # print()
    preprocessed_data_set = preprocess.preprocess(mps)
    print('end cacm')

    ret = tf_idf.indexCacm(preprocessed_data_set)
    documentClustering.kMeans(tf_idf.cacmDocs, False)

