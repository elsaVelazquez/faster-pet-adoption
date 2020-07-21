
from string import punctuation
import string 
import re #to remove special chars or grepped sub_strings
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
stopwords = ENGLISH_STOP_WORDS
# from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
# stopwords = ENGLISH_STOP_WORDS

def read_the_file(fname):
    '''Reads the filename - should have a .txt extension.

       Returns a text string containing the entire description.
    ''' 
    f = open(fname, 'r')
    textstring = f.read()
    return textstring


def read_df(path):
    '''read in file
    '''
    print('read df')
    return pd.read_csv(path) 



def lowercase_text(text):
    '''Returns a text string with all characters lower-cased.
    '''
    
    text_lowercased = text.lower()
    return text_lowercased


def remove_punctuation(text, punctuation=punctuation):
    '''Returns a text string without punctuation (no html for now).
    '''

    text_no_html = re.sub('<kw>', '', text) 
    text_no_html = re.sub('</kw>', '', text_no_html)
    text_nopunct = text_no_html.translate(str.maketrans('', '', string.punctuation))
    return text_nopunct


def remove_newline(text):
    ''' Removes all newlines \n in the whole text
    '''

    text_no_nl = text.strip('\n').replace('\n','').replace('None', 'null').replace('True', 'true').replace('False', 'false')
    return text_no_nl

def keep_double_quotes(text):
    '''set any single quote to double quotes for 
    dictionary data structure to be valid JSON'''
    text_double_quotes = text.replace("\'", '\"')
    return text_double_quotes



def replace_words(word_lst, name_set, replacement_val):
    '''Optional.  Replaces words in word_lst with replacement_val.
    Words are identified in the word set.
    '''
    
    word_lst_replacements = []
    for word in word_lst:
        if word in name_set:
            val = replacement_val
        else:
            val = word
        word_lst_replacements.append(val)
    return word_lst_replacements


def create_cleaned_textline_from_words(words):
    '''Takes in a list, returns a single string.
    '''
    text = ' '.join([word for word in words])
    return text


# def line_cleaning_pipeline(text, stopwords_set, name_set, replace_val):
#     '''Transforms raw text into clean text using text-cleaning functions above'''
#     # breakpoint() #for testing pipeline
#     text_lc = lowercase_text(text)
#     text_np = remove_punctuation(text_lc)
#     text_nnl = remove_newline(text_np)
#     words = split_text_into_words(text_nnl)
#     words_nsw = remove_stopwords(words, stopwords_set)
#     words_cleaned = replace_words(words_nsw, name_set, replace_val)
#     line_of_text_cleaned = create_cleaned_textline_from_words(words_cleaned)
#     return line_of_text_cleaned


if __name__ == '__main__':
    # to help test functions and pipeline:
    # text_str1 = "<kw>dance</kw> breaks during the school-day help her kids reset, \n and on Fridays, they usually do a 10-minute <kw>dance</kw> party.  "
    # text = text_str1 #for testing pipline


    #read in a sample scraped txt file
    path_including_filename = "small_json_string.txt"

    text = read_the_file(path_including_filename)
    

    
    # test functions
    # text_lc = lowercase_text(text)
    # text_np = remove_punctuation(text_lc)
    text_nnl = remove_newline(text)
    
    cleaned_text = keep_double_quotes(text_nnl)
    print(cleaned_text)
    # words = split_text_into_words(text_nnl)
    # words_nsw = remove_stopwords(words, stopwords)
    # words_cleaned = replace_words(words_nsw, names, replace)
    # line_of_text_cleaned = create_cleaned_textline_from_words(text_nnl)

    # print(cleaned_text)
    # import json
    # print(json.dumps(cleaned_text))
    # test pipeline
    # line_text_pipeline = line_cleaning_pipeline(text)

    # same_result = line_of_text_cleaned == line_text_pipeline

    # # print results
    # print(f"Original: {text}")
    # print(f"Lowercased: {text_lc}.")
    # # print(f"Punctuation removed: {text_np}.")
    # print(f"Without newlines: {text_nnl}")
    # # print(f"Into words: {words}")
    # # print(f"No stop words: {words_nsw}")
    # # print(f"Replaces names: {words_cleaned}")
    # print(f"Sample line of cleaned text: {line_of_text_cleaned}")
    # print(f"\nDoes pipeline give same result? {same_result}")
