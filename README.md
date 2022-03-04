# semantle_solver
Shitty Semantle Solver

After not solving semantle for 3 days straight, I decided to write a script to help me. 
To use this script, you need to download GoogleNews-vectors-negative300.bin dataset
I obtained this from https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz
This is probably outdated. Also download at your own risk lmao.

How to use:
1. Run the program
1. Guess a word on Semantle
1. Enter the word and similarity score when prompted
1. Wait for a (potentially huge) list of potential words that could be the answer
1. pick a word from the list and guess it on semantle
1. Repeat from step 3 until you get the answer

Dependencies:
nltk
gensim
