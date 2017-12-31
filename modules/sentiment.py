from textblob import TextBlob


def get_sentiment(doc):
    polarity = TextBlob(doc).sentiment.polarity
    if polarity >= 0.1:
        return 0
    elif polarity <= -0.1:
        return 1
    else:
        return -1


def get_dict_sentiment(corpus_dict):
    return {qid: get_sentiment(doc) for qid, doc in corpus_dict.items()}
