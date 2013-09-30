import os
from os.path import basename
import json
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
        self.related_image = image

    @classmethod
    def loadfile(cls, file) : #loads a properly formated json file.
        try:
            f = open(file, 'r')
            json_data = f.read()
            data = json.loads(json_data)
            headline = data['headline']            
            content = data['content']
            creator = data['creator']
            if data['image_url'] == '' :
                return cls(headline, creator, content)
            else :
                image = Picture(data['image_url'], data['image_creator'])
                cls(headline, creator, content, image)            
                return cls(headline, creator, content, image)
        except IOError :
            print 'File does not exists'

    def save(self) :
        title = self.headline + "-" + self.creator
        try :
            f = open(title, 'r') #check to see if file exists
            f.close()
            print 'file already exists\n'
        except IOError :
            try : 
                f = open(title, 'w')
                if self.related_image == None :
                    output = {
                        'headline' : self.headline,
                        'creator' : self.creator,
                        'content' : self.content,
                        'image_url' : '',
                        'image_creator' : ''
                    }
                else :
                    output = {
                        'headline' : self.headline,
                        'creator' : self.creator,
                        'content' : self.content,
                        'image_url' : self.related_image.image_file,
                        'image_creator' : self.related_image.creator
                    }
                json_output = json.dumps(output)
                f.write(json_output)
                print 'Write successful.\n'
            except IOError :
                print 'Could not open file to save\n'

    def __str__(self) :
        if self.related_image != None :
            self.related_image.show()
        return self.headline + '\nBy ' + self.creator + '\n\n' + self.content


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
        self.image_file = path
        self.creator = creator

    def show(self) :
        img = Image.open(self.image_file)
        img.show()

    pass
