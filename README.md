Here are descriptions of the files in this repository:

General Parser.py - Contains the parsing program, requires the user to specify a job file to run.

job.txt - A text file containing the names of the other needed text files in the following order:
          1. The source file
          2. The control file
          3. The frequency file
          4. The stats file

source.txt - A text file containing the text to be parsed by the program.

control.txt - A text file specifying how the parser should operate in the following format:
          1. Should it be case sensitive (y/n)?
          2. Alphabet of characters allowed in a "word"
          3. List of prefix characters allowed in a "word"
          4. List of infix characters allowed in a "word"
          5. List of suffix characters allowed in a "word"

frequency.txt - A text file listing all "words" that the program found as well as how many times they were found in the supplied text.

stats.txt - A text file containing some statistics on the text file that was parsed.
