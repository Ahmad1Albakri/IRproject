import spacy
from spacy.lang.en import English
from nltk.stem import PorterStemmer
from textblob import Word

nlp = English()

sp = spacy.load('en_core_web_lg')
# sp.add_pipe("merge_entities")
all_stopwords = sp.Defaults.stop_words
ps = PorterStemmer()


def preprocess(docs):
    print("st")
    return [lemmatize(remove_stopwords(remove_punc(tokenize(normalize(doc))))) for doc in docs]


def preprocess_query(query):
    return lemmatize(remove_stopwords(remove_punc(tokenize(normalize(query)))))


def tokenize(mps):
    mps = nlp(mps)
    # print("token")
    # print(mps)

    return [word.text for word in mps]


def remove_punc(mps):
    ret = [word.text for word in nlp(" ".join(mps)) if not word.is_punct and not word.is_space and len(word.text) > 1]
    # print("remove punc")
    # print(ret)

    return ret


def remove_stopwords(mps):
    ret = [word for word in mps if not (word in all_stopwords)]
    # print("remove stopwords")
    # print(ret)

    return ret


def normalize(mps):
    mps = mps.lower().replace('.', '')
    # print("normalize")
    # print(mps)

    return mps


def lemmatize(mps):
    mps = [ps.stem(word.lemma_) for word in sp(" ".join(mps))]
    mps = " ".join(mps)
    # print("lemmatize")
    # print(mps)

    return mps
