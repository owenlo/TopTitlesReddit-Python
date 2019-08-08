import praw
import re
import sys

# See https://praw.readthedocs.io/en/latest/getting_started/authentication.html for usage of praw lib
reddit = praw.Reddit(client_id='xxxx', \
                     client_secret='xxxx', \
                     user_agent='xxxx', \
                     username='xxxx', \
                     password='xxxx')

if len(sys.argv) > 1 :
    sub_reddit = sys.argv[1]
else:
    sub_reddit = 'worldnews' #We default to the worldnews subreddit if no argument is provided

subreddit = reddit.subreddit(sub_reddit)
resp = subreddit.top(limit=1000)

key_words = {}
common_words = {}

# The common.csv file contains a list 100+ common words which are to be filtered out from finals results (e.g. the, and, a etc)
# List was orignally derived from https://simple.wikipedia.org/wiki/Most_common_words_in_English#Top_100_words
f = open("common.csv", "r",  encoding='utf-8-sig')
for x in f:
  common_words[x.lower().rstrip("\n\r")] = 0

for submission in resp:
    for word in submission.title.split():
        word = ''.join([char for char in word if char.isalpha()]).lower() #Source: https://stackoverflow.com/a/21446722
        
        if word != '' and word not in common_words:
            if word not in key_words:
                key_words[word] = 1
            else:
                key_words[word] += 1

sort = sorted(key_words.items(), key=lambda x: x[1], reverse=True) #Source: https://stackoverflow.com/a/2258273

for i in range(0, 20):
    print(sort[i])
