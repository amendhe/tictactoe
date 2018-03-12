from django.db import models

from django.contrib.auth.models import User


class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="Invitations_sent", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,
                                related_name="Invitations_recived",
                                on_delete=models.CASCADE,
                                verbose_name="User To Invite",
                                help_text="Please select Opponent")
    message = models.CharField(max_length=300,
                               verbose_name="Optional Message",
                               help_text="  It's nice gesture to add friendly message before actual battle began .. ^.^"
                               )
    timestamp = models.DateTimeField(auto_now=True)
