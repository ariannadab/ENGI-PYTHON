from collections import defaultdict

def count_ngrams(file_name, n=2): 
    """
    This function reads an input file and returns a dictionary of n-gram counts.  
    file_name is a string, n is an integer. 
    The result dictionary maps n-grams to their frequency (i.e. the count of 
    how often that n-gram appears). Each n-gram key is a tuple and the count is
    an int.
    """
    # The defaultdict class may be useful here. Check the python 
    # documentation for more information: 
    # https://docs.python.org/3/library/collections.html#collections.defaultdict

    f=open(file_name,'r')
    text=f.read()
    text=text.lower()
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in punctuations:
        text=text.replace(x, "")
    text = text.replace("\n"," ")
    text = text.replace("\r"," ")
    ngrams={}
    text = text.split(' ')
    for i in range(len(text)-n+1):
        g = ' '.join(text[i:i+n])
        ngrams.setdefault(g, 0)
        ngrams[g] += 1
    return(ngrams)
            
    
    

def single_occurences(ngram_count_dict): 
    """
    This functions takes in a dictionary (in the format produces by 
    count_ngrams) and returns a list of all ngrans with only 1 occurence.
    That is, this function should return a list of all n-grams with a count
    of 1. 
    """
        
    occurs_once = []
    for key in ngram_count_dict:
        if ngram_count_dict[key] == 1:
            occurs_once.append(key)
    return occurs_once

def most_frequent(ngram_count_dict, num): 
    """
    This function takes in two parameters: 
        ngram_count_dict is a dictionary of ngram counts. 
        num denotes the number of n-grams to return.       
    This function returns a list of the num n-grams with the highest
    occurence in the file. For example if num=10, the method should 
    return the 10 most frequent ngrams in a list. 
    """
    # Hint: For this you will need to sort the information in the dict 
    # Python does not support any way of sorting dicts 
    # You will have to convert the dict into a list of (frequency, n-gram)
    # tuples, sort the list based on frequency, and return a list of the num
    # n-grams with the highest frequency. 
    # NOTE: you should NOT return the frequencies, just a list of the n-grams
    ngram_list = ngram_count_dict.items()
    ngram_list_sorted = sorted(ngram_list, key=lambda x: x[1], reverse=True)
    freq_list=[]
    for x in range(0, num):
       freq_list.append(ngram_list_sorted[x][0])
    return freq_list



def main():
    filename = input("Please enter the text file name, including the .txt extension. " )
    
    n = int((input("Please enter an integer n to find n-grams.\nEx: Entering 2 would create a dictionary of bigrams. ")))
    
    most_frequent_k = int((input("How many of the most frequent ngrams would you like returned? ")))

    ngram_counts = count_ngrams(filename, n)

    print('\n{}-grams that occur only once:'.format(n))
    print(single_occurences(ngram_counts))

    print('\n{} most frequent {}-grams:'.format(most_frequent_k, n))
    print(most_frequent(ngram_counts, most_frequent_k))

if __name__ == "__main__":
    main()
