

def parse_csv(f):
    word_freq = {}

    for line in f:
        line = line.strip()
        csv_parsed = line.split(',')

        word = csv_parsed[0]
        freq = int(csv_parsed[1])

        word_freq[word] = freq

    return word_freq
