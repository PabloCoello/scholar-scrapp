from scholarly import scholarly, ProxyGenerator


class Scholar():
    '''
    Wrapper of scholarly python library: https://pypi.org/project/scholarly/
    '''

    def __init__(self):
        '''
        Defines scholarly object using container tor proxy.
        '''
        self.sc_ = scholarly
        self.sc_.use_proxy(self.get_tor_proxy())

    def get_tor_proxy(self):
        '''
        Set tor proxy with default settings.
        '''
        pg = ProxyGenerator()
        pg.Tor_External(tor_sock_port=9050,
                        tor_control_port=9051,
                        tor_password="scholarly_password")
        return pg

    def get_docs_keyword(self, keyword):
        '''
        Return documents iterable by keyword.

        args:
            -keyword: str -- keyword to search for in google scholar.

        '''
        return self.sc_.search_pubs(keyword)

    def get_author_name(self, name):
        '''
        Return authors iterable by name.

        args:
            -name: str -- name of the author.

        '''
        return self.sc_.search_author(name)

    def get_author_id(self, id):
        '''
        Return authors iterable by Google Scholar id.

        args:
            -id: str -- Google Scholar id of the author.

        '''
        return self.sc_.search_author_id(id)

    def get_author_keyword(self, keyword):
        '''
        Return authors iterable by keyword.

        args:
            -keyword: str -- keyword to search for authors in Google Scholar.
            
        '''
        return self.sc_.search_keyword(keyword)

    def fill_author(self, author, sections):
        '''
        Fill single author object with extra data.

        args:
            author: object -- single author object to be filled.
            sections: list -- can take one or more of the following values:
                'basics' = name, affiliation, and interests;
                'indices' = h-index, i10-index, and 5-year analogues;
                'counts' = number of citations per year;
                'coauthors' = co-authors;
                'publications' = publications;
                '[]' = all of the above (this is the default)

        '''
        return self.sc_.fill(author, sections)

    def get_citedby(self, document):
        '''
        Searches Google Scholar for other articles that cite a given document
        and returns a documents iterable.

        args:
            -document: object -- initial document for searching its cites.

        '''
        return self.sc_.citedby(document)

    def get_bibtex_reference(self, document):
        '''
        Return bibtex reference for a given document object

        args:
            -document: object -- document to extract bibtex reference.
        '''
        return self.sc_.bibtex(document)
