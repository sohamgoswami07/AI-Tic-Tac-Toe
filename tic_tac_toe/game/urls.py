from django.urls import path
from .views import game_page, ai_move

urlpatterns = [
    path('', game_page, name='game'),
    path('api/ai-move/', ai_move, name='ai-move'),
]
