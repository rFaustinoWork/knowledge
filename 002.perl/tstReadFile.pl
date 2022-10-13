#!/usr/bin/perl
use strict;
use warnings;

my $file = "src/tst.cpp";

my $document = do {
    local $/ = undef;
    open my $fh, "<", $file
        or die "could not open $file: $!";
    <$fh>;
};

our $wd = "";

sub printResetWord
{
    my $token = shift;
    if(length($wd)>0){
        print("  -> $wd \n");
    }
    $wd = "";
}

sub method1()
{
    my $prevChar = "";
    my @a = split("", $document);
    for(@a)
    {
        if($_ eq "\n" or $_ eq "\r"){
            printResetWord("EOL");
            print "-> EOL \n";
        }elsif($_ eq ' '){
            printResetWord("SPC");
            print "-> SPC \n";
        }elsif($_ eq '(' or $_ eq ')'){
            printResetWord("parenthesis");
            print "-> parenthesis \n";
        }elsif($_ eq ','){
            printResetWord("comma");
            print "-> comma \n";
        }elsif($_ eq '{' or $_ eq '}'){
            printResetWord();        
            print "-> curly \n";
        }elsif($_ eq '/' and $prevChar eq '/'){
            print "-> singleLineComment \n";
        }elsif($_ eq '/' and $prevChar eq '*'){
            print "-> endBlockComment \n";
        }elsif($_ eq '*' and $prevChar eq '/'){
            print "-> beginBlockComment \n";
        }else{
            $wd .= $_;
        }
        $prevChar = $_;
    }
    print "-> EOF \n";
}

sub method2()
{
    print "-> EOF \n";
}

method1();