from sklearn.metrics.pairwise import linear_kernel


def cos_sim(tfidf_matrix):
    '''function to compute the similarity between different books title

        Parameters:
            tfidf_matrix (ndarray): matrix that represent the text data (content)

        Returns:
            cosine_sim (ndarray): Matrix where each value represent the similarity scores between 2 books.
    '''
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    return cosine_similarities