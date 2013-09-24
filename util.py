import unittest

def get_length(s):
    return len(s)


def is_longer(s1,s2):
    if len(s1)>len(s2):
        return True
    return False

def count_nucleotides(dna,N):
    count=0
    for x in dna:
        if x == N:
            count=count+1
    return count

def contains_sequence(s1,s2):
    if s1 in s2:
        return True
    return False


# TEST CODE
e = ''
s = 'ABCD'
t = 'ABCDE'
dnas = e,s,t
for k in range(len(dnas)):
    print "Test", k, ": get_length(", dnas[k], ") returns:", get_length(dnas[k])

print "Test 3 : is_longer(", e, ",", s, ") returns:", is_longer(e,s)
print "Test 4 : is_longer(", s, ",", e, ") returns:", is_longer(s,e)
print "Test 5 : is_longer(", s, ",", t, ") returns:", is_longer(s,t)
print "Test 6 : is_longer(", t, ",", s, ") returns:", is_longer(t,s)
print
print "Test 7 : contains_nucleotides(", e, ",'A') returns:", count_nucleotides(e,'A')
print "Test 8 : contains_nucleotides(", s, ",'A') returns:", count_nucleotides(s,'A')
print "Test 9 : contains_nucleotides(", t, ",'G') returns:", count_nucleotides(t,'G')
print
print "Test 10 : contains_sequence(", e, ",", s, ") returns:", contains_sequence(e,s)
print "Test 11 : contains_sequence(", s, ",", e, ") returns:", contains_sequence(s,e)
print "Test 12 : contains_sequence(", s, ",", t, ") returns:", contains_sequence(s,t)
print "Test 13 : contains_sequence(", t, ",", s, ") returns:", contains_sequence(t,s)
