#!/usr/bin/perl -w

# original model:

# I have been with a faith. But that faith was a lie, but even so, is
# the lie really more believable than my faith in that very lie? Or is
# it even the truth?

use strict;

my $Number_Of_Sentences_To_Generate = 20;

my @nouns = split_heredoc(", ", <<EOF);

the truth, a man in power, a lie, an extraterrestrial, the existence
of extraterrestrial life, the greatest of lies, my belief, my faith,
my singular quest for the truth, my faith in the truth, life on this
planet, a vast government conspiracy, this coverup, someone who
reveals the truth, Agent Scully

EOF

my @verbs = split_heredoc(", ", <<EOF);

is, has become, will be, is revealed to be, will never be, will never
come close to, has hidden, has conspired against, is more believable
than, was, is truly, cannot acknowledge, denies, can no longer avoid,
will be confronted by, is not, believes in, contradicts, can overcome,
knows of

EOF

my @conjunctions = split_heredoc(", ", <<EOF);

and, but, while, if, so, whereas, even if, even though, although, only
if, whenever, anywhere that, but still, as long as, until

EOF

for (1..$Number_Of_Sentences_To_Generate){
    $_ = join("", generate_sentence(\@nouns, \@conjunctions, \@verbs))
	. ".\n\n";
    s/^(.)(.*)/\U$1\E$2/; # upper case the first letter
    print;
}

sub generate_sentence {
    # A sentence is: Clause-Conjunction-Clause-Conjunction-...
    my $noun_ref = shift;
    my $conj_ref = shift;
    my $verb_ref = shift;
    my $max_clauses = 3;
    my $num_clauses = rand_int(1, $max_clauses);
    my @sentence;
    for(1..$num_clauses){
	push @sentence, clause($noun_ref, $verb_ref);
	push @sentence, ", ", rand_element($conj_ref), " "
	    if $_ < $num_clauses;
    }
    return @sentence;
}

sub clause {
    # A clause is: Noun-Verb-Noun
    my $noun_ref = shift;
    my $verb_ref = shift;
    my @clause;
    push @clause, rand_element($noun_ref), " ";
    push @clause, rand_element($verb_ref), " ";
    push @clause, rand_element($noun_ref);
    return @clause;
}

sub rand_element {
    my @a = @{shift()};
    return $a[rand_int(0,$#a)];
}

sub rand_int {
    my $from = shift;
    my $to = shift;
    return int(rand($to + 1 - $from)) + $from;
}

sub split_heredoc {
    my $pattern = shift;
    my $text = shift;
    $text =~s/^\s*//; # remove leading whitespace
    $text =~s/\s*$//; # remove trailing whitespace
    $text =~ s/\n/ /g;
    return split(/$pattern/, $text);
}
