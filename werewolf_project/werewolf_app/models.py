from django.db import models
from login_app.models import User
import random

class GameManager(models.Manager):
    def count_special_roles(self, postData):
        #for total special roles we skip accursed_one because the number is taken out of num_werewolves.  We add twins twice because it creates two special role players
        total_special_roles = (int(postData['num_werewolves']) + int(postData['seer']) + int(postData['witch']) + int(postData['cupid']) + int(postData['defender']) + int(postData['hunter']) + int(postData['twins']) + int(postData['twins']) + int(postData['village_idiot']) + int(postData['wild_child']) + int(postData['little_child']) + int(postData['rusty_knight']) + int(postData['elder']) + int(postData['angel']) + int(postData['gypsy']))
        return total_special_roles

    def randomizeRoles(self, thisGame):
        gameRoles = thisGame.roles.exclude(player=thisGame.host)
        roleArray = []
        numWerewolves = thisGame.num_werewolves
        if thisGame.has_accursed_one == True:
            numWerewolves -= 1
            roleArray.append("Accursed One")
        for i in range(numWerewolves):
            roleArray.append("Werewolf")
        if thisGame.has_village_idiot:
            roleArray.append("Village Idiot")
        if thisGame.has_cupid:
            roleArray.append("Cupid")
        if thisGame.has_twins:
            roleArray.append("Twin")
            roleArray.append("Twin")
        if thisGame.has_seer:
            roleArray.append("Seer")
        if thisGame.has_witch:
            roleArray.append("Witch")
        if thisGame.has_defender:
            roleArray.append("Defender")
        if thisGame.has_hunter:
            roleArray.append("Hunter")
        if thisGame.has_wild_child:
            roleArray.append("Wild Child")
        if thisGame.has_little_child:
            roleArray.append("Little Child")
        if thisGame.has_rusty_knight:
            roleArray.append("Knight with the Rusty Sword")
        if thisGame.has_elder:
            roleArray.append("Elder")
        if thisGame.has_angel:
            roleArray.append("Angel")
        if thisGame.has_gypsy:
            roleArray.append("Gypsy")
        current_player_count = (len(thisGame.players.all()) - 1) # subtract 1 to not count host
        numVillagers = current_player_count - len(roleArray)
        for i in range(numVillagers):
            roleArray.append("Villager")
        # array of roles is built, now randomize:
        for role in gameRoles:
            roleIndex = random.randrange(0, len(roleArray), 1)
            role.role_name = roleArray.pop(roleIndex)
            role.save()
            if role.role_name == "Gypsy":
                role.primary_ammo = 5
            else:
                role.primary_ammo = 1
            role.secondary_ammo = 1
            role.save()
        return

    # def renderGamePhase(self, gameID):
    #     game = Game.objects.get(id=gameID)
    #     turn = game.current_turn
    #     phase = game.current_phase
    #     roles = game.roles.exclude(player=game.host)
    #     aliveRoles = game.roles.filter(isAlive=True)
    #     htmlArr = [] # this is where we will append all html to send to template for form inputs
    #     if phase == "Night": # determining form inputs to send to template
    #         if turn == 0: # initial game setup for special roles
    #             #night of turn 0
    #             if len(roles.filter(role_name="Cupid")) > 0:
    #                 htmlArr.append("<div class='form-group row align-items-center'>")
    #                 htmlArr.append("<label for='lover1' class='control-label col-md-5'>Lover 1</label>")
    #                 htmlArr.append("<select name='lover1' class='form-control col-md-7'>")
    #                 for role in aliveRoles.exclude(role_name="Cupid"):
    #                     htmlArr.append(f"<option value='{role.id}'>{role.player.username}</option>")
    #                 htmlArr.append("</select>")
    #                 htmlArr.append("<select name='lover2'>")
    #                 for role in aliveRoles.exclude(role_name="Cupid"):
    #                     htmlArr.append(f"<option value='{role.id}'>{role.player.username}</option>")
    #                 htmlArr.append("</select>")
    #             if len(roles.filter(role_name="Wild Child")) > 0:
    #                 htmlArr.append("<select name='role_model'>")
    #                 for role in aliveRoles.exclude(role_name="Wild Child"):
    #                     htmlArr.append(f"<option value='{role.id}'>{role.player.username}</option>")
    #                 htmlArr.append("</select>")
    #         # all nights
    #         if len(aliveRoles.filter(role_name="Werewolf")) == 0 and len(aliveRoles.filter(role_name="Accursed One")) == 0:
    #             # logic for vill WIN
    #         if (len(aliveRoles.filter(role_name="Werewolf")) + len(aliveRoles.filter(role_name="Accursed One"))) == len(aliveRoles.all()): 
    #             # werewolf win logic
    #         if len(aliveRoles.filter(role_name='Werewolf')) > 0:
    #             # werewolf logic
    #                 # who the target??
    #         if len(aliveRoles.filter(role_name='Accursed One')) > 0:
    #             # accursed logic
    #                 # turn or not
    #         if len(aliveRoles.filter(role_name='Little Child')) > 0:
    #             # little
    #                 # caught or not
    #         if len(aliveRoles.filter(role_name='Seer')) > 0:
    #             # seer
    #                 # target check
    #         if len(aliveRoles.filter(role_name='Witch')) > 0:
    #             # witch
    #                 # check ammo:
    #                     # if use potion?:
    #                     # posion use or not: 
    #                         # who?
    #         if len(aliveRoles.filter(role_name='Defender')) > 0:
    #             # defender
    #                 # check ammo
    #                     # does role's ID NOT match ID in stored in sec/ammo (stored in defender's Role.primary_ammo as ID of target)
    #                         # defend who?
    #                         # set sec/ammo to defended's ID
    #         if len(aliveRoles.filter(role_name='Gypsy')) > 0:
    #             # gypsy
    #                 # check ammo
    #                     # adjust ammo
    #         # increase turn counter
    #         # change phase to day

    #     if phase == "Day":
        
    #         # form for who the villagers vote to kill
    #             #calculate/reveal dead logic for vote:
    #                 #if angel is killed and it's day 1, angel wins
    #                 #if hunter is killed
    #                 #if village idiot was killed (and check village idiot ammo)
    #                 #if lover was killed
    #                 #if role model was killed
    #                 #if elder was killed (check ammo)

    def calcKilled(self, request, gameID, gamePhase, postData):
        game = Game.objects.get(id=gameID)
        turn = game.current_turn
        phase = game.current_phase
        roles = game.roles.exclude(player=game.host)
        aliveRoles = game.roles.filter(isAlive=True)
        oldAliveRoles = []
        angelWon = False
        for role in aliveRoles:
            oldAliveRoles.append(role)
        
        if phase == "Night":
        # calculate/reveal dead logic
            #check who was chosen to be killed
            wwTarget = Role.objects.get(id=postData['wwTargetID'])
            # initialize life savers
            targetSwitched = False
            witchUsedPotion = False
            littleChildCaught = False
            defTarget = None
            
            #check for previously infected tetanus here
            tetanusList = Role.objects.filter(role_notes="Tetanus")
            if len(tetanusList) > 0: # we know one is infected
                tetanusList[0].isAlive = False
                tetanusList[0].turn_died = game.current_turn
                tetanusList[0].save()
            
            #check if accursed one switched them to werewolf
            if 'targetSwitched' in postData:
                if postData['targetSwitched'] == "True":
                    targetSwitched = True
            #check if defender saved
            if 'defTargetID' in postData:
                defTarget = Role.objects.get(id=postData['defTargetID'])
                defender = aliveRoles.filter(role_name="Defender")[0]
                defender.primary_ammo = defTarget.id # set 'primary_ammo' to be id of defender's target
                defender.save()

            #check if witch saved
            if 'witchUsedPotion' in postData:
                if postData['witchUsedPotion'] == "True":
                    witchUsedPotion = True
            #check if witch killed
            if 'witchPoisonTargetID' in postData:
                witchPoisonTargetID = postData['witchPoisonTargetID']
                if witchPoisonTargetID != '0':
                    witchPoisonTarget = Role.objects.get(id=witchPoisonTargetID)
                    # kill witch poison target logic
            #check if little child was spotted
            if 'littleChildCaught' in postData:
                if postData['littleChildCaught'] == "True":
                    littleChildCaught = True
                if littleChildCaught == True:
                    wwTarget = Role.objects.filter(role_name="Little Child")[0]
            if targetSwitched == True: # Accursed one turns/switches the target instead of killing
                wwTarget.role_notes = "Role before being turned: " + wwTarget.role_name
                wwTarget.role_name = "Werewolf"
                wwTarget.save()
                wwTarget = None
            if defTarget == wwTarget:
                wwTarget = None
            if wwTarget != None:
                if wwTarget.role_name == "Elder":
                    if wwTarget.primary_ammo == 1:
                        wwTarget.primary_ammo = 0
                        wwTarget.save()
                        wwTarget = None
            if witchUsedPotion == True and targetSwitched == False:
                witch = Role.objects.filter(role_name="Witch")[0]
                witch.primary_ammo = 0
                witch.save()
                wwTarget = None
            if wwTarget != None: # confirm someone is dying
                print("someone is dying")
                if wwTarget.secondary_role_name == "Role Model":
                    wildChildList = aliveRoles.filter(role_name="Wild Child")
                    if len(wildChildList) > 0:
                        wildChildList[0].role_notes = "Role before being turned: Wild Child"
                        wildChildList[0].role_name = "Werewolf"
                        wildChildList[0].save()
                if wwTarget.secondary_role_name == "Lover":
                    loverList = aliveRoles.filter(secondary_role_name="Lover")
                    if len(loverList) > 0:
                        loverList[0].isAlive = False
                        loverList[0].turn_died = game.current_turn
                        loverList[0].save()
                        loverList[1].isAlive = False
                        loverList[1].turn_died = game.current_turn
                        loverList[1].save()
                if wwTarget.role_name == "Knight with the Rusty Sword":
                    pass
                    # infect werewolf with tetanus logic

                wwTarget.isAlive = False # actually kill the target
                wwTarget.turn_died = game.current_turn
                wwTarget.save()
                


                #checking if Hunter died during this calculation
                hunter = None
                for role in oldAliveRoles:
                    if role.role_name == "Hunter":
                        hunter = role
                if hunter != None:
                    hunter = Role.objects.get(id=hunter.id) # have to update sql object now that it might be dead
                    if hunter.isAlive == False:
                        game.current_phase = "Hunter"
                        game.save()
                        return True
            
                   
            #check if angel killed and it's day 2, angel wins
            if game.current_turn == 2:
                angelList = aliveRoles.filter(role_name="Angel")
                if len(angelList) > 0:
                    if angelList[0] == wwTarget:
                        angelWon = True
            
            game.current_phase = "Day"
            game.current_turn += 1
            game.save()
        
        if phase == "Day":
            voteTarget = Role.objects.get(id=postData['voteTarget'])

            # if turn 1 angel logic
            if game.current_turn == 1:
                if voteTarget.role_name== "Angel":
                    angelWon = True
            # role model logic
            if voteTarget.secondary_role_name == "Role Model":
                wildChildList = aliveRoles.filter(role_name="Wild Child")
                if len(wildChildList) > 0:
                    wildChildList[0].role_notes = "Role before being turned: Wild Child"
                    wildChildList[0].role_name = "Werewolf"
                    wildChildList[0].save()
            # lover logic
            if voteTarget.secondary_role_name == "Lover":
                loverList = aliveRoles.filter(secondary_role_name="Lover")
                if len(loverList) > 0:
                    loverList[0].isAlive = False
                    lowerList[0].turn_died = game.current_turn
                    loverList[0].save()
                    loverList[1].isAlive = False
                    lowerList[1].turn_died = game.current_turn
                    loverList[1].save()
            # elder logic
            if voteTarget.role_name == "Elder":
                villageList = aliveRoles.exclude(role_name="Werewolf").exclude(role_name="Accursed One")
                for villager in villageList:
                    villager.role_name = "Villager"
                    villager.primary_ammo = 0
                    villager.secondary_ammo = 0
                    villager.save()
            # village idiot logic
            if voteTarget.role_name == "Village Idiot":
                voteTarget.primary_ammo = 0 # use this to store that they were identified as the idiot and will show up on player list, and not be able to vote
                voteTarget.save()
            # kill the target
            voteTarget.isAlive = False
            voteTarget.turn_died = game.current_turn
            voteTarget.save()
            
           
            #checking if Hunter died during this calculation
            hunter = None
            for role in oldAliveRoles:
                if role.role_name == "Hunter":
                    hunter = role
            if hunter != None:
                hunter = Role.objects.get(id=hunter.id) # have to update sql object now that it might be dead
                if hunter.isAlive == False:
                    game.current_phase = "Hunter"
                    game.save()
                    return True
        

            game.current_phase = "Night"
            game.save()

        if phase == "Hunter":
            hunterTarget = Role.objects.get(id=postData['hunterTarget'])
            # role model logic
            if hunterTarget.secondary_role_name == "Role Model":
                wildChildList = aliveRoles.filter(role_name="Wild Child")
                if len(wildChildList) > 0:
                    wildChildList[0].role_notes = "Role before being turned: Wild Child"
                    wildChildList[0].role_name = "Werewolf"
                    wildChildList[0].save()
            # lover logic
            if hunterTarget.secondary_role_name == "Lover":
                loverList = aliveRoles.filter(secondary_role_name="Lover")
                if len(loverList) > 0:
                    loverList[0].isAlive = False
                    lowerList[0].turn_died = game.current_turn
                    loverList[0].save()
                    loverList[1].isAlive = False
                    lowerList[1].turn_died = game.current_turn
                    loverList[1].save()
            hunterTarget.isAlive = False
            hunterTarget.turn_died = game.current_turn
            hunterTarget.save()
            if postData['prevPhase'] == "Day":
                game.current_phase = "Night"
                game.save()
            if postData['prevPhase'] == "Night":
                game.current_phase = "Day"
                game.current_turn += 1
                game.save()
        
        # calculate if game is over
        if angelWon == True:
            game.ended = True
            game.winning_team = "Angel wins it for the villagers!"
        badGuys = len(game.roles.filter(role_name="Werewolf").filter(isAlive=True)) + len(game.roles.filter(role_name="Accursed One").filter(isAlive=True))
        print('badguys: ', badGuys)
        playersStillAlive = len(game.roles.exclude(player=game.host).filter(isAlive=True))
        print('playerstillalive: ', playersStillAlive)
        if badGuys == playersStillAlive:
            game.ended = True
            game.winning_team = "Werewolves Win!"
        if badGuys == 0:
            game.ended = True
            game.winning_team = "Villagers Win!"
        game.save()
        return False
            





    def game_validator(self, postData):
        errors = {}
        max_players = int(postData['max_players'])
        num_werewolves = int(postData['num_werewolves'])
        if max_players < 2 or max_players > 100:
            errors['max_players'] = "Please enter a valid number between 2 and 100 for max # of players"
        if num_werewolves < 1 or num_werewolves >= max_players:
            errors['num_werewolves'] = "Number of werewolves must be at least 1 and less than your max # of players"
        total_special_roles = self.count_special_roles(postData)
        if total_special_roles > max_players:
            errors['special_roles'] = "The number of non-villager roles you specified exceeds your maximum # of players"
        return errors

    def updateGame(self, postData, gameID, userID):
        errors = {}
        gameList = Game.objects.filter(id=gameID)
        if len(gameList) == 0: # prevent errors from users typing in an address of a non-existing game id
            errors['nogame'] = "No game with that ID found"
            return errors
        currUser = User.objects.get(id=userID)
        thisGame = gameList[0]
        if thisGame.started == True or thisGame.ended == True: # prevent hosts from updating a game after it started or ended
            errors['gameNotAvail'] = "This game can no longer be edited or started"
            return errors
        if thisGame.host != currUser:
            errors['notYourGame'] = "You cannot edit or start a game you did not create!"
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
            thisGame.has_role_model = postData['wild_child'] # based on whether there's a wild child
            thisGame.has_little_child = postData['little_child']
            thisGame.has_rusty_knight = postData['rusty_knight']
            thisGame.has_elder = postData['elder']
            thisGame.has_angel = postData['angel']
            thisGame.has_gypsy = postData['gypsy']
            thisGame.allow_spectators = postData['allow_spectators']
            thisGame.save()
        return errors
        
    def startGame(self, postData, gameID, userID):
        errors = self.updateGame(postData, gameID, userID)
        thisGame = Game.objects.get(id=gameID)
        current_player_count = (len(thisGame.players.all()) - 1) # subtract 1 to not count host
        total_special_roles = self.count_special_roles(postData)
        if total_special_roles > current_player_count:
            errors['special_roles_exceeds_players'] = "The number of non-villager roles you specified exceeds your currently connected players"
        if current_player_count > int(postData['max_players']):
            errors['too_many_players'] = "There are more players connected than you are allowing in your max # of players... kick someone?"
        if len(errors) == 0: #actually start the game
            thisGame.started = True
            thisGame.current_phase = "Night"
            thisGame.save()
            # randomize roles
            self.randomizeRoles(thisGame)

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
