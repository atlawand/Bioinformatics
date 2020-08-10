# DNA ToolSet/Code testing file...
from dnatoolkit import *

import random


rndDNAStr =''.join([random.choice(Nucleotides)
                    for nuc in range(50)])

DNAStr = validateseq(rndDNAStr)

print(validateseq(rndDNAStr))
print(countNucFrequency(DNAStr))
print(new(DNAStr))
print(transcription(DNAStr))


print(f'\nSequence: {DNAStr}')
print(f'[1] Sequence Length: {len(DNAStr)}')
print(f'[2] NUcleotide Frequency: {countNucFrequency(DNAStr)}')
print(f'[3] DNA to RNA Transcription: {transcription(DNAStr)}')
