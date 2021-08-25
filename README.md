# minor_project_6

Text-based content recommendation system using tf-Idf on book title dataset.

Objective:

+ To create tf-idf matrix from the text book dataset.
+ To compute cosine similarity
+ To build a recommendation system model that can recommend other similar books based on given user target book.

In this project, we have used TF-IDF and cosine similarity as a ML model (NLP)

TF-IDF stands for “Term Frequency — Inverse Document Frequency”. This is a technique to quantify a word in documents, we generally compute a weight to each word which signifies the importance of the word in the document and corpus.

### Project Structure
```
|
│   .gitignore
│   config.yaml
│   main.py
│   Pipfile
│   Pipfile.lock
│   README.md
│
├───src
│       cosine_similarity.py
│       text_recommendation.py
│       tfidf.py
│
└───txt_dataset
        book_title.csv
   ```

Folders/files Description:

1. src
+ Contains the tf-idf.py which outputs the tfidf matrix (numeric representation of text data).
+ Contains the cosine_similarity.py to compute the similarity score between texts.
+ Contains the text_recommendation.py to build content recommendations  of 5 other books similar to the target book

2. main.py
the main.py file that calls the other functions py file to perform word embedding,calculate similarity and recommend other books based on users input.

4. Config.yaml
has global variables, data paths and dictionaries

Dataset:
Contains 2 columns : 
+ id: unique code of books
+ book_title: the name of the book
The dataset is a custom webscapped dataset that contains 50  ML books name.
Dataset: https://drive.google.com/file/d/1GABD_LnT-ZCm373gpLXJLJAEJKE4bdjI/view?usp=sharing


How to run this repository:
Pre-requisits: Install pipenv(sudo apt-get pipenv)

Step 1: Setup
Clone the repository.
pipenv shell
setup the folder

Step 2: Run for py file
Run "python main.py"

Output:
Recommend 5 books that has higher similarity score
