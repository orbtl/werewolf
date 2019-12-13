from django.db import models
from login_app.models import User

class Game(models.Model):
    # Game Options:
    max_players = models.IntegerField(default=100)
    num_werewolves = models.IntegerField(default=0)
    has_village_idiot = models.BooleanField(default=False)
    has_cupid = models.BooleanField(default=False)
    has_lovers = models.BooleanField(default=False)
    has_twins = models.BooleanField(default=False)
    has_accursed_one = models.BooleanField(default=False)
    has_seer = models.BooleanField(default=False)
    has_witch = models.BooleanField(default=False)
    has_defender = models.BooleanField(default=False)
    has_hunter = models.BooleanField(default=False)
    has_wild_child = models.BooleanField(default=False)
    has_role_model = models.BooleanField(default=False)
    has_little_child = models.BooleanField(default=False)
    has_rusty_knight = models.BooleanField(default=False)
    has_elder = models.BooleanField(default=False)
    has_angel = models.BooleanField(default=False)
    has_gypsy = models.BooleanField(default=False)
    allow_spectators = models.BooleanField(default=False)
    # Game Properties:
    started = models.BooleanField(default=False) # whether the game has started or is still in lobby -- do we need this or can we just use turn number or phase?
    ended = models.BooleanField(default=False) # whether the game is over
    current_phase = models.CharField(max_length=45, default="Lobby") # Lobby, Night, Day
    current_turn = models.IntegerField(default=0) #what turn are we on
    winning_team = models.CharField(max_length=45, null=True) # for statistics, store who won this particular game in form of string such as "Villagers", "Werewolves", or "Lovers"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Game Relationships:
    host = models.ForeignKey(User, related_name="games_hosted", on_delete=models.SET_NULL, null=True)
    players = models.ManyToManyField(User, related_name="games_joined") # I believe we need this in addition to roles for each player so we can have the players join the lobby before they are assigned roles.  I suppose an alternative owuld be to assign them a role initially by default that would be called something like "noRole" or "lobbyRole" etc
    
    


class Role(models.Model):
    player = models.ForeignKey(User, related_name="roles", on_delete=models.SET_NULL, null=True)
    game = models.ForeignKey(Game, related_name="roles", on_delete=models.SET_NULL, null=True)
    isAlive = models.BooleanField(default=True)
    turn_died = models.IntegerField(null=True) # keep track of what turn the player died
    role_notes = models.CharField(max_length=255, null=True) # Not sure we'll need this, but I want it here in case we need to put special notes on a role a player played to explain that they became a werewolf from being turned by the accursed one, etc
    primary_ammo = models.IntegerField(default=0) # Used to keep track of whether special abilities have been used, such as the gypsy questions, or witch potion
    secondary_ammo = models.IntegerField(default=0) # Used to keep track of secondary special abilities, like witch's poison
    isActivePlayer = models.BooleanField(default=True) # to deal with players being kicked?
    role_name = models.CharField(max_length=45, null=True) #Name of Role, choose from:
    secondary_role_name = models.CharField(max_length=45, null=True) # Need this for roles like Lover that can be used in conjunction with other roles like werewolf
    #role_name options: cupid,lover,werewolf,villager,village_idiot,twin,accursed_one,seer,witch,defender,hunter,wild_child,role_model,little_child,rusty_knight,elder,angel,gypsy
    












    ### this was the old setup of relationships
    # roles = each role associated with this game
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
