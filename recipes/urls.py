from django.urls import path
from recipes.views import home, sobre, contato, receitas

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
    path('receita/', receitas, name='receitas')
]