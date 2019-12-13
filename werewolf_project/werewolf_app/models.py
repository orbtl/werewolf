from django.db import models
from login_app.models import User

class Role(models.Model):
    player = models.ForeignKey(User, related_name="roles", on_delete=models.SET_NULL, null=True)
    game = models.ForeignKey(Game, related_name="roles", on_delete=models.SET_NULL, null=True)
    isAlive = models.BooleanField(default=True)
    isActivePlayer = models.BooleanField(default=True) # to deal with players being kicked?
    role_name = models.CharField(max_length=45) #Name of Role, choose from:
    #role_name options: cupid,lover,werewolf,villager,village_idiot,twin,accursed_one,seer,witch,defender,hunter,wild_child,role_model,little_child,rusty_knight,elder,angel,gypsy
    

class Game(models.Model):
    # Game Options:
    max_players = models.IntegerField()
    num_werewolves = models.IntegerField()
    # Game Properties:
    started = models.BooleanField(default=False) # whether the game has started or is still in lobby -- do we need this or can we just use turn number or phase?
    ended = models.BooleanField(default=False) # whether the game is over
    current_phase = models.CharField(max_length=45, default="Lobby") # Lobby, Night, Day
    current_turn = models.IntegerField(default=0) #what turn are we on
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Game Relationships:
    host = models.ForeignKey(User, related_name="games_hosted", on_delete=models.SET_NULL, null=True)
    players = models.ManyToManyField(User, related_name="games_joined")
    # roles = each role associated with this game
    











    ### this was the old setup of relationships
    # werewolves = models.ManyToManyField(User, related_name="games_werewolf")
    # villagers = models.ManyToManyField(User, related_name="games_villager")
    # village_idiot = models.ForeignKey(User, related_name="games_village_idiot", on_delete=models.SET_NULL, null=True)
    # cupid = models.ForeignKey(User, related_name="games_cupid", on_delete=models.SET_NULL, null=True)
    # lovers = models.ManyToManyField(User, related_name="games_lover")
    # twins = models.ManyToManyField(User, related_name="games_twin")
    # accursed_one = models.ForeignKey(User, related_name="games_accursed_one", on_delete=models.SET_NULL, null=True)
    # seer = models.ForeignKey(User, related_name="games_seer", on_delete=models.SET_NULL, null=True)
    # witch = models.ForeignKey(User, related_name="games_witch", on_delete=models.SET_NULL, null=True)
    # defender = models.ForeignKey(User, related_name="games_defender", on_delete=models.SET_NULL, null=True)
    # hunter = models.ForeignKey(User, related_name="games_hunter", on_delete=models.SET_NULL, null=True)
    # wild_child = models.ForeignKey(User, related_name="games_wild_child", on_delete=models.SET_NULL, null=True)
    # role_model = models.ForeignKey(User, related_name="games_role_model", on_delete=models.SET_NULL, null=True) # this is purely for the wild_child
    # little_child = models.ForeignKey(User, related_name="games_little_child", on_delete=models.SET_NULL, null=True)
    # rusty_knight = models.ForeignKey(User, related_name="games_rusty_knight", on_delete=models.SET_NULL, null=True) # knight with the rusty sword
    # elder = models.ForeignKey(User, related_name="games_elder", on_delete=models.SET_NULL, null=True)
    # angel = models.ForeignKey(User, related_name="games_angel", on_delete=models.SET_NULL, null=True)
    # gypsy = models.ForeignKey(User, related_name="games_gypsy", on_delete=models.SET_NULL, null=True)
    
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
