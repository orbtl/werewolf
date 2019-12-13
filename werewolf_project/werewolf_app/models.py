from django.db import models
from login_app.models import User

class GameManager(models.Manager):
    def count_special_roles(self, postData):
        #for total special roles we skip accursed_one because the number is taken out of num_werewolves.  We can add booleans because True acts as 1 and False acts as 0.  We add twins twice because it creates two special role players
        total_special_roles = (postData['num_werewolves'] + postData['seer'] + postData['witch'] + postData['cupid'] + postData['defender'] + postData['hunter'] + postData['twins'] + postData['twins'] + postData['village_idiot'] + postData['wild_child'] + postData['little_child'] + postData['rusty_knight'] + postData['elder'] + postData['angel'] + postData['gypsy'])
        return total_special_roles

    def game_validator(self, postData):
        errors = {}
        if postData['max_players'] < 2 or postData['max_players'] > 100:
            errors['max_players'] = "Please enter a valid number between 2 and 100 for max # of players"
        if postData['num_werewolves'] < 1 or postData['num_werewolves'] >= postData['max_players']:
            errors['num_werewolves'] = "Number of werewolves must be at least 1 and less than your max # of players"
        total_special_roles = self.count_special_roles(postData)
        if total_special_roles > postData['max_players']:
            errors['special_roles'] = "The number of non-villager roles you specified exceeds your maximum # of players"
        return errors

    def start_game_validator(self, postData, gameID):
        errors = self.game_validator(postData)
        current_player_count = (len(Game.objects.get(id=gameID)) - 1) # subtract 1 to not count host
        total_special_roles = self.count_special_roles(postData)
        if total_special_roles > current_player_count:
            errors['special_roles_exceeds_players'] = "The number of non-villager roles you specified exceeds your currently connected players"
        if current_player_count > postData['max_players']:
            errors['too_many_players'] = "There are more players connected than you are allowing in your max # of players... kick someone?"
        return errors

    def updateGame(self, postData, gameID, userID):
        errors = {}
        gameList = Game.objects.filter(id=GameID)
        if len(gameList) == 0: # prevent errors from users typing in an address of a non-existing game id
            errors['nogame'] = "No game with that ID found"
            return errors
        currUser = User.objects.get(id=userID)
        thisGame = gameList[0]
        if thisGame.started == True or thisGame.ended == True: # prevent hosts from updating a game after it started or ended
            errors['gameNotAvail'] = "This game can no longer be edited"
            return errors
        if thisGame.host != currUser:
            errors['notYourGame'] = "You cannot edit a game you did not create!")
            return errors
        furtherErrors = Game.objects.game_validator(postData)
        if len(furtherErrors) > 0:
            for error in furtherErrors:
                errors[error] = furtherErrors[error]
            return errors
        if len(errors) == 0 and len(furtherErrors) == 0: # actually update
            thisGame.max_players = postData['max_players']
            thisGame.num_werewolves = postData['num_werewolves']
            thisGame.has_village_idiot = postData['village_idiot']
            thisGame.has_cupid = postData['cupid']
            thisGame.has_lovers = postData['cupid'] # based on whether cupid is there or not
            thisGame.has_twins = postData['twins']
            thisGame.has_accursed_one = postData['accursed_one']
            thisGame.has_seer = postData['seer']
            thisGame.has_witch = postData['witch']
            thisGame.has_defender = postData['defender']
            thisGame.has_hunter = postData['hunter']
            thisGame.has_wild_child = postData['wild_child']
            thisGame.has_role_model = postData['role_model']
            thisGame.has_little_child = postData['little_child']
            thisGame.has_rusty_knight = postData['rusty_knight']
            thisGame.has_elder = postData['elder']
            thisGame.has_angel = postData['angel']
            thisGame.has_gypsy = postData['gypsy']
            thisGame.allow_spectators = postData['allow_spectators']
            thisGame.save()
        return errors
        
        

class Game(models.Model):
    objects = GameManager()
    # Game Options:
    max_players = models.IntegerField(default=100)
    num_werewolves = models.IntegerField(default=2)
    has_village_idiot = models.BooleanField(default=False)
    has_cupid = models.BooleanField(default=True)
    has_lovers = models.BooleanField(default=True)
    has_twins = models.BooleanField(default=False)
    has_accursed_one = models.BooleanField(default=True)
    has_seer = models.BooleanField(default=True)
    has_witch = models.BooleanField(default=True)
    has_defender = models.BooleanField(default=True)
    has_hunter = models.BooleanField(default=False)
    has_wild_child = models.BooleanField(default=False)
    has_role_model = models.BooleanField(default=False)
    has_little_child = models.BooleanField(default=False)
    has_rusty_knight = models.BooleanField(default=False)
    has_elder = models.BooleanField(default=False)
    has_angel = models.BooleanField(default=False)
    has_gypsy = models.BooleanField(default=False)
    allow_spectators = models.BooleanField(default=True)
    # Game Properties:
    started = models.BooleanField(default=False) # whether the game has started or is still in lobby -- do we need this or can we just use turn number or phase?
    ended = models.BooleanField(default=False) # whether the game is over
    current_phase = models.CharField(max_length=45, default="Lobby") # Lobby, Night, Day
    current_turn = models.IntegerField(default=0) #what turn are we on
    winning_team = models.CharField(max_length=45, null=True) # for statistics, store who won this particular game in form of string such as "Villagers", "Werewolves", or "Lovers"
    join_key = models.CharField(max_length=45, null=True) # for joining a game manually by alphanumeric key
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Game Relationships:
    host = models.ForeignKey(User, related_name="games_hosted", on_delete=models.SET_NULL, null=True)
    players = models.ManyToManyField(User, related_name="games_joined") # I believe we need this in addition to roles for each player so we can have the players join the lobby before they are assigned roles.  I suppose an alternative owuld be to assign them a role initially by default that would be called something like "noRole" or "lobbyRole" etc
    # roles = each role associated with this game
    


class Role(models.Model):
    player = models.ForeignKey(User, related_name="roles", on_delete=models.SET_NULL, null=True)
    game = models.ForeignKey(Game, related_name="roles", on_delete=models.SET_NULL, null=True)
    isAlive = models.BooleanField(default=True)
    isBanned = models.BooleanField(default=False) # If we implement ban-from-game functionality we'll need this
    turn_died = models.IntegerField(null=True) # keep track of what turn the player died
    role_notes = models.CharField(max_length=255, null=True) # Not sure we'll need this, but I want it here in case we need to put special notes on a role a player played to explain that they became a werewolf from being turned by the accursed one, etc
    primary_ammo = models.IntegerField(default=0) # Used to keep track of whether special abilities have been used, such as the gypsy questions, or witch potion
    secondary_ammo = models.IntegerField(default=0) # Used to keep track of secondary special abilities, like witch's poison
    successes = models.IntegerField(default=0) # Used to keep track of things like how many times a seer correctly found a werewolf, etc
    isActivePlayer = models.BooleanField(default=True) # to deal with players being kicked?
    role_name = models.CharField(max_length=45, null=True) #Name of Role, choose from:
    secondary_role_name = models.CharField(max_length=45, null=True) # Need this for roles like Lover that can be used in conjunction with other roles like werewolf
    #role_name options: cupid,lover,werewolf,villager,village_idiot,twin,accursed_one,seer,witch,defender,hunter,wild_child,role_model,little_child,rusty_knight,elder,angel,gypsy
    












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
