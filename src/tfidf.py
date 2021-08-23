from sklearn.feature_extraction.text import TfidfVectorizer


def tf_idf_compute(content):
    '''Constructs the tf-idf matrix on the input text.

            Parameters:
            content: the text data

            Returns:
            tfidf_matrix:  ndarray that represent the book (sentence) data
    '''

    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(content)

    return tfidf_matrix