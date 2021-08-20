"""Retrieve and print words from a URL.

Usage:
   
   python3 fetchWords.py <URL>
"""

import sys
from urllib.request import urlopen

def fetch_words(url):
   """fetch a list of words from URL.

    Args:
        url: The URL of words from UTF-8 text document.
    Returns:
        A list of string containing the words from the document
   """    
   story = urlopen('url')
   story_words =[]
   for line in story:
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)
   story.close()
   return story_words

def print_items(items):
    """print items one per line.
        Args:
           An iterable series of printable items.
    """
    for word in items:
     print(items)

def main(url):
    """print each word from a text document from at a URL.
        Args:
            url: The Url ofa UTF-8 text document.
    """        
    url = sys.argv[1]
    words= fetch_words(url)
    print_items(words)

    
if __name__=='__main__':
        fetch_words()

import time
time.ctime()
def show_default(arg=time.ctime()):
    print(arg)



