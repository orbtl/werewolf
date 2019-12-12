from django.db import models
from login_app.models import User

class Game(models.Model):
    # Game Options:
    max_players = models.IntegerField()
    num_werewolves = models.IntegerField()
    # Game Properties:
    started = models.BooleanField(default=False)
    ended = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Game Relationships:
    host = models.ForeignKey(User, related_name="games_hosted", on_delete=models.SET_NULL, null=True)
    players = models.ManyToManyField(User, related_name="games_joined")
    werewolves = models.ManyToManyField(User, related_name="games_werewolf")
    villagers = models.ManyToManyField(User, related_name="games_villager")
    village_idiot = models.ForeignKey(User, related_name="games_village_idiot", on_delete=models.SET_NULL, null=True)
    cupid = models.ForeignKey(User, related_name="games_cupid", on_delete=models.SET_NULL, null=True)
    lovers = models.ManyToManyField(User, related_name="games_lover")
    twins = models.ManyToManyField(User, related_name="games_twin")
    accursed_one = models.ForeignKey(User, related_name="games_accursed_one", on_delete=models.SET_NULL, null=True)
    seer = models.ForeignKey(User, related_name="games_seer", on_delete=models.SET_NULL, null=True)
    witch = models.ForeignKey(User, related_name="games_witch", on_delete=models.SET_NULL, null=True)
    defender = models.ForeignKey(User, related_name="games_defender", on_delete=models.SET_NULL, null=True)
    hunter = models.ForeignKey(User, related_name="games_hunter", on_delete=models.SET_NULL, null=True)
    wild_child = models.ForeignKey(User, related_name="games_wild_child", on_delete=models.SET_NULL, null=True)
    role_model = models.ForeignKey(User, related_name="games_role_model", on_delete=models.SET_NULL, null=True) # this is purely for the wild_child
    little_child = models.ForeignKey(User, related_name="games_little_child", on_delete=models.SET_NULL, null=True)
    rusty_knight = models.ForeignKey(User, related_name="games_rusty_knight", on_delete=models.SET_NULL, null=True) # knight with the rusty sword
    elder = models.ForeignKey(User, related_name="games_elder", on_delete=models.SET_NULL, null=True)
    angel = models.ForeignKey(User, related_name="games_angel", on_delete=models.SET_NULL, null=True)
    gypsy = models.ForeignKey(User, related_name="games_gypsy", on_delete=models.SET_NULL, null=True)
    # Thought about doing this with another model called "Role" so each player has a role for each game they are in
    # When put in practice it meant every role just had one User and one Game associated with it
    # So this seemed unnecessary.  Went with ManyToMany relationships and OneToMany relationships
    # Instead of going with OneToMany and OneToOne relationships with the Role class addition

    # ROLES:
    # cupid
    # lovers
    # werewolves
    # villagers
    # village_idiot
    # twins
    # accursed_one
    # seer
    # witch
    # defender
    # hunter
    # wild_child
    # little_child
    # rusty_knight
    # elder
    # angel
    # gypsy
