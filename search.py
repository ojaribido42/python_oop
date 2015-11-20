import pdb
import difflib as diff

class SortFile(object):
     
    """ This class opens a file and sorts all the items in that file. """
    
    def __init__(self,file_name):
        self._file_name = file_name
        
    def read_file(self):
        self._file_handle = open(self._file_name,'r')
        text = self._file_handle.read()
        return text

    def clean_file(self,text):
        import string
        return text.translate(string.maketrans("",""), string.punctuation)
    
    def sort_file(self,text):
        doc =[s for s in text.split(" ")]
        doc.sort()
        return doc


class LinearSearch(SortFile):
    """This class searches within the sorted words and prints out the three closest words to the inserted word """

    def __init__(self,word,file_name):
        self.__search_word = word.lower()
        self.__selected_list = []
        self.__all_words = {}
        self._file_name = file_name
        
        """ Initialize the contructor of the inherited class """
        SortFile.__init__(self,self._file_name)


    """ Define a search method"""
    def search(self):
        _text = self.read_file()
        _text = self.clean_file(_text)
        _text = self.sort_file(_text)
        SEARCH = True
        n = 10 # Number of selected list
        r = 1 # For exact matches
        while (SEARCH == True):
            templist = diff.get_close_matches(self.__search_word,_text,n,r) # this method returns n words of less depending on the number of matches
            self.__selected_list.extend(list(set(templist))) # this line adds only a unique list \ to the list of selected words. Basically, only one word that exactly matches the string would be added to the list in the first loop
            if len(self.__selected_list) > 9:
                SEARCH == False
                return self.__selected_list
            else:
                # Delete the selected words from the list of words available
                for selected_words in self.__selected_list:
                    if selected_words in _text:
                        _text.remove(selected_words)

                n = 10 - len(self.__selected_list)
                r -= 0.1 
    
    

class CalculateTime(object):
    """ This file calculates the time taken for each of the other two classes to run """
    from time import time
    pass



def main():
    newText = LinearSearch("love","text")
    result = newText.search()
    print(result)


if __name__ == "__main__":
    main()        

 
