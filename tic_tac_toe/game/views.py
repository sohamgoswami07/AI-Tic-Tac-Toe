from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .ai import get_best_move, check_winner

def game_page(request):
    return render(request, 'game.html')

@csrf_exempt
def ai_move(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        board = data['board']
        move = get_best_move(board)

        if move:
            board[move[0]][move[1]] = 'O'

        winner = check_winner(board)
        return JsonResponse({'board': board, 'winner': winner})
