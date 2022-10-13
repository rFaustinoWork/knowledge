#!/usr/bin/perl
use strict;
use warnings;

package CTokenizer;

sub new
{
    my $class = shift;
    my $self = {};
    bless $self, $class;

    $self->{_tokens} = [];
    $self->{_tmpWord} = "";
    
    return $self;
}

sub DESTROY
{
    # not needed    
}

sub getFilename
{
    my $self = shift;
    return $self->{_filename};
}

sub _handleWord
{
    my ($self, $token_code) = @_;

    $self->{_tmpWord} =~ s/^\s+|\s+$//g;


    if(length($self->{_tmpWord})>0){
        push( @{$self->{_tokens}}, $self->{_tmpWord});
    }
    if($token_code ne "SPC"){
        push( @{$self->{_tokens}}, $token_code);
    }
    $self->{_tmpWord} = "";
}

sub ProcessFile
{
    my ($self, $filename) = @_;

    my $document = do {
        local $/ = undef;
        open my $fh, "<", $filename or die "could not open $filename: $!";
        <$fh>;
    };

    my $state = 0;
    my $prevChar = "";
    my @a = split("", $document);
    for(@a)
    {
        if($state == 0)
        {
            if($_ eq "\n" or $_ eq "\r"){
                $self->_handleWord("EOL");
            }elsif($_ eq ' '){
                $self->_handleWord("SPC");
            }elsif($_ eq '('){
                $self->_handleWord("oBracket");
            }elsif($_ eq ')'){
                $self->_handleWord("cBracket");
            }elsif($_ eq ','){
                $self->_handleWord("comma");
            }elsif($_ eq ';'){
                $self->_handleWord("semiColon");
            }elsif($_ eq '{'){
                $self->_handleWord("oCurly");
            }elsif($_ eq '}'){
                $self->_handleWord("cCurly");
            }elsif($_ eq '/' and $prevChar eq '/'){
                $state = 1;
                $self->{_tmpWord} .= $_;
            }elsif($_ eq '*' and $prevChar eq '/'){
                $state = 2;
                $self->{_tmpWord} .= $_;
            }else{
                $self->{_tmpWord} .= $_;
            }
        }elsif($state == 1)
        {   # Single line comment 
            if($_ eq "\n" or $_ eq "\r"){
                $self->_handleWord("commentLine");
                $state = 0;
            }else{
                $self->{_tmpWord} .= $_;
            }
        }elsif($state == 2)
        {   # Multiline comment 
            if($_ eq '/' and $prevChar eq '*'){
                $self->{_tmpWord} .= $_;
                $self->_handleWord("commentBlock");
                $state = 0;
            }else{
                $self->{_tmpWord} .= $_;
            }
        }
        $prevChar = $_;
    }
    $self->_handleWord("EOF");
    
    # for (@{$self->{_tokens}})
    # {
    #     print "-> $_\n";
    # }
    return @{$self->{_tokens}};
}


1;