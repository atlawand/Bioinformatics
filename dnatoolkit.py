#DNA Toolkit file
import collections
Nucleotides = ["A", "C", "G", "T"]
DNA_ReverseComplement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

#Check the sequence to make sure it is a DNA String...

def validateseq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


# count Nuc Frequency : 
def countNucFrequency(seq):
    tmpFreqDict = {"A":0, "C":0, "G":0, "T":0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

def new(seq):
    return dict(collections.Counter(seq))


def transcription(seq):
    #DNA -> RNA Transcription
    return seq.replace("T", "U")

def reverse_complement(seq):
    return ''.join([DNA_cslReverseComplement(nuc) for nuc in seq])[::-1]

