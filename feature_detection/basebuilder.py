import sys
import os


FOOD = []
AMBIENCE = []
SERVICE = []
PRICE = []


def main():
    if len(sys.argv) != 2:
        print "USAGE: python basebuilder.py <path to labels folder>"
        sys.exit(0)

    for root, _, files in os.walk(sys.argv[1]):
        for feat_file in files:
            print 'processing ' + feat_file
            with open(root + '/' + feat_file) as f:
                for line in f:
                    item = eval(line)
                    for category in item[2]:
                        if category == 'F':
                            FOOD.append(item[0])
                        if category == 'S':
                            SERVICE.append(item[0])
                        if category == 'A':
                            AMBIENCE.append(item[0])
                        if category == 'P':
                            PRICE.append(item[0])

    # dump the data to model file
    model = open('features.model', 'w')
    model.write(', '.join(map(str, FOOD)) + '\n')
    model.write(', '.join(map(str, AMBIENCE)) + '\n')
    model.write(', '.join(map(str, SERVICE)) + '\n')
    model.write(', '.join(map(str, PRICE)) + '\n')
    model.close()
    return
if __name__ == "__main__":
    main()
