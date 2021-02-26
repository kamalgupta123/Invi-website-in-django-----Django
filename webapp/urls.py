from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register/$', views.register,name="register"),
    url(r'^send_otp/$', views.send_otp,name="send_otp"),
    url(r'^verify_otp/$', views.verify_otp,name="verify_otp"),
    url(r'^services/$', views.services,name="services"),
    url(r'^portfolio/$', views.portfolio,name="portfolio"),
    url(r'^blog/$', views.blog,name="blog"),
    url(r'^contact-us/$', views.contactus,name="contact-us"),
    url(r'^project-item/$', views.projectItem,name="projectItem"),
    url(r'^blog-item/$', views.blogItem,name="blogItem"),
    url(r'^no-page/$', views.noPageFound,name="noPageFound"),
    url(r'^$',views.index,name="index"),
]