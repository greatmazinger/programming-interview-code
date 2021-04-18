#!/usr/bin/perl -w
$multi_line = 'user
password
something_else';
@fields = split(/\n/, $multi_line);
print "Field values are:\n";
for (@fields) {
    print $_ . "|||\n";
}
