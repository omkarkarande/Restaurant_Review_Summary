import sys


def main():

    if len(sys.argv) != 3:
        print "USAGE: python frequency_distribution.py <path to label file> <path to word freq file>"
        sys.exit(0)

    FOOD = []
    AMBIENCE = []
    SERVICE = []
    PRICE = []
    three_letter_words = ['vat', 'sec', 'kfc', 'bug', 'gym', 'gin', 'veg', 'rye', 'tax', 'pan', 'fry', 'soy', 'raw',
                          'pub', 'sub', 'ham', 'bun', 'pie', 'oil', 'tip', 'rib', 'mac', 'pho', 'tea', 'bbq', 'ice', 'egg', 'bar']
    with open(sys.argv[1], 'r') as f:
        FOOD = f.readline().strip().split(', ')
        AMBIENCE = f.readline().strip().split(', ')
        SERVICE = f.readline().strip().split(', ')
        PRICE = f.readline().strip().split(', ')

    # tag the freq words
    FREQ = []
    with open(sys.argv[2], 'r') as f:
        FREQ = eval(f.read())

    LABELLED = []
    for item in FREQ:
        # skip less frequent ones
        if item[1] < 100 or len(item[0]) <= 2:
            continue

        if len(item[0]) == 3:
            goahead = 0
            for exclusion in three_letter_words:
                if item[0] == exclusion:
                    goahead = 1
                    break
            if goahead == 0:
                continue

        word = item[0]
        categories = []
        # check if FOOD
        for food in FOOD:
            if word.startswith(food):
                categories.append('F')
                break
        # check for AMBIENCE
        for amb in AMBIENCE:
            if word.startswith(amb):
                categories.append('A')
                break
        # check for SERVICE
        for service in SERVICE:
            if word.startswith(service):
                categories.append('S')
                break
        # check for PRICE
        for price in PRICE:
            if word.startswith(price):
                categories.append('P')
                break
        LABELLED.append((item[0], item[1], categories))

    # dump LABELLED ITEMS TO A FILE
    samples = [LABELLED[i::4] for i in range(4)]
    i = 1
    for sample in samples:
        with open('labelled_categories_' + str(i), 'w') as f:
            for item in sample:
                f.write(str(item) + '\n')
        i += 1
    return


if __name__ == "__main__":
    main()
