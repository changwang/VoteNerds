from django.db import models

# Create your models here.
class GameManager(models.Manager):
    """
    it would be helpful to create some customized query set methods.
    """
    def owned_list(self):
        """
        retrieves owned games.
        """
        return super(GameManager, self).get_query_set().filter(owned=True)

    def wish_list(self):
        """
        retrieves unowned games
        """
        return super(GameManager, self).get_query_set().filter(owned=False)

class Game(models.Model):
    """
    game model, represents xbox game.
    """
    title = models.CharField("Title", max_length=256, unique=True)
    owned = models.BooleanField("Owned", default=False)
    created = models.DateTimeField(auto_now_add=True)

    objects = GameManager()

    def __unicode__(self):
        return self.title

    class Meta:
        # by default, sorts games alphabetically
        ordering = ['title',]

class Vote(models.Model):
    """
    vote model, represents game vote.
    using count field to record the number of vote regarding the specific game.
    """
    game = models.OneToOneField(Game, primary_key=True)
    count = models.PositiveIntegerField("Vote Count", default=0, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.game.title + " has " + str(self.count) + " votes"
