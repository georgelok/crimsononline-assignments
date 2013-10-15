from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('blogger.views',

    # Homepage is just static HTML so skip view and directly render the template
    url(r'^$', TemplateView.as_view(template_name="home.html")),

    # View all posts
    url(r'^posts/$', 'all_posts'),

    # View a specific post
    url(r'^posts/(?P<post_id>\d*)/$', 'blog_post'),

    # Create a post
    url(r'^posts/create/$', 'create'),

    # Page that handles data sent by /posts/create
    url(r'^posts/create/submit/$', 'save_post'),

    # View all authors
    url(r'^authors/$', 'all_authors'),

    # View all posts by one author
    url(r'^authors/(?P<author_id>\d*)/$', 'author'),
    
)
