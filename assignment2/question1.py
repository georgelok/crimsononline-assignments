import os
from os.path import basename
import json
from PIL import Image
import datetime
import re

class Content(object):
    '''
    Required properties:
        - title
        - subtitle
        - creator
        - publication date
    Required methods:
        - show
        - matches_url (question 1d)
    '''
    def __init__(self, title, subtitle, creator, year, month, day, slug) :
        self.title = title
        self.subtitle = subtitle
        self.creator = creator
        self.publicationdate = datetime.date(year,month,day)
        self.slug = slug


    def matches_url(self, url) :
        #We care mostly about the values after thecrimson.com
        pattern = r'http://thecrimson.com/(\w+)/(\d{4})/(\d{1,2})/(\d{1,2})/(\w+)/'
        match = re.search(pattern, url)
        if match :
            date = datetime.date(int(match.groups()[1]), int(match.groups()[2]), int(match.groups()[3]))
            if self.__class__.__name__ == match.groups()[0] and self.publicationdate == date and self.slug == match.groups()[4] :
                return True
            else :
                return False
        else :
            return False
    def show(self):
        print self.title + ':', self.subtitle
        print "By: ", self.creator
        print "Published on:", self.publicationdate

class Article(Content):
    '''
    Required properties:
        - All properties of Content
        - related_image
    Required methods:
        - All methods of Content
    '''
    def __init__(self, title, subtitle, creator, content, year, month, day, slug, image=None) :
        super(Article, self).__init__(title, subtitle, creator, year, month, day, slug)
        self.content = content
        self.related_image = image

    @classmethod
    def loadfile(cls, file) : #loads a properly formated json file.
        try:
            f = open(file, 'r')
            json_data = f.read()
            data = json.loads(json_data)
            title = data['title']       
            subtitle = data['subtitle']
            creator = data['creator']
            content = data['content']
            year = data['year']
            month = data['month']
            day = data['day']
            slug = data['slug']
            if data['image_url'] == '' :
                return cls(title, subtitle, creator, content, year, month, day, slug)
            else :
                image = Picture(data['image_title'], data['image_subtitle'], data['image_creator'], data['image_year'], data['image_month'], data['image_day'], data['image_url'])
                return cls(title, subtitle, creator, content, year, month, day, slug, image)

        except IOError :
            print 'File does not exists'

    def save(self) :
        name = self.title + "-" + self.creator
        try :
            f = open(name, 'r') #check to see if file exists
            f.close()
            print 'file already exists\n'
        except IOError :
            try : 
                f = open(name, 'w')
                output = {
                    'title' : self.title,
                    'subtitle' : self.subtitle,
                    'creator' : self.creator,
                    'content' : self.content,
                    'year' : self.publicationdate.year,
                    'month' : self.publicationdate.month,
                    'day' : self.publicationdate.day,
                    'slug' : self.slug
                }
                if self.related_image == None :
                    output.update({
                        'image_title' : '',
                        'image_subtitle' : '',
                        'image_url' : '',
                        'image_creator' : '',
                        'image_year' : '',
                        'image_month' : '',
                        'image_day' : '',
                    })
                else :
                    output.update({
                        'image_title' : self.related_image.title,
                        'image_subtitle' : self.related_image.subtitle,
                        'image_url' : self.related_image.image_file,
                        'image_creator' : self.related_image.creator,
                        'image_year' : self.related_image.publicationdate.year,
                        'image_month' : self.related_image.publicationdate.month,
                        'image_day' : self.related_image.publicationdate.day,                        

                    })
                json_output = json.dumps(output)
                f.write(json_output)
                print 'Write successful.\n'
            except IOError :
                print 'Could not open file to save\n'

    def show(self) :
        super(Article, self).show()
        print self.content
        if self.related_image != None :
            self.related_image.show()

    def __str__(self) :
        if self.related_image != None :
            self.related_image.show()
        return self.headline + '\nBy ' + self.creator + '\n\n' + self.content




class Picture(Content):
    '''
    Required properties:
        - All properties of Content
        - image_file
    Required methods:
        - All methods of Content
    '''

    def __init__(self, title, subtitle, creator, year, month, day, path) :
        #path without the extension is also the slug.
        fileName, ext = os.path.splitext(path)
        slug = os.path.basename(fileName)

        super(Picture, self).__init__(title, subtitle, creator, year, month, day, slug)
        self.image_file = path

    def show(self) :
        super(Picture, self).show()
        img = Image.open(self.image_file)
        img.show()

'''
Question 1e
'''
def from_url(c_lst, url):
    matches = [content for content in c_lst if content.matches_url(url)]
    if len(matches) > 1 :
        print "Error: too many matches"
        return None
    elif len(matches) == 1 :
        return matches[0]
    else :
        print "no match"
        return None

'''
Question 1e
'''
def posted_after(c_lst, dt):
    return [content for content in c_lst if content.publicationdate > dt]
