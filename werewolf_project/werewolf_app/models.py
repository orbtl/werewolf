from django.db import models
from login_app.models import User
import random

class GameManager(models.Manager):
    def roleDescription(self, role):
        desc = ""
        if role.role_name == "Werewolf":
            desc = "Each night, the Werewolves bite, kill and devour one Villager. During the day they try to conceal their identity and vile deeds from the Villagers.  The werewolves win when no villager-based roles are left in the game."
        if role.role_name == "Villager":
            desc = "As a villager, you do not have any special abilities.  There are werewolves in your midst, and your goal is to identify and eliminate them, using only your wit.  Each day, you will have the opportunity to come to a consensus with your fellow villagers and vote to kill one of your own that you suspect is secretly a werewolf.  Choose wisely!  You win the game if you eliminate all werewolves from the game."
        if role.role_name == "Village Idiot":
            desc = "What is a village without an Idiot? You do pretty much nothing important, but you are so charming that no one would want to hurt you....\n If the village votes against you, you are revealed as the Village Idiot. At that moment the Villagers understand their mistake and immediately let you be. From now on you continue to play, but may no longer vote. As what would the vote of an idiot be worth....\n Keep in mind that if the Werewolves devour you, you are dead."
        if role.role_name == "Cupid":
            desc = "Cupid is the village matchmaker. YOu received the nickname because of your ability to make any two people fall in love instantly. During the first night of the game, Cupid designates two players who will be in 'in love' with one another for the rest of the game. Cupid can choose themself as one of the lovers. If one of the lovers dies, the other immediately kills him/herself in a fit of grief. A love cannot, even as a bluff, vote to lynch their lover."
        if role.role_name == "Twin":
            desc = "You are one of two Twins in this game. The Twins get along like the fingers of the hand or the hair in a lock. It's certainly encouraging to have someone close you can trust in these uncertain times! The first night, when called by the Host, you wake up together and recognize each other as fellow villagers."
        if role.role_name == "Accursed One":
            desc = "You have just woken up from a long sleep and are ready to devour. You act as a regular werewolf with the exception that once per game, after the werwolves fall asleep the Host will ask if you would like to use your special powers to save the victim from death by instead turning them into a Werewolf. Choose wisely - for your power disappears after it has been used. "
        if role.role_name == "Seer":
            desc = "Each night, you see the humanity of a player of your choice. You will receive a yes or no response from the game moderator letting you know if your chosen player is a werewolf or not.  You must help the other Villagers, but remain discreet in order not to be unmasked by the Werewolves."
        if role.role_name == "Witch":
            desc = "The Witch is a villager who knows how to make two very powerful potions.  The first is a healing potion, which can be used to resurrect a player that is killed by a Werewolf. The second is a poison, used during the night to eliminate one player.  Each potion can be only used once per game. You can use either potion on yourself if you wish."
        if role.role_name == "Defender":
            desc = "You can save the Villagers from the bite of the Werewolves... Each night you are called before the Werewolves.  You then point out a player to the Host. The player thus chosen will be protected during the night (and only during the night) against the Werewolves. Even if chosen by them, the player will not be eliminated from the game.  You can protect yourself, however you are not able to defend the same player 2 nights in a row. "
        if role.role_name == "Hunter":
            desc = "The Hunter is a villager with special abilities. If you are killed by the Werewolves, or lynched by the Villagers, you can retalitate. With your dying breath, you will shoot, thus eliminating, any one other player."
        if role.role_name == "Wild Child":
            desc = "Abandoned in the woods by your parents, at a young age you were raised by wolves. As soon as you learned to walk you began to explore the Village. The community was moved by your frailty and adopted you. You are currently a Villager and on the first night, once called by the Host, you will choose a player to be your role model.  As long as your role model is alive, you are a villager. \nIF during the game your role model is eliminated, you become a Werewolf and will wake up the next night with your peers and devour with them until the end of the game."
        if role.role_name == "Little Child":
            desc = "The Little Child is a villager who is very curious. You can open your eyes during the night to spy on the Werewolves. However, if you are caught in the act by the Werewolves, you immediately die of fright, silently, instead of the designated victim. You can spy during the night only during the 'Werewolves awaking' phase. When the Little Child is in play, it is necessary for all players to avoid hiding their faces when sleeping (and instead just close their eyes)."
        if role.role_name == "Knight with the Rusty Sword":
            desc = "'Don Sneezy' as they like to call you, is an old retired knight. You are rather tired by a life of questing throughout the world and you just simply don't maintain your noble sword very well anymore. Rust has slowly started to settle on your protector's dull edge, but you'll never leave it for another. \n If you are devoured, as you lay dying you contaminate one of the Werewolves with your trusty rusty sword. \n A random Werewolf will now be infected with tetanus and will survive his wound for the day, but succumb at night."
        if role.role_name == "Elder":
            desc = "You have victoriously gone through all of life's terrible trials, and have gained an uncommon resistance! The Werewolves have to try twice to devour you! \n The first time you are defvoured by the Werewolves, you survive. \n You are only eliminated when devoured a second time. \n The Villager's vote, Witch's poison, and the Hunter's shot will all kill you the first time, BUT, despairing from having killed such a fount of knowledge, the Villagers all lose their special powers for the rest of the game. "
        if role.role_name == "Angel":
            desc = "The muddy life of a village infested with evil creatures repulses you. You only wish to escape this terrible nightmare and wake up in your comfortable bed. If you manage to attract the discriminatory vote of the villagers or the devouring vindictiveness of the lycanthropes to be eliminated on the first turn, you will then be able to leave the nightmare as the winner of the game! \n If you fail, you are reduced to a simple villager the rest of the game."
        if role.role_name == "Gypsy":
            desc = "You are Esmeralda's sister, who is simply called The Gypsy and you know the ways of the Great Beyond. You simply have to, with no artifice or unguent, concentrate and gaze upon the sky during the new moon to communicate with the souls of the departed\n Each night, the Host will ask if you would like you use your power. If affirmative, you may be given a choice of yes/no questions to ask the departed players. This ability may be used 5 times per game, but only once per night. "
        if role.secondary_role_name == "Lover":
            desc += "\n \n You have been destined by Cupid to fall in love!  You now care more about the welfare of your lover than anyone else in the game.  You may not vote in favor of your lover being lynched during the day phase!  If your lover dies, you simply cannot go on, and you take your own life." 
        return desc


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


    def calcKilled(self, request, gameID, gamePhase, postData):
        game = Game.objects.get(id=gameID)
        phase = game.current_phase
        aliveRoles = game.roles.filter(isAlive=True)
        oldAliveRoles = []
        angelWon = False
        for role in aliveRoles:
            oldAliveRoles.append(role)

        # store initializing of secondary roles
        if 'lover1' in postData:
            loverToSet1 = Role.objects.get(id=postData['lover1'])
            loverToSet2 = Role.objects.get(id=postData['lover2'])
            loverToSet1.secondary_role_name = "Lover"
            loverToSet2.secondary_role_name = "Lover"
            loverToSet1.save()
            loverToSet2.save()
        
        if 'role_model' in postData:
            roleModel = Role.objects.get(id=postData['role_model'])
            roleModel.isRoleModel = True
            roleModel.save()
        
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
            tetanusList = aliveRoles.filter(hasTetanus = True)
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
                    witchPoisonTarget.isAlive = False
                    witchPoisonTarget.turn_died = game.current_turn
                    witchPoisonTarget.save()
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
                if wwTarget.isRoleModel == True:
                    wildChildList = aliveRoles.filter(role_name="Wild Child")
                    if len(wildChildList) > 0:
                        wildChildList[0].role_notes = "Wild Child - Your Role before being turned"
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
                    wwList = aliveRoles.filter(role_name="Werewolf")
                    aoList = aliveRoles.filter(role_name="Accursed One")
                    wwArr = []
                    if len(wwList) > 0:
                        for ww in wwList: wwArr.append(ww)
                    if len(aoList) > 0:
                        wwArr.append(aoList[0])
                    randIndex = random.randint(0, len(wwArr), 1)
                    wwArr[randIndex].hasTetanus = True
                    wwArr[randIndex].save()


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
            if voteTarget.isRoleModel == True:
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
                    loverList[0].turn_died = game.current_turn
                    loverList[0].save()
                    loverList[1].isAlive = False
                    loverList[1].turn_died = game.current_turn
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
                voteTarget = None
            # kill the target
            if voteTarget != None:
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
            if hunterTarget.isRoleModel == True:
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
                    loverList[0].turn_died = game.current_turn
                    loverList[0].save()
                    loverList[1].isAlive = False
                    loverList[1].turn_died = game.current_turn
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
        playersStillAlive = len(game.roles.exclude(player=game.host).filter(isAlive=True))
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
    isRoleModel = models.BooleanField(default=False) #store if role is wild child's role model
    hasTetanus = models.BooleanField(default=False) # store if werewolf has tetanus
    #role_name options: cupid,lover,werewolf,villager,village_idiot,twin,accursed_one,seer,witch,defender,hunter,wild_child,role_model,little_child,rusty_knight,elder,angel,gypsy
    
