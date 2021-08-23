import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def get_recom_text(df,target_title, cosine_similarities):
    """Return a dataframe of content recommendations based on TF-IDF cosine similarity.
    
            Args:
                df (object): Pandas dataframe containing the text data.  
                value (string): Name of title to get recommendations for, i.e. 1982 Ferrari 308 GTSi For Sale by Auction
                cosine_similarities (array): Cosine similarities matrix from linear_kernel
    
                
            Returns: 
                Pandas dataframe. 
    """
    indices = pd.Series(df.index, index=df['book_title'])
    try:
        target_index = indices[target_title]
        print(target_index)
        cosine_similarity_scores = list(enumerate(cosine_similarities[target_index]))
        print(cosine_similarity_scores)
        cosine_similarity_scores = sorted(cosine_similarity_scores, key=lambda x: x[1], reverse=True)
        print(cosine_similarity_scores)
        # Return tuple of the requested closest scores 
        cosine_similarity_scores = cosine_similarity_scores[1:6]
        # Extract the tuple values
        index = (x[0] for x in cosine_similarity_scores)
        scores = (x[1] for x in cosine_similarity_scores)    

        # Get the indices for the closest items
        recommendation_indices = [i[0] for i in cosine_similarity_scores]
        # Get the actutal recommendations
        recommendations = df['book_title'].iloc[recommendation_indices]
        return recommendations
    except:
        return "Book title not found"
    