
# py.test gives the testing functionality
import pytest

# We'll use our bioinformatics dictionary from before
import bioinfo_dicts as bd

DNA = 'ATGGAGAACAACGAAGCCCCCTCCCCCTCGGGATCCAACAACAACGAGAACAACAATGCAGCCCAGAAGAAGCTGCAGCAGACCCAAGCCAAGGTGGACGAGGTGGTCGGGATTATGCGTGTGAACGTGGAGAAGGTCCTGGAGCGGGACCAGAAGCTATCGGAACTGGGCGAGCGTGCGGATCAGCTGGAGCAGGGAGCATCCCAGTTCGAGCAGCAGGCCGGCAAGCTGAAGCGCAAGCAATGGTGGGCCAACATGAAGATGATGATCATTCTGGGCGTGATAGCCGTTGTGCTGCTCATCATCGTTCTGGTGTCGCTTTTCAATTGA'

protein = 'MENNEAPSPSGSNNNENNNAAQKKLQQTQAKVDEVVGIMRVNVEKVLERDQKLSELGERADQLEQGASQFEQQAGKLKRKQWWANMKMMIILGVIAVVLLIIVLVSLFN'

def find_codon_lesson6(codon, seq):
    """Find a specified codon with a given sequence."""

    i = 0
    # Scan sequence until we hit the start codon or the end of the sequence
    while seq[i:i+3] != codon and i < len(seq):
        i += 1

    if i == len(seq):
        return -1

    return i

# this function utilizes the previous function to find start point 'ATG'
def find(codon, seq):
    start = find_codon_lesson6('ATG', seq)
    i = start
    for x in range(i, len(seq)-2):
        if seq[x:x+3] == codon:
            print(x)
