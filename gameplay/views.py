from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Game
from .forms import MoveForm


@login_required
def game_detail(request, id):
    game = get_object_or_404(Game, pk=id)
    context = {'game': game}
    if game.is_users_move(request.user):
        context['form'] = MoveForm()

    if request.method == "POST":
        if "delete" in request.POST:
            game.delete()
            return redirect('player_home')

    return render(request,
                  "gameplay/game_detail.html",
                  context
                  )
