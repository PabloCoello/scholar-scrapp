class Document():
    def __init__(self, doc):
        self.doc_ = doc

    def get_bib_citation(self, scholarly):
        '''
        '''
        return scholarly.bibtext(self.doc_)