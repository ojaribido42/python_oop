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
        self.__search_word = word
        self.__list_of_selected = []
        self.__list_of_all_words = {}
        self._file_name = file_name
        SortFile.__init__(self,self._file_name)

    def search(self):
        _text = self.read_file()
        _text = self.clean_file(_text)
        _text = self.sort_file(_text)
        
        for each_word in _text:

            
    
    

class CalculateTime(object):
    """ This file calculates the time taken for each of the other two classes to run """
    from time import time
    pass



def main():
    newText = SortFile("text")
    text = newText.read_file()
    text = newText.clean_file(text)
    text = newText.sort_file(text)
    print(text)


if __name__ == "__main__":
    main()        

 
