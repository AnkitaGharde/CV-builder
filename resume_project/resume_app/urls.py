from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('make_cv/',views.make_cv,name='make_cv'),
    path('show_cv/', views.show_cv, name='show_cv'),
    # path('<int:id>/', views.get_resume, name='get_resume'),

    path('signup/', views.registerPage, name="signup"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
    # path('<int:id>/', views.cv, name="cv"),


    path('pdf_view/(?P<id>[0-9]+)/$', views.ViewPDF.as_view(), name="pdf_view"),

    # path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),

]