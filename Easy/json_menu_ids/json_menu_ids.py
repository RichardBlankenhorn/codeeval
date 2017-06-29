import sys
import json

def dict_search(d):
    for k,v in d.items():
        if k == "label":
            label_nums.append(v.split().pop())
        if isinstance(v,dict):
            dict_search(v)
        elif isinstance(v,list):
            list_search(v)

def list_search(l):
    for item in l:
        if isinstance(item,dict):
            dict_search(item)

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        json_string = json.loads(test.rstrip('\n'))
        label_nums = []
        dict_search(json_string)
        label_nums = map(int, label_nums)
        print str(sum(label_nums))
