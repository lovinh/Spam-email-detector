import numpy as np
import pandas as pd
import sys
import os
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import pickle
import sklearn
from sklearn.svm import LinearSVC
from UI import MainActivity
from model import text_preprocessing, Model_Predict


class App:
    def __init__(self):
        self.GUI = MainActivity()

    def run(self):
        self.GUI.run()
