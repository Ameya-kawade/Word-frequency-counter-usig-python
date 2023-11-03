import re
from collections import Counter


def wordFrequencyCounter(inputFilePath,outputFilePath):
    try :
        # Opening the file
        with open(inputFilePath,'r') as file :
            # Reading from the file and removing whitespaces and \n
            linesFromFile = file.read().strip().replace("\n"," ")
            # Creating delimitter which will be used for splitting the string
            delimiter = r',|;|\.|\(|\)| |:|"|\'|/'
            # Splitting the string on the basis of the given delimiters 
            # It returns a list of strings
            words = re.split(delimiter, linesFromFile)
            # Using list comprehesion to only add non empty strings in the list 
            words = [word for word in words if word != ""]
            # Creating counter to count the frequency of all words
            # It returns a dictionary with words as keys and frequencies of those words as key's value
            wordCounter = Counter(words)
            
            # Opening the output file to write the output in it

            with open(outputFilePath,'w') as output :

                output.write("Frequency of words is as follows : \n\n")

                for keys, values in wordCounter.items() :

                    output.write(f"{keys} : {values} times\n\n")

    except FileNotFoundError:
        print("File not found, please give a valid file path.")            


wordFrequencyCounter('./file2.txt','./output.txt')
