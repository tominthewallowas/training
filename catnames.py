#!/usr/bin/env python3

'''
Simple python program to learn about Git and GitHub.
'''

import cat_facts

def determine_cat_names():
    cat_names = ('Tippi', 'Kse', 'Lilee')
    return cat_names

def collect_cat_facts(name=None):
    return cat_facts.cat_facts[name]

if __name__ == '__main__':
    cat_names = determine_cat_names()
    for cat_name in cat_names:
        print(cat_name)

    for cat_name in cat_names:
        cat_info = collect_cat_facts(cat_name)
        for info in cat_info:
            print(info)