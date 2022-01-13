file_out = open('resulting_data.csv','w')
file_in = open('twitter_data.csv')
positive_words = open('positive_words.txt')
negative_words = open('negative_words.txt')

positives = []
negatives = []

for line in positive_words:
    line = line.strip()
    positives.append(line)

for line in negative_words:
    line = line.strip()
    negatives.append(line)


header = "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score"
file_out.write(header)
file_out.write('\n')

def strip_punctuation(word):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for letter in punctuation_chars:
        if letter in word:
            word = word.replace(letter,"")
    return word

def countPos(string):
    count = 0
    for word in string.split():
        word = strip_punctuation(word)
        word = word.lower()
        if word in positives:
            count+=1
    return count

def countNeg(string):
    count = 0
    for word in string.split():
        word = strip_punctuation(word)
        word = word.lower()
        if word in negatives:
            count += 1
    return count

for line in file_in:
    line = line.strip()
    if line.startswith('tweet_text'):
        continue
    data = line.split(',')
    retweet_count = data[1]
    reply_count = data[2]
    numPositives = countPos(data[0])
    numNegatives = countNeg(data[0])
    netScore = numPositives - numNegatives
    string = '{},{},{},{},{}'.format(retweet_count, reply_count, numPositives, numNegatives, netScore)
    file_out.write(string)
    file_out.write('\n')

file_out.close()
file_in.close()
