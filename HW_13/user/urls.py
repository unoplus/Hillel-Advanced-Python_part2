from django.urls import path
from .views import UserEditView, UserSignUpView

urlpatterns = [
    path('sign_up/', UserSignUpView.as_view(), name='sign_up'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]