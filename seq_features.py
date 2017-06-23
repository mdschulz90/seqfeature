# py.test gives the testing functionality
#import pytest
import bioinfo_dicts

def n_neg(seq):
    """Number of negative residues a protein sequence"""

    # Convert sequence to upper case
    seq = seq.upper()

    for aa in seq:
        if aa not in bioinfo_dicts.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid.')

    if seq == 'Z':
        raise RuntimeError('Z is not a valid amino acid.')

    # Count E's and D's, since these are the negative residues
    return seq.count('E') + seq.count('D')
