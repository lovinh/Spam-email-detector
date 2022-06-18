from xml.dom.minidom import Text
import numpy as np
import pandas as pd
import nltk
import sys
import os
import sklearn
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from app import App


def main():
    app = App()
    app.run()


main()
