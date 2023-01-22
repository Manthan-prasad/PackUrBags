from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('store/', views.store, name='store'),
    # path('login/', views.loginPage, name='login'),
    # path('register/', views.registerPage, name='register'),
    # path('',views.store, name="store"),
    path('cart/',views.cart, name="cart"),
    # path('cart/<int:packageId>/',views.cart, name="cart"),
    path('checkout/',views.checkout, name="checkout"),
    path('view/<int:packageId>/', views.view, name='view'),
    path('process_order/', views.processOrder, name='process_order'),
    path('update_Item/',views.updateItem, name="update_Item")
]

# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     # ...
#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
#     path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
#     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
#     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
#     # ...
# ]
