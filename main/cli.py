import json
from .fuzzymatcher import FuzzyMatcher

def cli():
    master = {
        'master_key1': {'value1': 'Value1'},
        'master_key2': {'value2': 'Value2'},
        'master_key3': {'value3': 'Value3'},
    }

    src = {
        'src_key1': {'value1': 'Value1'},
        'src_key2': {'value2': 'Value2'},
        'src_key3': {'value3': 'Value3'},
    }

    src_str_list = list(src.keys())

    fm = FuzzyMatcher(master)

    result = fm.match_all(src_str_list)

    with open('./result.json', 'w') as f:
        json.dump(result, f)