import sys
import json

REVIEWS = {}


def main():

    if len(sys.argv) != 2:
        print 'USAGE: python preprocessor.py <dir to yelp files>'
        sys.exit(0)

    # open the business file to get all restaurants
    with open(sys.argv[1] + '/yelp_academic_dataset_business.json') as f:
        for line in f:
            data = json.loads(line)
            if 'Restaurants' in data['categories']:
                REVIEWS[data['business_id']] = {'name': data['name'], 'reviews': []}

    # read reviews
    with open(sys.argv[1] + '/yelp_academic_dataset_review.json') as f:
        for line in f:
            data = json.loads(line)
            if data['business_id'] in REVIEWS:
                review = {'score': data['stars'], 'text': data['text']}
                REVIEWS[data['business_id']]['reviews'].append(review)

    # write to output files
    print 'Dumping to files...'
    for key, value in REVIEWS.iteritems():
        with open(key + ".json", 'w') as f:
            json.dump(value, f)
            print 'File dumped ' + key


if __name__ == "__main__":
    main()
