#!/usr/bin/perl
use strict;
use warnings;

use lib ".";

use CTokenizer;

my $obj = new CTokenizer();

my @tokens = $obj->ProcessFile("src/tst.cpp");

my @ar;
my %results;
my @tmpReq;

my $isAReqWaiting = 0;

for my $i (0 .. $#tokens) {
    my $tok = $tokens[$i];
    if($tok eq "commentBlock" or $tok eq "commentLine"){
        @tmpReq = ();
        #while($tokens[$i-1] =~ m/REQ-[\w\-\,]*/g){
        while($tokens[$i-1] =~ m/\@real\{[\w\-\,\_]*\}/g){
            $isAReqWaiting = 1;
            push(@tmpReq, substr($&,6,-1));
        }
    }elsif($tok eq "class"){
        if($tokens[$i+2] ne "semiColon"){
            my $str = "";
            for(@ar){
                $str .= $_."::";
            }
            if($isAReqWaiting == 1){
                $isAReqWaiting = 0;
                for(@tmpReq){
                    if(exists $results{$_}){
                    $results{$_} .= "[SEP]".$str.$tokens[$i+1];
                }else{             
                    $results{$_} = $str.$tokens[$i+1];
                }
                }
                # print("Class name: $str$tokens[$i+1]\n");
            }
            push(@ar, $tokens[$i+1]);
        }
    }elsif($tok eq "enum"){
        my $str = "";
        for(@ar){
            $str .= $_."::";
        }
        if($isAReqWaiting == 1){
            $isAReqWaiting = 0;
            for(@tmpReq){
                if(exists $results{$_}){
                    $results{$_} .= "[SEP]".$str.$tokens[$i+1];
                }else{             
                    $results{$_} = $str.$tokens[$i+1];
                }
            }
            # print("Enum name: $str$tokens[$i+1]\n");
        }
        push(@ar, $tokens[$i+1]);
    }elsif($tok eq "struct"){
        my $str = "";
        for(@ar){
            $str .= $_."::";
        }
        if($isAReqWaiting == 1){
            $isAReqWaiting = 0;
            for(@tmpReq){
                if(exists $results{$_}){
                    $results{$_} .= "[SEP]".$str.$tokens[$i+1];
                }else{             
                    $results{$_} = $str.$tokens[$i+1];
                }
            }
            # print("Struct name: $str$tokens[$i+1]\n");
        }
        push(@ar, $tokens[$i+1]);
    }elsif($tok eq "oBracket"){
        my $str = "";
        for(@ar){
            $str .= $_."::";
        }
        if($isAReqWaiting == 1){
            $isAReqWaiting = 0;
            for(@tmpReq){
                if(exists $results{$_}){
                    $results{$_} .= "[SEP]".$str.$tokens[$i-1];
                }else{             
                    $results{$_} = $str.$tokens[$i-1];
                }
            }
            # print("Function name: $str$tokens[$i-1]\n");
        }
    }elsif($tok eq "semiColon" and $tokens[$i-1] eq "cCurly"){
        pop(@ar);
    }elsif($tok eq "semiColon" and $tokens[$i-1] ne "cBracket"){
        my $str = "";
        for(@ar){
            $str .= $_."::";
        }
        if($isAReqWaiting == 1){
            $isAReqWaiting = 0;
            for(@tmpReq){
                if(exists $results{$_}){
                    $results{$_} .= "[SEP]".$str.$tokens[$i-1];
                }else{             
                    $results{$_} = $str.$tokens[$i-1];
                }
            }
            #print("Method name: $str$tokens[$i-1]\n");
        }
    }
}

for(keys %results){
    print("$_   -> $results{$_}\n");
}

# my $state = 0;
# my $idxComment = -1;
# my $idxSemiColon = -1;
# for my $i (0 .. $#tokens) {
#     my $tok = $tokens[$i];

#     if($tok eq "commentBlock"){
#         $idxComment = $i;
#     }
#     if($tok eq "semiColon"){
#         $idxSemiColon = $i;
#     }

#     if($state == 0)
#     {
#         if($tokens[$i] eq "oCurly"){
#             print("i              = $i\n");
#             print("idxComment     = $idxComment\n");
#             print("idxSemiColon   = $idxSemiColon\n");

#             my $tmpIdx = $idxComment;
#             while(1){
#                 if($tokens[$tmpIdx] eq "class"){
#                     print("Class name: $tokens[$tmpIdx+2]\n");
#                     last;
#                 }elsif($tokens[$tmpIdx] eq "enum"){
#                     print("Enum name: $tokens[$tmpIdx+2]\n");
#                     last;
#                 }elsif($tokens[$tmpIdx] eq "struct"){
#                     print("Struct name: $tokens[$tmpIdx+2]\n");
#                     last;
#                 }
#                 $tmpIdx += 1;
#             }


#             #$state = 1;
#         }
#     }elsif($state == 1){
#         if($tokens[$i] eq "oCurly"){
#             $state = 2;
#         }
#     }elsif($state == 2){
#        # print("END");

#     }

# }
