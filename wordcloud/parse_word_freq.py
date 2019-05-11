

def parse_csv(filename):
    word_freq = {}

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            csv_parsed = line.split(',')

            word = csv_parsed[0]
            freq = csv_parsed[1]

            word_freq[word] = freq

    return word_freq

wf = parse_csv("/home/hanbinsock/output/will-eternal-chapter-0001-word-count/part-00000-d433bb1c-451e-4c4f-8acf-659081634e7a-c000.csv")
print(wf)
