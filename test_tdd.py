# py.test gives the testing functionality
import pytest

# We'll use our bioinformatics dictionary from before
import bioinfo_dicts as bd

import lesson_35

def test_n_neg():
    """Number of negative residues a protein sequence"""
    assert lesson_35.n_neg('E') == 1
    assert lesson_35.n_neg('D') == 1
    assert lesson_35.n_neg('') == 0
    assert lesson_35.n_neg('ACKLWTTAE') == 1
    assert lesson_35.n_neg('DEDEDDEE') == 8
    assert lesson_35.n_neg('acklwttae') == 1

    pytest.raises(RuntimeError, "lesson_35.n_neg('Z')")

    return None
