def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

##STEP 3 Write functions is_valid_sequence and insert_sequence


def is_valid_sequence(dna1):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (that is, it contains
    no characters other than 'A','T','C' and'G').

    >>> is_valid_sequence('SSAGG')
    False
    >>> is_valid_sequence('SSSS')
    False
    >>> is_valid_sequence('AAAA')
    True
    >>> is_valid_sequence('ATGC')
    True

    """
    checker = True 
    for char in dna1:
        if (char !='A' and char !='T' and char !='C' and char!= 'G'):
            checker =False
            break

    return checker            
        
    

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) ->str

    Return the DNA sequence obtained by inserting the second DNA sequence into
    the first DNA sequence at the given index

    >>> insert_sequence('CCGG', 'AT', 4)
    'CCGGAT'
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> 
    
    """
    return dna1[:index] + dna2 +dna1[index:]


##STEP 4 Write functions get_complement and get_complementary_sequence.

def get_complement(nucleotide):
    """ (str) -> str

    The first parameter is a nucleotide ('A','T','C' or 'G'). Return the
    nucleotide's complement. The nucleotides in one strand are
    bonded to the nucleotides in the otherstrand. A and T can be bonded together,
    and thus complement each other; similarly, C and G are complements of each other.

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    
    """
    if (nucleotide =='A'):
        return 'T'     
    elif (nucleotide =='T'):
        return 'A'
    elif (nucleotide =='C'):
        return 'G'
    elif (nucleotide =='G'):
        return 'C'

def get_complementary_sequence(dna1):
    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.

    >>> get_complementary_sequence('AT')
    'TA'
        
    """
   ## x=0
    nucleotide1=''
    for x in range(0, len(dna1)):
         nucleotide = get_complement(dna1[x])
         nucleotide1 = nucleotide1 + nucleotide
        
    return nucleotide1  
