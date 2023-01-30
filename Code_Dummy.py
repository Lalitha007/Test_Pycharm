from collections import defaultdict
import itertools


def normalize_string_groc(s):
    assert type(s) is str
    import string as st
    s = s.lower()
    return s


def extract_list(lst):
    lst_n = normalize_string_groc(lst)
    groc_list = [line.split(',') for line in lst_n.split("\n")]
    # list_groc_lists = []
    # for lst in groc_list:
    # sub = lst.split(', ')
    #    [list_groc_lists.append(sub)]
    # return list_groc_lists
    return groc_list


def update_item_counts_groc(item_counts_groc, itemlist):
    assert type(item_counts_groc) is defaultdict
    for i in itemlist:
        item_counts_groc[i] += 1


def update_pair_counts_groc(pair_counts_groc, itemlist):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    assert type(pair_counts_groc) is defaultdict
    for a, b in itertools.combinations(itemlist, 2):
        pair_counts_groc[(a, b)] += 1
        pair_counts_groc[(b, a)] += 1

def groc_filter_rules_by_conf (pair_counts_groc, item_counts_groc, threshold):
    rules_groc = {} # (item_a, item_b) -> conf (item_a => item_b)
    for a, b in pair_counts_groc.items():
        if a in item_counts_groc:
            conf_groc = pair_counts_groc[a, b] / item_counts_groc[a]
            if conf_groc >= threshold:
                rules_groc [(a, b)] = conf_groc
    return rules_groc

def groc_find_assoc_rules(receipts, THRESHOLD, MIN_COUNT):
    item_counts_groc = defaultdict(int)
    pair_counts_groc = defaultdict(int)
    for item in receipts:
        update_item_counts_groc(item_counts_groc, item)
        update_pair_counts_groc(pair_counts_groc, item)
    item_counts_groc = {a: b for a, b in item_counts.items() if b > MIN_COUNT}
    rules_groc2 = groc_filter_rules_by_conf(pair_counts_groc, item_counts_groc, THRESHOLD)
    return rules_groc2

### YOUR CODE HERE

groc_list = extract_list(groceries_file)

basket_rules = groc_find_assoc_rules(groc_list, THRESHOLD, MIN_COUNT)