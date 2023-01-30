
def normalize_string(s):
    assert type(s) is str
    ###
    new_s = ""
    for letters in s:
        if letters.isspace() or letters.isalpha():
            new_s = new_s + letters.lower()
    return new_s


def get_normalized_words (s):
    assert type(s) is str
    ###
    new_s =  normalize_string(s).split()
    return new_s

def make_itemsets(words):
    for i in words:
        new_data = [set(i) for i in words]
    return new_data


make_itemsets(['sed', 'ut', 'perspiciatis', 'unde', 'omnis'])


from collections import defaultdict
from itertools import combinations  # Hint!
from collections import Counter

def update_pair_counts(pair_counts, itemset):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    assert type(pair_counts) is defaultdict
    for k, v in Counter(combinations(itemset, 2)):
        pair_counts[(k, v)] += 1
    for k, v in Counter(combinations(itemset, 2)):  # reverse order k and v add for combinations
        pair_counts[(v, k)] += 1


def update_item_counts(item_counts, itemset):
    ###
    for i in itemset:
        item_counts[i] += 1
        print(item_counts)


def filter_rules_by_conf (pair_counts, item_counts, threshold):
    rules = {} # (item_a, item_b) -> conf (item_a => item_b)
    prob_item1_threshold = int()
    for k,v in pair_counts:
        prob_item1_threshold = pair_counts[(k,v)] / item_counts[k]        # translate T[a,b] / C[a]
        if prob_item1_threshold >= threshold:
            rules[k,v] = prob_item1_threshold
    return rules

from collections import defaultdict
def find_assoc_rules(receipts, threshold):
    ###
    pair_counts = defaultdict(int)
    item_counts = defaultdict(int)
    for itemset in receipts:
        print(itemset)
        update_pair_counts (pair_counts, itemset)
        update_item_counts(item_counts, itemset)
    rules = filter_rules_by_conf (pair_counts, item_counts, threshold)
    return rules



normalize_latin_words = get_normalized_words(latin_text)
latin_itemsets = make_itemsets(normalize_latin_words)
latin_rules = find_assoc_rules(latin_itemsets, 0.75)
# Inspect your result:
print_rules(latin_rules)
###

# Inspect your result:
print_rules(latin_rules)


def intersect_keys(d1, d2):
    assert type(d1) is dict or type(d1) is defaultdict
    assert type(d2) is dict or type(d2) is defaultdict
    data = {k: d1[k] for k in d1.keys() & d2.keys()}
    return data


#latin_text
normalize_latin_words = get_normalized_words(latin_text)
latin_itemsets = make_itemsets(normalize_latin_words)
latin_rules = find_assoc_rules(latin_itemsets, 0.75)

#english_text =
normalize_english_words = get_normalized_words(english_text)
english_itemsets = make_itemsets(normalize_english_words)
english_rules = find_assoc_rules(english_itemsets, 0.75)

#intersect_keys(d1, d2)

common_high_conf_rules = intersect_keys(latin_rules, english_rules)
print("High-confidence rules common to _lorem ipsum_ in Latin and English:")
print_rules(common_high_conf_rules)



normalize_grocery_string = normalize_string(groceries_file):
normalize_grocery_words = get_normalized_words(normalize_grocery_string)
itemset_grocery  = make_itemsets(normalize_grocery_words)
update_grocery_pair_item = update_pair_counts(pair_counts, itemset_grocery)


filter_rules_by_conf (pair_counts, item_counts, threshold):
find_assoc_rules(receipts, threshold,MINN_COUNT):