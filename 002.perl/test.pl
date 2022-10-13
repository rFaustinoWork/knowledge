#!/usr/bin/perl
use strict;
use warnings;

my $str = "Just a test string";
print(length($str));

my @ar = split('', $str);

sub printData
{
    print("DataData\n");
}

sub tst
{
    my $met = shift;
    &$met();
}

for $a(@ar){
    print("$a\n");
}

printData();
tst(\&printData)

