import sys
import os
import json
import operator
import pprint

from spacy.en import English, LOCAL_DATA_DIR
data_dir = os.environ.get('SPACY_DATA', LOCAL_DATA_DIR)
nlp = English(data_dir=data_dir)

NOUNS = {}


def extract_features(data):
    for review in data['reviews']:
        doc = nlp(review['text'])
        for chunk in doc.noun_chunks:
            words = str(chunk).lower().split()
            for word in words:
                if word not in NOUNS:
                    NOUNS[word] = 1
                else:
                    NOUNS[word] += 1


def main():
    if len(sys.argv) != 2:
        print 'USAGE: python features.py <path to reviews folder>'
        sys.exit(0)

    for root, _, files in os.walk(sys.argv[1]):
        file_count = 1
        for review_file in files:
            with open(root + '/' + review_file, 'r') as f:
                data = json.load(f)
                extract_features(data)
                # pprint.pprint(sentences)
            file_count += 1

    sorted_toks = sorted(NOUNS.items(), key=operator.itemgetter(1))
    pprint.pprint(sorted_toks)

    return

if __name__ == "__main__":
    main()
