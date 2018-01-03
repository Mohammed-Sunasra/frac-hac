import pandas as pd
import spacy

nlp = spacy.load('en')

class Document(object):

    def __init__(self, data, query, column):
        """
        Helper methods for semantic similarity of the documents
        :param data:
        :type data:
        :param query:
        :type query:
        :param column:
        :type column:
        """
        self.data = pd.DataFrame(data)
        self.query = unicode(query)
        self.column = column
        # self.documents = self.get_documents()

    def get_similar_documents(self, threshold=0.5):
        """
        Returns similar documents for the query with similarity score greater than the threshold value

        :param threshold: Threshold value
        :type threshold: float
        :return: Request data
        :rtype: dict
        """
        docs = self.data[self.column].apply(nlp)
        query = nlp(self.query)
        self.data['similarity_score'] = docs.apply(query.similarity)
        similar_data = self.data[self.data['similarity_score'] > threshold]
        return similar_data.T.to_dict().values()
