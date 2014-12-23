#!/usr/bin/env python
import random
Number_Of_Sentences_To_Generate = 20
nouns = open('nouns.txt', 'r').read().splitlines()
verbs = open('verbs.txt', 'r').read().splitlines()
conjunctions = open('conjunctions.txt', 'r').read().splitlines()

def clause(nouns, verbs):
    return [random.choice(nouns), " ", random.choice(verbs), " ", random.choice(nouns)]

def generate_sentence(nouns, conjunctions, verbs):
    max_clauses = 3
    num_clauses = random.randrange(max_clauses) + 1
    sentence = []
    for i in range(num_clauses):
        sentence += clause(nouns, verbs)
        if i < (num_clauses - 1):
            sentence += [", ", random.choice(conjunctions), " "]
    return sentence

for i in range(Number_Of_Sentences_To_Generate):
    print (''.join(generate_sentence(nouns, conjunctions, verbs)) + "\n").capitalize()
