#!/usr/bin/perl -w
use strict;

my @noun = split(", ", "the truth, men in power, lies, extraterrestrials");
my @linking = split(", ", "is, has become, will be, is revealed to be");
my @conj = split(", ", "and, but, while, if, so, whereas, even if, even though, although, only if, whenever, anywhere that");



my $i;
while ($i++ < 100){

print join("", multi_clause(\@noun, \@linking)) . ".\n";

}

sub multi_clause {
    my $nr = shift;
    my $lr = shift;
    my $n = pick_a_num(1,3);
    my @sentence;
    for(1..$n){
	push @sentence, clause($nr, $lr);
	push @sentence, ", ", "but", " " if $_ < $n;
    }
    return @sentence;
}

sub clause {
    my @noun = @{shift()};
    my @linking = @{shift()};
    my @sentence;
    push @sentence, pick_ary(\@noun), " ";
    push @sentence, pick_ary(\@linking), " ";
    push @sentence, pick_ary(\@noun);
    return @sentence;
}

sub pick_ary {
    my @a = @{shift()};
    return $a[pick_a_num(0,$#a)];
}

sub pick_a_num {
    my $from = shift;
    my $to = shift;
    return int(rand($to + 1 - $from)) + $from;
}
