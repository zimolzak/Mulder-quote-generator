#!/usr/bin/env python

Number_Of_Sentences_To_Generate = 20

def file2array(filename):
    f = open(filename, 'r')
    a = []
    for line in f:
        a.append(line)
    f.close()
    return a

nouns = file2array('nouns.txt')

print ' '.join(nouns)

# nf = open('nouns.txt', 'r')
# vf = open('verbs.txt', 'r')
# cf = open('conjunctions.txt', 'r')

# nf.close()


# my @nouns = file2array("nouns.txt");
# my @verbs = file2array("verbs.txt");
# my @conjunctions = file2array("conjunctions.txt");
