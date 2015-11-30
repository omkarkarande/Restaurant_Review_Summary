import sys
import json
import os
import codecs
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

DIFF_THRESHOLD = 0.2

if len(sys.argv) != 2:
    print 'USAGE: python preprocessor.py <dir to yelp files>'
    sys.exit(0)

directory_reviews = os.path.dirname('review_sentiments/')
os.makedirs(directory_reviews)

for root, dirs, files in os.walk(sys.argv[1]):
    file_count = 1
    for review_file in files:
        with open(root + '/' + review_file) as inf:
            print "Processing file " + str(file_count) + " - " + review_file + "..."
            outf = codecs.open(
                'review_sentiments/' + review_file.split('.')[0] + '.txt', 'w', encoding="utf-8")
            sentence_sentiment = []

            for line in inf:
                data = json.loads(line)
                for review in data['reviews']:

                    score = review['score']
                    normalized_score = (float(score) - 3.0) / 2.0
                    # print "Overall Review Rating in Stars:" + str(score)
                    # extract text from the review
                    text = review['text']
                    # split the text of the review into small sentences
                    sentences = tokenize.sent_tokenize(text)

                    # get the polariity of the sentences
                    vader_analyzer = SentimentIntensityAnalyzer()

                    for sentence in sentences:
                        # print(sentence)

                        # print(vader_analyzer.polarity_scores(sentence))
                        # break
                        senti = vader_analyzer.polarity_scores(
                            sentence.strip())
                        if(abs(senti['pos'] - senti['neg']) > DIFF_THRESHOLD):
                            sentence_score = (
                                (senti['pos'] - senti['neg']) + normalized_score) / 2.0
                            sentence_sentiment.append(
                                (sentence_score, sentence))
                outf.write(str(sentence_sentiment))
                outf.close()
        file_count += 1
