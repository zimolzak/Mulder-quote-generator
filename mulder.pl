#!/usr/bin/perl -w

# original model:

# I have been with a faith. But that faith was a lie, but even so, is
# the lie really more believable than my faith in that very lie? Or is
# it even the truth?

use strict;

my @noun = split(", ", "the truth, a man in power, a lie, an extraterrestrial, the existence of extraterrestrial life, the greatest of lies, my belief, my faith, my singular quest for the truth, my faith in the truth, life on this planet, a vast government conspiracy, this coverup, someone who reveals the truth");
my @linking = split(", ", "is, has become, will be, is revealed to be, will never be, will never come close to, has hidden, has conspired against, is more believable than, was, is truly, cannot acknowledge");
my @conj = split(", ", "and, but, while, if, so, whereas, even if, even though, although, only if, whenever, anywhere that, but still, as long as, until");

for (1..20){
    $_ = join("", multi_clause(\@noun, \@conj, \@linking)) . ".\n";
    s/^(.)(.*)/\U$1\E$2/;
    print;
}

sub multi_clause {
    # noun ref, conj ref, link ref = ary
    my $nr = shift;
    my @conj = @{shift()};
    my $lr = shift;
    my $n = pick_a_num(1,3);
    my @sentence;
    for(1..$n){
	push @sentence, clause($nr, $lr);
	push @sentence, ", ", pick_ary(\@conj), " " if $_ < $n;
    }
    return @sentence;
}

sub clause {
    # noun ref, link ref = ary
    my @noun = @{shift()};
    my @linking = @{shift()};
    my @sentence;
    push @sentence, pick_ary(\@noun), " ";
    push @sentence, pick_ary(\@linking), " ";
    push @sentence, pick_ary(\@noun);
    return @sentence;
}

sub pick_ary {
    # ary ref = element
    my @a = @{shift()};
    return $a[pick_a_num(0,$#a)];
}

sub pick_a_num {
    # from, to = int
    my $from = shift;
    my $to = shift;
    return int(rand($to + 1 - $from)) + $from;
}
