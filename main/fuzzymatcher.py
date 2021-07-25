from fuzzywuzzy import fuzz
from fuzzywuzzy import process


class FuzzyMatcher:
    # master_dict = {
    #                'key1': {'value1': value1},
    #                'key2': {'value2': value2},
    #                 ...
    #               }
    def __init__(self, master_dict):
        self.master = master_dict
        self.master_keys = list(master_dict.keys())

    def get_master(self, master_key):
        return self.master[master_key]

    def match_one(self, query_str, limit=3):
        matches = process.extract(query_str, self.master_keys, limit=limit)
        return [match[0] for match in matches] # スコア除去

    def match_all(self, query_str_list, limit=3):
        result = {}
        for query_str in query_str_list:
            matches = self.match_one(query_str, limit)
            result[query_str] = matches
        return result