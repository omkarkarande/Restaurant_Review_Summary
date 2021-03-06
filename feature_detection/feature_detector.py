import sys
import os
import nltk
import operator

# token dictionaries
FOOD = []
AMBIENCE = []
SERVICE = []
PRICE = []

# detection threshold
THRESHOLD = 4.0
# review dictionary
REVIEW_DATA = {}


def getType(sentence):	
    TYPE = {'FOOD': 0, 'SERVICE': 0, 'AMBIENCE': 0, 'PRICE': 0}
    # tokenize the sentence
    tokens = nltk.word_tokenize(sentence)
    for token in tokens:
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
    sorted_types = sorted(TYPE.items(), key=operator.itemgetter(1), reverse=True)
    sentype = []

    if sorted_types[0][1] == 0 and sorted_types[1][1] == 0 and sorted_types[2][1] == 0 and sorted_types[3][1] == 0:
        return None
    else:
        # add first item to sorted type
        sentype.append(sorted_types[0][0])
        # add second item if it lies within THRESHOLD / 2 of first
        if sorted_types[1][1] != 0 and sorted_types[0][1] - sorted_types[1][1] <= THRESHOLD / 2.0:
            sentype.append(sorted_types[1][0])
        # add second item if it lies within THRESHOLD / 3 of first
        if sorted_types[2][1] != 0 and sorted_types[0][1] - sorted_types[2][1] <= THRESHOLD / 3.0:
            sentype.append(sorted_types[2][0])
        # add second item if it lies within THRESHOLD / 4 of first
        if sorted_types[3][1] != 0 and sorted_types[0][1] - sorted_types[3][1] <= THRESHOLD / 4.0:
            sentype.append(sorted_types[3][0])

        return sentype


def main():

    global FOOD, AMBIENCE, SERVICE, PRICE
    if len(sys.argv) != 3:
        print "USAGE: python feature_detector.py <model file> <path to sentence sentiment dir>"
        sys.exit(0)

    # read the model to get tokens
    with open(sys.argv[1], 'r') as f:

        FOOD = f.readline().strip().split(', ')
        FOOD = [i.decode('UTF-8') for i in FOOD]
        AMBIENCE = f.readline().strip().split(', ')
        AMBIENCE = [i.decode('UTF-8') for i in AMBIENCE]
        SERVICE = f.readline().strip().split(', ')
        SERVICE = [i.decode('UTF-8') for i in SERVICE]
        PRICE = f.readline().strip().split(', ')
        PRICE = [i.decode('UTF-8') for i in PRICE]

    # read the sentiment files
    for root, _, files in os.walk(sys.argv[2]):
        # for every file
        for sentiment_file in files:
            key = sentiment_file[:len(sentiment_file) - 5]
            if key not in REVIEW_DATA:
                REVIEW_DATA[key] = {'FOOD': 0.0, 'SERVICE': 0.0, 'AMBIENCE': 0.0, 'PRICE': 0.0}

            # open the file and read the contents into a list
            with open(root + '/' + sentiment_file) as f:
                sentences = eval(f.read())
                N = len(sentences)
                if N == 0:
                    continue
                # for each sentence detect what the reviewer is talking about
                for item in sentences:
                    sentence_type = getType(item[1])
                    if sentence_type is not None:
                        for feat_type in sentence_type:
                            REVIEW_DATA[key][feat_type] += item[0] / float(len(sentence_type))

                # normalize the data
                print 'RESTAURANT ID: ' + key
                for category, value in REVIEW_DATA[key].iteritems():
                    REVIEW_DATA[key][category] = value / N
                    print category + ": " + str(REVIEW_DATA[key][category])
                print ''

    return

if __name__ == "__main__":
    main()
