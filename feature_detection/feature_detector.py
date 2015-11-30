import sys
import os
import nltk
import operator

# token dictionaries
FOOD = []
AMBIENCE = []
SERVICE = []
PRICE = []

# review dictionary
REVIEW_DATA = {}


def getType(sentence):
    TYPE = {'FOOD': 0, 'SERVICE': 0, 'AMBIENCE': 0, 'PRICE': 0}

    # tokenize the sentence
    tokens = nltk.word_tokenize(sentence)
    for token in tokens:
        print token
        # check for the features
        if token in FOOD:
            TYPE['FOOD'] += 1
        if token in AMBIENCE:
            TYPE['AMBIENCE'] += 1
        if token in SERVICE:
            TYPE['SERVICE'] += 1
        if token in PRICE:
            TYPE['PRICE'] += 1

    # sort the type based on frequency
    sorted_types = sorted(TYPE.items(), key=operator.itemgetter(1))
    sentype = []
    for item in sorted_types:
        print item
    return sentype


def main():

    global FOOD, AMBIENCE, SERVICE, PRICE
    if len(sys.argv) != 3:
        print "USAGE: python feature_detector.py <model file> <path to sentence sentiment dir>"
        sys.exit(0)

    # read the model to get tokens
    with open(sys.argv[1], 'r') as f:

        FOOD = f.readline().strip().split()
        AMBIENCE = f.readline().strip().split()
        SERVICE = f.readline().strip().split()
        PRICE = f.readline().strip().split()

    # read the sentiment files
    for root, _, files in os.walk(sys.argv[2]):
        # for every file
        for sentiment_file in files:
            key = sentiment_file[:len(sentiment_file) - 50]
            if key not in REVIEW_DATA:
                REVIEW_DATA[key] = {
                    'FOOD': 0.0, 'SERVICE': 0.0, 'AMBIENCE': 0.0, 'PRICE': 0.0}

            # open the file and read the contents into a list
            with open(root + '/' + sentiment_file) as f:
                sentences = eval(f.read())
                N = len(sentences)
                # for each sentence detect what the reviewer is talking about
                for item in sentences:
                    sentence_type = getType(item[1])

    return

if __name__ == "__main__":
    main()
