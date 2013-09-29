import unittest

def get_length(dna):
    """ (str) -> int
    Return the length of the DNA sequence dna.
    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    ''' hy's original code:
    length = 0
    for char in dna:
        if char in 'AGCT':
            length = length + 1

    print(length)
    '''

    # wjd's suggestion:
    return len(dna)

    '''Explanation: 
    I don't think they want you to print the number of letters from the set {A, G, C, T}.
    I think they just want you to return (not print) the length of the given string.
    Whether or not it is a valid dna sequence doesn't matter.'''


def is_longer(dna1, dna2):
    """ (str, str) -> bool
    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.
    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    # hy's original code:
    if len(dna1) > len(dna2):
        return True
    else:
        return False
    
    '''Comments:  Looks great!  Your code is correct!!

    One minor note: you don't need the else. 

    This will also work:

        if len(s1)>len(s2):
            return True
        return False
    '''

def count_nucleotides(dna, nucleotide): 
    """ (str, str) -> int
    Return the number of occurrences of nucleotide in the DNA sequence dna.
    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    #hy's code:
    occurrence = 0
    for char in dna:
        if char in nucleotide:
            occurrence = occurrence + 1

    # print(occurrence)
    
    '''Comments: I think your code is essentially correct.
    However, they want you to return (not print) the count.
    '''
    # wjd's suggested mod
    return occurrence


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool
    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.
    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    # hy's original code:
    for char in dna2:
        if dna2[:] in dna1:
            return True
        else:
            return False

    '''Comments: looks great!  
    (again, you don't need the else)'''


def is_valid_sequence(dna): 
    """ (str) -> bool
    Return True if and only if the DNA sequence is valid (that is, it contains
    no characters other than 'A', 'T', 'C' and 'G').
    >>> is_valid_sequence('ACGTACG')
    True
    >>> is_valid_sequence('AAA')
    True
    >>> is_valid_sequence('TTTTTTT')
    True
    >>> is_valid_sequence('ABC')
    False
    """
    # hy's original code:
    not_nucleotides = 'BDEFHIJKLMNOPQRSUVWXYZ'

    # for char in not_nucleotides:
    #     if char in dna:
    #         return False
    #     else:                 <<== Here is the bug
    #         return True

    # The following will work
    for char in not_nucleotides:
        if char in dna:
            return False

    return True


    '''Comments:
    
    You could also do this:

        nucleotides = 'ATCG'
        for char in dna:
            if not char in nucleotides:
                return False
        return True
    '''


def insert_sequence(dna1, dna2, index): 
    """ (str, stre, int) -> str
    Return the DNA sequence obtained by inserting the second DNA sequence into
    the first DNA sequence at the given index.
    index <= len(dna1)
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('TAGA', 'C', 3)
    'TAGCA'
    >>> insert_sequence('AA', 'TGCG', 0)
    'TGCGAA'
    >>> insert_sequence('C', 'A', 1)
    'CA'
    """
    # hy's original code:
    # sequence = dna1[:index] + dna2 + dna1[index:]
    # print(sequence)
    
    '''Comments: looks great!

    ...but it will probably be marked wrong since they just
    want you to return the answer, don't print it.

    Try this instead:
    '''
    return dna1[:index] + dna2 + dna1[index:]
    

def get_complement(nct):
    """ (str) -> str
    Return the nct's complement.
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A'
    """

    '''hy's original code:
    complement = ''
    if nct == 'A':
        complement == complement + 'T'
    if nct == 'G':
        complement == complement + 'C'
    if nct == 'C':
        complement == complement + 'G'
    if nct == 'T':
        complement == complement + 'A'

    print(complement)
    '''

        
    '''Comments: good start!

    Two problems:
    
        1. you are printing the complement instead of returning it.

        2. you use double equals instead of assignment.

    Here's how I would rewrite the function:
    '''
    if nct == 'A':
        return 'T'
    if nct == 'G':
        return 'C'
    if nct == 'C':
        return 'G'
    if nct == 'T':
        return 'A'


''' TEST CODE '''


''' Test 1:
    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
'''
print "\n---- Test 1 ----"
print "    get_length('ATCGAT') returns:", get_length('ATCGAT')
if not get_length('ATCGAT')==6:
    print "    >>>> FAILED TEST 1 <<<<"

print "    get_length('ATCG') returns:", get_length('ATCG')
if not get_length('ATCG')==4:
    print "    >>>> FAILED TEST 1 <<<<"


''' Test 2:
    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
'''
print "\n---- Test 2 ----"
print "    is_longer('ATCG', 'AT') returns:", is_longer('ATCG', 'AT')
if not is_longer('ATCG', 'AT'):
    print "    >>>> FAILED TEST 2 <<<<"
print "    is_longer('ATCG', 'ATCGGA') returns:", is_longer('ATCG', 'ATCGGA')
if is_longer('ATCG', 'ATCGGA'):
    print "    >>>> FAILED TEST 2 <<<<"

print "    get_length('ATCG') returns:", get_length('ATCG')
if not get_length('ATCG')==4:
    print "    >>>> FAILED TEST 1 <<<<"


''' Test 3:
    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
'''
print "\n---- Test 3 ----"
print "    count_nucleotides('ATCGGC', 'G') returns:", count_nucleotides('ATCGGC', 'G')
if not count_nucleotides('ATCGGC', 'G')==2:
    print "    >>>> FAILED TEST 3 <<<<"
print "    count_nucleotides('ATCTA', 'G') returns:", count_nucleotides('ATCTA', 'G')
if not count_nucleotides('ATCTA', 'G')==0:
    print "    >>>> FAILED TEST 3 <<<<"


''' Test 4:
    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
'''
print "\n---- Test 4 ----"
print "    contains_sequence('ATCGGC', 'GG') returns:", contains_sequence('ATCGGC', 'GG')
if not contains_sequence('ATCGGC', 'GG'):
    print "    >>>> FAILED TEST 4 <<<<"
print "    contains_sequence('ATCGGC', 'GT') returns:", contains_sequence('ATCGGC', 'GT')
if contains_sequence('ATCGGC', 'GT'):
    print "    >>>> FAILED TEST 4 <<<<"


''' Test 5:
    >>> is_valid_sequence('ACGTACG')
    True
    >>> is_valid_sequence('AAA')
    True
    >>> is_valid_sequence('TTTTTTT')
    True
    >>> is_valid_sequence('ABC')
    False
'''
print "\n---- Test 5 ----"

# Here are the cases we will test:
cases = {0:'ACGTACG', 1:'AAA', 2:'TTTTTTT', 3:'ABC', 4:'ABBBBBB'}

# Here are the correct answers in each case:
answers = {0:True, 1:True, 2:True, 3:False, 4:False}

# Test each case:
for k in range(len(cases)):
    print "    is_valid_sequence('", cases[k],"') returns:", is_valid_sequence(cases[k])
    if not is_valid_sequence(cases[k])==answers[k]:
        print "    >>>> FAILED TEST 5 on input:", cases[k]


''' Test 6:
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('TAGA', 'C', 3)
    'TAGCA'
    >>> insert_sequence('AA', 'TGCG', 0)
    'TGCGAA'
    >>> insert_sequence('C', 'A', 1)
    'CA'
'''
print "\n---- Test 6 ----"
print "    insert_sequence('CCGG', 'AT', 2) returns:", insert_sequence('CCGG', 'AT', 2)
if not insert_sequence('CCGG', 'AT', 2)=='CCATGG':
    print "    >>>> FAILED TEST 6 <<<<"
print "    insert_sequence('TAGA', 'C', 3) returns:", insert_sequence('TAGA', 'C', 3)
if not insert_sequence('TAGA', 'C', 3)=='TAGCA':
    print "    >>>> FAILED TEST 6 <<<<"
print "    insert_sequence('AA', 'TGCG', 0) returns:", insert_sequence('AA', 'TGCG', 0)
if not insert_sequence('AA', 'TGCG', 0)=='TGCGAA':
    print "    >>>> FAILED TEST 6 <<<<"
print "    insert_sequence('C', 'A', 1) returns:", insert_sequence('C', 'A', 1)
if not insert_sequence('C', 'A', 1)=='CA':
    print "    >>>> FAILED TEST 6 <<<<"

''' Test 7:
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A'
'''
print "\n---- Test 7 ----"
print "    get_complement('A') returns:", get_complement('A')
if not get_complement('A')=='T':
    print "    >>>> FAILED TEST 7 <<<<"
print "    get_complement('C') returns:", get_complement('C')
if not get_complement('C')=='G':
    print "    >>>> FAILED TEST 7 <<<<"
print "    get_complement('T') returns:", get_complement('T')
if not get_complement('T')=='A':
    print "    >>>> FAILED TEST 7 <<<<"
