import sys
import re

testfile_name = sys.argv[1]
outputfile_name = sys.argv[2]

read_data = []
hash_data = []
feature_base = {}


def read_data(filename, data_list):
    testfile = open(filename, 'r')
    for i in testfile:
        data_list.append(i.strip())
    testfile.close()
    return data_list


def add_hash(tweet):
    tweet = re.findall(u'\w+\d*', tweet)
    tweet = map(lambda x: "#"+x+"#", tweet)
    return tweet


def to_trigram(hash_tweet, _list):
    for cut in range(0, len(hash_tweet)-2):
        trigram = hash_tweet[cut:cut+3]
        _list.append(trigram)
    return _list


def to_trigrams(hash_tweets, _list):
    for hash_tweet in hash_tweets:
        to_trigram(hash_tweet, _list)
    return _list


def count_element(_list):
    result_dict = dict([(i, _list.count(i)) for i in set(_list)])
    return result_dict
