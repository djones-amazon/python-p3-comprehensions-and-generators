#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [n for n in num_list if (n % 2) == 0]
    if len(even_list) == 0:
        return list()
    else:
        return even_list
def make_exclamation(sentence_list):
    exclaim_added = [sentence + "!" for sentence in sentence_list]
    if len(sentence_list) == 0:
        return list()
    else:
        return exclaim_added