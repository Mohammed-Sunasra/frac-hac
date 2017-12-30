import operator

class Document(object):

    def __init__(self, data):
        """

        :param data:
        """
        self.data = data
        self.documents = self.getDocuments()

    def getDocuments(self):
        """
        Fetches all the documents returned by DB for a PID
        And creates a dict of key(id) and value(question)
        :return:
        """
        data = {}
        documents = self.data
        for line in documents:
            doc_id = line['id']
            question = line['question']
            data[doc_id] = question
        return data

    def sortDictionary(self,dict):
        """
        Sorts the results returned after calculating BM25

        :param dict:
        :return:
        """
        sorted_dic = sorted(dict.items(), key=operator.itemgetter(1))
        return sorted_dic