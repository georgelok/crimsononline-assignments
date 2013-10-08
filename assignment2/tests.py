from question1 import *

# Testing Content, Article, and Picture classes.
# remember to delete test article-me3 to test saving.

c = Content("test content", "content subtitle", "me1", 2013, 7, 1, "slug1")
#c.show()

p = Picture("test picture", "picture subtitle", "me2", 2012, 10, 2, "test.png")
#p.show()

a= Article("test article", "article subtitle", "me3", "article content", 2011, 12, 3, "slug3", p)
#a.show()
#a.save()
#b = Article.loadfile("test article-me3")
#b.show()

content_list = [c,p,a]
#content_list = [c,p,a,b] #with one duplicate

# Test for from_url:
print 'TESTING from_url'
url1 = r'http://thecrimson.com/Content/2013/7/1/slug1/'
url2 = r'http://thecrimson.com/Picture/2012/10/2/test/'
url3 = r'http://thecrimson.com/Article/2011/12/3/slug3/'
c1 = from_url(content_list, url1)
c2 = from_url(content_list, url2)
c3 = from_url(content_list, url3)
 
print 'CONTENT MATCHING {0}:'.format(url1)
if c1:
	c1.show()
print '\nCONTENT MATCHING {0}:'.format(url2)
if c2:
	c2.show()
print '\nCONTENT MATCHING {0}:'.format(url3)
if c3:
    c3.show()

print '\n'

#Test for posted_after:
print 'TESTING posted_after'
time1 = datetime.date(2013,6,30)
time2 = datetime.date(2012,9,9)
time3 = datetime.date(2011,6,30)
 
print 'CONTENT POSTED AFTER {0}'.format(time1)
for c in posted_after(content_list, time1):
    c.show()
print '\nCONTENT POSTED AFTER {0}'.format(time2)
for c in posted_after(content_list, time2):
    c.show()
print '\nCONTENT POSTED AFTER {0}'.format(time3)
for c in posted_after(content_list, time3):
    c.show()
