import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import pickle
import sklearn
from sklearn.svm import LinearSVC


class CustomLemmatizer(WordNetLemmatizer):
    def extract_lemmatizer(self, text):
        lemma_text = [self.lemmatize(word) for word in text]
        return lemma_text


class text_preprocessing:
    def remove_punctuation(self, text):
        result_text = "".join(
            char for char in text if char not in string.punctuation)
        return result_text

    def lower_case(self, text):
        return text.lower()

    def tokenization(self, text):
        word_list = text.split(" ")
        token = list()
        for word in word_list:
            if word != "":
                token.append(word)
        return token

    def remove_stopword(self, token):
        # nltk.download('stopwords')
        stopword_eng_list = nltk.corpus.stopwords.words('english')
        stopword_vie_list = open(
            r"E:\Learn Machine Learning\Project\Spam Email Classifier\train\vietnamese-stopwords.txt", encoding="utf-8").read().split("\n")
        result = list()
        for word in token:
            if (word not in stopword_eng_list) and (word not in stopword_vie_list):
                result.append(word)
        return result

    def stemming(self, text):
        porter_stemmer = PorterStemmer()
        stem_text = [porter_stemmer.stem(word) for word in text]
        return stem_text

    def lemmatizer(self, text):
        # nltk.download('omw-1.4')
        # nltk.download('wordnet')
        cus_lemmatizer = CustomLemmatizer()
        return cus_lemmatizer.extract_lemmatizer(text)

    def tf_idf(self, vector):
        bag_of_word = pickle.load(open(
            r"E:\Learn Machine Learning\Project\Spam Email Classifier\program\word.txt", "rb"))
        idf_score = pickle.load(open(
            r"E:\Learn Machine Learning\Project\Spam Email Classifier\program\idf_score.out", "rb"))
        word_dict_list = dict.fromkeys(bag_of_word, 0)
        sample_dict_list = dict()
        for token in vector:
            try:
                word_dict_list[token] += 1
            except:
                continue
        result_vector = dict()
        total_word = len(vector)
        for keys in word_dict_list:
            result_vector[keys] = word_dict_list[keys] / float(total_word)

        tf_idf = list()
        for key in idf_score:
            tf_idf.append(result_vector[key] * idf_score[key])

        return tf_idf

    def fit_transform(self, text):
        return self.tf_idf(self.lemmatizer(self.remove_stopword(self.tokenization(self.lower_case(self.remove_punctuation(text))))))


class Model_Predict:
    def __init__(self):
        self.model = pickle.load(open(
            r"E:\Learn Machine Learning\Project\Spam Email Classifier\program\best_linear_svc_model.pkl", "rb"))

    def get_predict(self, sample):
        result = self.model.predict([sample])
        if result[0] == 0:
            return False
        else:
            return True
