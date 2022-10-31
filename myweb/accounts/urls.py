from django.urls import path
from .views import SignUpView, CustomLoginView, UserListView, BiographyView
from django.contrib.auth.views import LogoutView


urlpatterns = [path("sign-up", SignUpView.as_view(), name="sign-up"),
               path("login", CustomLoginView.as_view(), name="login"),
               path("logout", LogoutView.as_view(), name="logout"),
               path("users/<int:pk>", BiographyView.as_view(), name="user-detail"),
               path("users", UserListView.as_view(), name="user-list"),

]