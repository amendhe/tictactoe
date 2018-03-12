from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse

Game_status_choices = (
    ('F', 'First player Move',),
    ('S', 'Second Player to Move'),
    ('W', 'Win-First playter'),
    ('L', 'Second player wins'),
    ('D', 'Draw')
)


class GameQuerySet(models.QuerySet):

    def games_for_user(self, user):
        return self.filter(
            Q(first_player=user) | Q(second_player=user)
        )

    def active(self):
        return self.filter(
            Q(status='F') | Q(status='S')
        )


@python_2_unicode_compatible
class Game(models.Model):
    first_player = models.ForeignKey(User,
                                     related_name="gmaes_first_player", on_delete=models.CASCADE, )
    second_player = models.ForeignKey(User,
                                      related_name="gmaes_second_player", on_delete=models.CASCADE)

    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F', choices=Game_status_choices)
    objects = GameQuerySet.as_manager()

    def board(self):
        board = [[None for x in range(3)] for y in range(3)]

        for move in self.move_set.all():
            board[move.y][move.x] = move

        return board

    def is_users_move(self, user):
        return (user == self.first_player and self.status == 'F') or \
               (user == self.second_player and self.status == 'S')

    def get_absolute_url(self):
        return reverse('gameplay_detail', args=[self.id])

    def __str__(self):
        return "{0} vs {1}".format(self.first_player, self.second_player)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField(editable=False)
    game = models.ForeignKey(Game, editable=False, on_delete=models.CASCADE)
