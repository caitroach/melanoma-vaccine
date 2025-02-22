from Bio import SeqIO

#Loading the FASTA data
fasta_file = "MAGE-A3.fasta"

#Reading the protein sequence
with open(fasta_file, "r") as file:
  for record in SeqIO.parse(file, "fasta"):
    mage_a3_sequence = str(record.seq) #Extracting the sequence as a string

print(mage_a3_sequence) #Outputting the cleaned sequence to check
