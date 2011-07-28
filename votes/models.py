from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField("Title", max_length=256, unique=True)
    owned = models.BooleanField("Owned", default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title',]

class Vote(models.Model):
    game = models.ForeignKey(Game, db_index=True)
    count = models.PositiveIntegerField("Vote Count", default=0, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.game.title + "has" + str(self.count) + "votes"

    class Meta:
        unique_together = ('id', 'game')