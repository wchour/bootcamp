codon = input('Input your codon, please: ')
codon_list = ['UAA', 'UAG', 'UGA']
if codon == 'AUG':
    print('This codon is the start codon.')
elif codon in codon_list:
    print('This is a stop codon.')
else:
    print('This codon is neither a stop nor start codon.')
