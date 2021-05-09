# The genome assembling project
This repository contains my project dedicated to the genome assembling problem.
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Input format](#input-format)
## General info
This project is a string assembling algorithm, based on the Eulerian graphs, applied to the genome assembling problem.  
The [string_reconstruction.py](https://github.com/ihoxofixu/bioinfo_course_project/blob/main/string_reconstruction.py) contains only functions and can be regarded as a library.  
The [genome_reconstruction.py](https://github.com/ihoxofixu/bioinfo_course_project/blob/main/genome_reconstruction.py) is the main file that takes all the data and then process it, using string_reconstruction.py.
## Technologies
Project is created with:
* Python version: 3.9.
## Setup
To run this project, first of all, download it locally.
Then, if you want to input all the data from file, you should run it using command line. It has two arguments - input stream and output stream.
```
$ cd ../bioinfo_course_project
$ python genome_reconstruction.py -i INPUT [-o OUTPUT]
```
For help use this commands in command line:
```
$ cd ../bioinfo_course_project
$ python genome_reconstruction.py -h
```
## Input format
The program takes a collection of DNA strings in FASTA format.
Example of FASTA format:

```
>example_1
TAACCCATAGGACCCCCGCATGCCCCTAAGTAGGTACCGGAGATAACACTAGACCCGTAA
GATGTTCGGCCCGCGATTCTGGAGGATGGCTCATAGCATATCTAGCAGCCATACTTTGTA
AATCAACCTACTCAGTGTCTCAGACTGAGGATCTACCATATGATAACATCGTATGGTGAC
CTCGAGATGCGAACGTCTACCCCAGATGAAGGGCACGCTAGCAAAATCAACAAATCTCTT
GCCGACCACCGAGTCTGAAGGGTGCCATAACCCCGGGGGTCCGCCTGAGGGACCCAGTAT
ACACGCGTTGAAAAAATAACGTTTCCTTGTATTTTCAAGAAAGGCGCTGTCCATCTCGAT
GATCCACTTTTGCACCCTTGTGATGAGCCAGGAACAGCAAAGCTGTTTTATATGCCAAGA
GCCTACAAGTTCATGCTTGTTCTACTATGGGTTCGATACCTTAGCTACAAGTACTTAGTC
CCTGTAACGGACGGTTAACGACTACGCAGTTATCTCGGAGCTTGCGTCTAATAATCTTTT
ATTGCCAGAAAAGTCGTTAGGTCAACGCTTCCGTGGTTGATTGCCTCGTAATAGGGAATG
ATTTCGCATCGACCTGTCTTGTGCTAATACCAGAAGTCGTGTTGATAATAACGACAACCT
CCTGCCCAGACTTTTGGATGTACTCCTATCTGATCCTATAAGATGATGAAATTGACGCTG
GCCTAAAGACTGGCAATCGTATACAACTGTCTCTGGCTGGTAAACGTACATGCCTCTGAG
TCCGGTTGTCTACACAGACAATGACTTCCGCGTACCCCATCTAACGATTCACGCCGCTGG
GTACTGGAATTTTCGTTTGACCTACCCCACTAGAGGCTACTGGCTGCGGATACGTTGAGG
AGGTAATAAGGTGGTTGTCCTATTCTTCTTGGCATTAGCAGCGACACCCCGATCACGAAT
GCGTAGAGACTTGAAACAATGTCCCGTGTTAGCACCCCGG
```
