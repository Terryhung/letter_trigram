import sys
import re
import numpy as np


class trigram:
    def __init__(self, tweet):
        self.tweet = tweet
        self._list = []

    def add_hash(self, tweet):
        # claen tweet by reg
        tweet = re.findall(u'\w+\d*', tweet)
        tweet = map(lambda x: "#"+x+"#", tweet)
        return tweet

    def to_trigram(self, hash_tweet, _list):
        for cut in range(0, len(hash_tweet)-2):
            trigram = hash_tweet[cut:cut+3]
            _list.append(trigram)
        return _list

    def to_trigrams(self, hash_tweets, _list):
        for hash_tweet in hash_tweets:
            self.to_trigram(hash_tweet, _list)
        return _list

    def count_element(self, _list):
        result_dict = dict([(i, _list.count(i)) for i in set(_list)])
        return result_dict

    def result(self):
        _list = self.to_trigrams(self.add_hash(self.tweet), self._list)
        return self.count_element(_list)


class _dic(trigram):
    def result(self):
        _list = self.to_trigrams(self.add_hash(self.tweet), self._list)
        return self.count_element(_list).keys()


def read_data(filename):
    data_list = []
    testfile = open(filename, 'r')
    for i in testfile:
        data_list.append(i.strip())
    testfile.close()
    return data_list


def build_dic(tweets, filename):
    _list = []
    for tweet in tweets:
        _list = _list + _dic(tweet).result()
        _list = list(set(_list))
    np.save(filename, np.asarray(_list))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: python trigram.py file_name output_file_name"
        sys.exit()
    testfile_name = sys.argv[1]
    outputfile_name = sys.argv[2]
    build_dic(read_data(testfile_name), outputfile_name)
