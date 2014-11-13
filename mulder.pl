#!/usr/bin/perl -w
use strict;

my @noun = split(", ", "the truth, men in power, lies, extraterrestrials");
my @linking = split(", ", "is, has become, will be, is revealed to be");



my $i;
while ($i++ < 100){

my @sentence;

push @sentence, pick_ary(\@noun);
push @sentence, pick_ary(\@linking);
push @sentence, pick_ary(\@noun);
print join(" ", @sentence) . ".\n";


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
