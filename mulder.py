#!/usr/bin/env python
import random
import sys
Number_Of_Sentences_To_Generate = 200
nouns = open('nouns.txt', 'r').read().splitlines()
verbs = open('verbs.txt', 'r').read().splitlines()
conjunctions = open('conjunctions.txt', 'r').read().splitlines()
twitter = False

for arg in sys.argv:
    if arg == '--count':
        n = len(nouns)
        c = len(conjunctions)
        v = len(verbs)
        total = ((n ** 6 * v ** 3 * c ** 2)
                 + (n ** 4 * v ** 2 * c)
                 + (n ** 2 * v))
        print '%e possible 1- 2- and 3-clause sentences.' % total
        quit()
    if arg == '--twitter':
        twitter = True

def generate_sentence(nouns, conjunctions, verbs):
    max_clauses = 3
    num_clauses = random.randrange(max_clauses) + 1
    sentence = []
    for i in range(num_clauses):
        sentence += [random.choice(nouns), " ",
                     random.choice(verbs), " ",
                     random.choice(nouns)]
        if i < (num_clauses - 1):
            sentence += [", ", random.choice(conjunctions), " "]
    return sentence

i = 0
while i < Number_Of_Sentences_To_Generate:
    sentence = ''.join(generate_sentence(nouns, conjunctions, verbs)) + ".\n"
    sentence = sentence[0].capitalize() + sentence[1:]
    if twitter:
        sentence = sentence[:-1] + " #thexfiles\n"
    if ( (twitter and len(sentence) < 140) or not twitter):
        print sentence
        i += 1
