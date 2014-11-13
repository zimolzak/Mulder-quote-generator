#!/usr/bin/perl -w
use strict;

my @noun = split(", ", "the truth, a man in power, a lie, an extraterrestrial");
my @linking = split(", ", "is, has become, will be, is revealed to be");
my @conj = split(", ", "and, but, while, if, so, whereas, even if, even though, although, only if, whenever, anywhere that");

for (1..100){
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
