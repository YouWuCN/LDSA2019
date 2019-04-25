import sys
import json 

def read_input(fl):
    for line in fl:
        if line != "\n" and "retweeted_status" not in line:
            d = json.loads(line)
           # if "retweeted_status" not in d:
            d = d["text"]
            yield d.split(" ")

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        pronoun = ["han","hon","den","det","denna","denne","hen"] 
        for word in words:
            word = word.lower()
            if word in pronoun:
                pronoun.remove(word)
                print('%s%s%d' % (word, separator, 1))

if __name__ == "__main__":
    main()


