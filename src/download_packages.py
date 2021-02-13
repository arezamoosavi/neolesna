import nltk

try:
    nltk.download("stopwords")
    nltk.download("punkt")
    print("downloaded!")
except Exception as e:
    print(str(e))
