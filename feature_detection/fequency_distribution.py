import sys
import operator


def main():

    if len(sys.argv) != 2:
        print "USAGE: python frequency_distribution.py <path to file>"
        sys.exit(0)

    distribution = {}
    with open(sys.argv[1], 'r') as f:
        data = eval(f.read())
        for item in data:
            if item[1] not in distribution:
                distribution[item[1]] = 1
            else:
                distribution[item[1]] += 1

    sorted_distribution = sorted(distribution.items(), key=operator.itemgetter(0))
    op_file = open('freq_distribution', 'w')
    for item in sorted_distribution:
        op_file.write(str(item)[1:len(str(item)) - 1] + '\n')
    op_file.close()
    return


if __name__ == "__main__":
    main()
