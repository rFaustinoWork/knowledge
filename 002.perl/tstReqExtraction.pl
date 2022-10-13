#!/usr/bin/perl
use strict;
use warnings;


my $str = "/**
 * \@brief Just a comment
 * \@real{REQ-0015}
 * \@real{REQ-0002,02}
 */";

 while( ($str =~ m/REQ-[\w]*/g) ){

    print ("$&\n");
 }