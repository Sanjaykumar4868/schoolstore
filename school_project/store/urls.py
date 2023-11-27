from django.urls import path
from store import views

urlpatterns = [   
    path('',views.Home,name="home"),
    path('add/', views.person_create_view, name='person_add'),
    path('success/',views.Success,name="success"),
    path('login/',views.Login_page,name="Login_page"),
    path('logout/',views.Logout_view,name="Logout_view"),
    path('register/',views.Register_page,name="Register_page"),
    path('<slug:c_slug>/',views.allProdCat,name="department_by_category"),
    

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
    
]