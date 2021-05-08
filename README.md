# The genome assembling project
This repository contains my project dedicated to the genome assembling problem.
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Input format](#input-format)
## General info
This project is a string assembling algorithm, based on the Eulerian graphs, applied to the genome assembling problem. \n
The [string_reconstruction.py](https://github.com/ihoxofixu/bioinfo_course_project/blob/name_main_test/string_reconstruction.py) contains only functions and can be regarded as a library. \n
The [genome_reconstruction.py](https://github.com/ihoxofixu/bioinfo_course_project/blob/name_main_test/genome_reconstruction.py) is the main file that does all the data and then process it, using string_reconstruction.py.
## Technologies
Project is created with:
* Python version: 3.9.
## Setup
To run this project, first of all, download it locally.
Then, if you want to input all the data from file, you should run it using cmd:

```
$ cd ../bioinfo_course_project
$ python genome_reconstruction.py FILENAME.txt
```
Make sure, that your file is in the same folder as genome_reconstruction.py and string_reconstruction.py; \n
Otherwise, if you want to input data from your keyboard, you should run it a bit another way:

```
$ cd ../bioinfo_course_project
$ python genome_reconstruction.py STDIN
```
Or you can just run it in your interpreter.
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
>example_2
AAGGAAGGAGACATTACCCAAGCTACCGCTAACGGCGTAGCGGGTAGCTTCCGAGTTGTG
CAATTATGGTCCTACAAAACAGAGGGCGTCAGGTTAAACCGTGCAGGTCCCGCCTCATTT
TACTAGAGCATCTTTTCCATACTCAATCCGCAATGTAGCGGCTTCAAATCGCTACAAACC
AAGACTCGCGCCGTTGCGGTGTTATCATAGTGTTGAAACAGCCGGTGTTGGAATACAGAA
TATTAAATCCTTAACCCCACACGTCAGCGTCCGCACTGGACGAGCAATTTACCTAAGAGC
GTACCGACACATCTCGCGTTACCCGCCCTCCGGACGTGGAAAACTTCTCGTCAGATCTCA
TAAGAGTAGTACCGCGAATTCCCAGTGTTAATTCCCTTAAATCTCTCTCGGCGCTACAAG
TCTAGGGTTAATGAGCTCCCAGGATGGTGATCTCACGTATGTTGAACCGTTGGTTAGCTA
TGATTTACGCGTAAGCGAACATGAGTTCCTTGACACTCACGTAGGATAGTACGGGCGTTG
TTCTAAACGTCGCTGGGTTTGTAGTGGTGCACGTGGCATAGCGACCATTCTTTCGGAACA
TTCATTGCGACTCCCTAGACACTCCAACAGCAGAACATCAACCCCGCATGCCTAGTTTGA
TTCCGCCAGGATGGTGCGGAATCTTTTATCCTTTTTCAAGAAAGGCGCTGTCCATCTCGA
TGAACTGCCAGTGCCTAGCCGATGAACATCGTGGATTAAAGCTATGTCCTGTGTGGTCAG
GTAAGAACTTAAGCCAGGGCATCCCCGCCCGTTGTAAGTCTGTTTCTCTGTCCACAGGTT
AGAAGAGGGGCTCTTGTTCCCTATAAAATTAGTGAGGGAATTAGGGCTTCACCCCGCCTC
CGCTGTACAACAAGAATGCAGGTAGACTGACTAGGTAGAGCCCCACTTTTTTTTCGCACT
TTATATTCCCCCCTGCTTTTATGCTACCCTGCTCAGTACG
```
Also it is required for a solution to exist, or a program will crash.
