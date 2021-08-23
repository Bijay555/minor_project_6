import yaml
import logging
import pandas as pd
from src.tfidf import tf_idf_compute
from src.cosine_similarity import cos_sim
from src.text_recommendation import get_recom_text

with open("config.yaml", "r") as stream:
    config_file_instance = yaml.safe_load(stream)


if __name__ == "__main__":

    df = pd.read_csv(config_file_instance["book_dataset"])
    logging.info(df.head(10))
    tf_idf_mat = tf_idf_compute(list(df['book_title']))
    cosine_sim = cos_sim(tf_idf_mat)
    target_book = input('Enter the book name: ')
    recommend_books = get_recom_text(df,target_book,cosine_sim)
    print("Similar books are:\n", recommend_books)

