import os
from os.path import basename

from PIL import Image

class Article:
    '''
    Question 2a
        Properties:
            - headline
            - content
            - creator (author)
        Methods:
            - show (print contents)
            - save (save to text file)

    Question 2b
        Methods:
            - Load article from text file

    Question 2d
        Properties:
            - related_image
        Methods:
            - modify save to save info about related picture (if it exists)
            - modify load to load info about related picture (if it exists)
            - modify show to also show the related picture (if it exist)
    '''
    def __init__(self, headline, creator, content, image=None) :
        self.headline = headline
        self.creator = creator        
        self.content = content
        self.image = None

    @classmethod
    def loadfile(cls, file, creator, image=None) : #loads a file, using the file name as a title and the contents as content
        try:
            f = open(file, 'r')
            base = basename(file)
            headline = os.path.splitext(base)[0]
            content = f.read()
            f.close()
            return cls(headline, creator, content, image)
        except IOError :
            print "File does not exists"

    def save(self) :
        title = self.headline + "-" + self.creator
        try :
            f = open(title, 'r') #check to see if file exists
            f.close()
            print "file already exists\n"
        except IOError :
            try : 
                f = open(title, 'w')
                f.write(self.headline + "\nBy "  + self.creator + "\n\n" + self.content)
                print "Write successful.\n"
            except IOError :
                print "Could not open file to save\n"

    def __str__(self) :
        return self.headline + "\nBy " + self.creator + "\n\n" + self.content


    pass

class Picture:
    '''
    Question 2c
        Properties:
            - image_file (path to original image relative to this file)
            - creator (photographer)
         Methods
            - show (show image)
    '''
    def __init__(self, path, creator) :
        self.path = path
        self.creator = creator

    def show(self) :
        img = Image.open(self.path)
        img.show()

    pass
