"""Write a function that divides a sequence into blocks and computes the GC
content for each block, returning a tuple. The function signature should look
like

gc_blocks(seq, block_size)

To be clear, if seq = 'ATGACTACGT and block_size = 4, the blocks to be
considered are

ATGA
CTAC

and the function should return (0.25, 0.5). Note that the blocks are
non-overlapping and that we don't bother with the end of the sequence that does
not fit completely in a block.
"""

def gc_blocks(seq, block_size):
    import math

    # Calculate # of slots in tuple.
    tuple_size = int(math.ceil(len(seq)/(block_size)))


    # initialize variables
    seq = seq.upper()
    gc_tuple = ()

    # run through sequence, calculating GC content per block and concatenating
    # tuple with GC content value
    for i in range(tuple_size):
        a = seq[(i-1) * block_size : i * block_size].count('G')
        b = seq[(i-1) * block_size : i * block_size].count('C')
        gc = (a+b)/block_size
        gc_tuple += tuple((gc,))

    # remove the first entry of tuple (1st entry is 0.0 for some reason...)
    gc_tuple = gc_tuple[1:]

    return gc_tuple


"""
Write a function that takes as input a sequence, block size, and a threshold GC
content, and returns the original sequence where every base in a block with GC
content above threshold is capitalized and every base in a block below the
threshold is lowercase. You would call the function like this:
mapped_seq = gc_map(seq, block_size, gc_thresh)

For example,
gc_map('ATGACTACGT', 4, 0.4)

returns 'atgaCTAC'. Note that bases not included in GC blocks are truncated.
"""

def gc_map(seq, block_size, gc_thresh):
    import math

    # Calculate # of slots in tuple.
    tuple_size = int(math.ceil(len(seq)/(block_size)))

    # initialize variables
    seq = seq.upper()
    counter = 0
    seq_out = ''
    gc_tuple = ()

    # run through sequence, calculating GC content per block and concatenating
    # tuple with GC content value
    for i in range(tuple_size):
        a = seq[(i-1) * block_size : i * block_size].count('G')
        b = seq[(i-1) * block_size : i * block_size].count('C')
        gc = (a+b)/block_size
        gc_tuple += tuple((gc,))
        if gc > gc_thresh:
            seq_out += seq[(i-1) * block_size : i * block_size].upper()
        else: seq_out += seq[(i-1) * block_size : i * block_size].lower()

    # remove the first entry of tuple (1st entry is 0.0 for some reason...)
    gc_tuple = gc_tuple[1:]

    return seq_out


"""
test case for exercise, imports salmonella data as a single string w/ 1st line stripped
"""
def salmonella(data):
    # input = data/salmonella_spi1_region.fna
    f = open(data,'r')
    f_str = f.readlines()
    f_str = f_str[1:]
    number = len(f_str)
    seq = ''
    for i in range(number):
        seq += f_str[i].rstrip()
    return seq

"""
locate region of pathogenicity island in salmonella for specified block size
"""
def islands(block_size):
    data = gc_blocks(salmonella('data/salmonella_spi1_region.fna'), 1000)
    import math

    # Calculate # of slots in tuple.
    seq = data
    size = int(math.ceil(len(seq)/(block_size)))
    counter = 0
    count = []

    for i in range(size):
        while counter != size:
            count += [i-1]

    return count

"""
function to final part of salmonella exercise
"""

def salmonella_answer():
    import math
    with open('salmonella_answer.txt', 'w') as f:
        f.write('>gi|821161554|gb|CP011428.1| Salmonella enterica subsp. enterica strain YU39, complete genome, subsequence 3000000 to 3200000\n')
        # seq = salmonella('data/salmonella_spi1_region.fna')
        seq = gc_map(salmonella('data/salmonella_spi1_region.fna'), 1000, 0.45)
        seq_length = len(seq)
        final_seq = ''
        iterations = int(math.ceil(seq_length/60))
        #return seq
        for i in range(iterations):
            final_seq += seq[:60] + '\n'
            seq = seq[60:]
        f.write(final_seq)

"""
Write a function, longest_orf(), that takes a DNA sequence as input and finds
the longest open reading frame (ORF) in the sequence (we will not consider
reverse complements). A sequence fragment constitutes an ORF if the following
are true.
It begins with ATG.
It ends with any of TGA, TAG, or TAA.
The total number of bases is a multiple of 3.
Note that the sequence ATG may appear in the middle of an ORF. So, for example,
GGATGATGATGTAAAAC

has two ORFs, ATGATGATGTAA and ATGATGTAA. You would return the first one, since
it is longer of these two.
"""

def longest_orf(seq):
    data = seq.upper()
    length = len(seq)
    stop_list = ['TGA', 'TAG', 'TAA']
    master_count = 0
    longest = ''
    import math
    # length = # of iterations, minus 2 to avoid terminal 2 bases
    # for each iteration, check if ATG
        # if ATG, move to next 3 and check, if not stop list, move to next 3 and check
    for i in range(length-2):
        if data[i-1:i+2] == 'ATG':
            count = 0
            count1 = 0
            for j in range(int(math.floor(((length-(i+2))/3)))):
                if data[i+(j*3)-1:i+(j*3)+2] in stop_list:
                    break
                else: count += 1
            if count > 0:
                count1 = i+(3*count)
            if count1 > master_count:
                master_count = count1
                longest = seq[i-1:i+2+(3*count)]
        else: pass
    return longest

def orfB():
    return longest_orf(salmonella('data/salmonella_spi1_region.fna'))


def DNA2protein(seq):
# import DNA sequence
    import math
    aa = {'A': 'Ala',
          'R': 'Arg',
          'N': 'Asn',
          'D': 'Asp',
          'C': 'Cys',
          'Q': 'Gln',
          'E': 'Glu',
          'G': 'Gly',
          'H': 'His',
          'I': 'Ile',
          'L': 'Leu',
          'K': 'Lys',
          'M': 'Met',
          'F': 'Phe',
          'P': 'Pro',
          'S': 'Ser',
          'T': 'Thr',
          'W': 'Trp',
          'Y': 'Tyr',
          'V': 'Val'}

    # The set of DNA bases
    bases = ['T', 'C', 'A', 'G']

    # Build list of codons
    codon_list = []
    for first_base in bases:
        for second_base in bases:
            for third_base in bases:
                codon_list += [first_base + second_base + third_base]

    # The amino acids that are coded for (* = STOP codon)
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'

    # Build dictionary from tuple of 2-tuples (technically an iterator, but it works)
    codons = dict(zip(codon_list, amino_acids))

    del codon_list
    del amino_acids
    del bases
    del first_base
    del second_base
    del third_base

    data = seq.upper()
    length = len(seq)
    stop_list = ['TGA', 'TAG', 'TAA']
    temp_dna = ''
    protein_list = []

# length = # of iterations, minus 2 to avoid terminal 2 bases
# for each iteration, check if ATG
    # if ATG, move to next 3 and check, if not stop list, move to next 3 and check
    for i in range(length-2):
        if data[i-1:i+2] == 'ATG':
            count = 0
            count1 = 0
            temp_protein = ''
            temp_protein += codons['ATG']
            for j in range(int(math.floor((length-i-1)/3))):
                if data[i+(j*3)-1:i+(j*3)+2] in stop_list:
                    pass
                else:
                    count += 1
                    temp_protein += codons[data[i+(j*3)-1:i+(j*3)+2]]
            if count > 0:
                temp_dna = seq[i-1:i+2+(3*count)]
                protein_list += list(temp_protein)

        else: pass
    return protein_list
