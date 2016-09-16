# py.test gives the testing functionality
import pytest

# We'll use our bioinformatics dictionary from before
import bioinfo_dicts as bd

def n_neg(seq):
    """Number of negative residues a protein sequence"""
    seq = seq.upper()

    # Check for validity of sequence
    for aa in seq:
        if aa not in bd.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid.')
    # Count Es & Ds and return count
    return seq.count('D') + seq.count('E')
