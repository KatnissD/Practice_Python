#!/usr/bin/python
#coding:utf-8
codon_table = {'GCT':'A','GCC':'A','GCA':'A','GCG':'A','CGT':'R','CGC':'R','CGA':'R',\
	'CGG':'R','ACT':'T','ACC':'T','ACA':'T','ACG':'T','GTT':'V','GTC':'V','GTA':'V',\
	'GTG':'V','GGT':'G','GGC':'G','GGA':'G','GGG':'G','TCT':'S','TCC':'S','TCA':'S',\
	'TCG':'S','CTT':'L','CTC':'L','CTA':'L','CTG':'L','CCT':'P','CCC':'P','CCA':'P',\
	'CCG':'P','ATT':'I','ATC':'I','ATA':'I','ATG':'M','GAT':'D','GAC':'D','GAA':'E',\
	'GAG':'E','CAT':'H','CAC':'H','CAA':'Q','CAG':'Q','AAT':'N','AAC':'N','AAA':'K',\
	'AAG':'K','AGT':'S','AGC':'S','AGA':'R','AGG':'R','TTT':'F','TTC':'F','TTA':'L',\
	'TTG':'L','TGT':'C','TGC':'C','TGG':'W','TAT':'Y','TAC':'Y','TAA':'STOP','TAG':'STOP',\
	'TGA':'STOP'}
dna_file = open('Ce_40_ehE_hT_sequence.fa','r')
aa_file = open('Ce_40_ehE_hT_aa.txt','w')
dna = ''
for line in dna_file:
	if line.startswith('>') and dna == '':    
# The sequence title is now obtained.
		header = line
		print (header)
	elif not line.startswith('>'):
		dna = dna + line.strip()
	elif line.startswith('>') and dna != '':
		prot = ''
		for i in range(0,len(dna),3):
			codon = dna[i:i+3]
			if codon in codon_table:
				if codon_table[codon] == 'STOP':
					prot = prot + '*'
				else:
					prot = prot + codon_table[codon]
			else:
			# handle too short codons
				prot = prot + '-'
		aa_file.write(header)
		j = 0
		while j < len(prot):
			print prot[j:j+48]
			aa_file.write(prot[j:j+48] + '\n')	
			j = j + 48 
		#aa_file.write(header + prot + '\n')	
		seq = ''
		header = line
dna_file.close()
aa_file.close()
