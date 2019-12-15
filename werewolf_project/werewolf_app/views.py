from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Game, Role
import random #for random key generation
import string #for easy random key string generation
import bcrypt

def randomKey():
    charsAllowed = (string.ascii_uppercase + string.digits)
    return ''.join(random.choice(charsAllowed) for i in range(5))

def homeIndex(request): # Main Home Page
    if 'userID' not in request.session or request.session['userID'] == None:
        messages.error(request, "You must log in to view that page")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['userID']),
        'games': Game.objects.all(),
    }
    return render(request, 'homeIndex.html', context)

def header(request): #partial render header
    context = {
        'user': User.objects.get(id=request.session['userID']),
    }
    return render(request, 'partial/header.html', context)

def game(request, gameID): # game page
    if 'userID' not in request.session or request.session['userID'] == None:
        messages.error(request, "You must log in to view that page")
        return redirect('/')
    gameList = Game.objects.filter(id=gameID)
    if len(gameList) == 0: # prevent errors from users typing in an address of a non-existing game id
        messages.error(request, "No game with that ID found")
        return redirect('/home')
    currUser = User.objects.get(id=request.session['userID'])
    context = {
        'user': currUser,
        'game': gameList[0],
    }
    return render(request, 'gamePage.html', context)


def createGame(request):
    if 'userID' not in request.session or request.session['userID'] == None:
        messages.error(request, "You must log in to view that page")
        return redirect('/')
    key = randomKey()
    currUser = User.objects.get(id=request.session['userID'])
    newGame = Game.objects.create(join_key=key, host=currUser) #create new game instance
    newGame.players.add(currUser) # add host to list of players
    Role.objects.create(player=currUser, game=newGame, role_name="host") #create role for host 'player'
    return redirect(f'/home/game/{newGame.id}')

def joinGame(request, gameID):
    if 'userID' not in request.session or request.session['userID'] == None:
        messages.error(request, "You must log in to view that page")
        return redirect('/')
    gameList = Game.objects.filter(id=gameID)
    if len(gameList) == 0: # prevent errors from users typing in an address of a non-existing game id
        messages.error(request, "No game with that ID found")
        return redirect('/home')
    currUser = User.objects.get(id=request.session['userID'])
    thisGame = gameList[0]
    if thisGame.started == True or thisGame.ended == True: # prevent players from joining a game after it started or ended
        messages.error(request, "This game is no longer joinable")
        return redirect('/home')
    roleList = Role.objects.filter(game=thisGame, player=currUser)
    if len(roleList) > 0: # player has already joined game and been assigned a role
        return redirect(f'/home/game/{gameID}')
    else: # create a new role for the player and add them to the player list
        thisGame.players.add(currUser)
        thisRole = Role.objects.create(player=currUser, game=thisGame, role_name="unassigned")
        return redirect(f'/home/game/{gameID}')
    
def startGame(request, gameID, postData):
    if 'userID' not in request.session or request.session['userID'] == None:
        messages.error(request, "You must log in to view that page")
        return redirect('/')
    errors = Game.objects.startGame(request.POST, gameID, request.session['userID'])
    if len(errors) > 0:
        for error in errors:
            messages.error(request, errors[error])
    return redirect(f'/home/game/{gameID}')

def updateGame(request, gameID):
    if 'userID' not in request.session or request.session['userID'] == None:
        messages.error(request, "You must log in to view that page")
        return redirect('/')
    if request.POST['submitAction'] == 'update':
        errors = Game.objects.updateGame(request.POST, gameID, request.session['userID']) # this function spits out any errors and updates the game if there are none
        if len(errors) > 0:
            for error in errors:
                messages.error(request, errors[error])
        return redirect(f'/home/game/{gameID}')
    elif request.POST['submitAction'] == 'start':
        return startGame(request, gameID, request.POST)
    else:
        return redirect(f'/home/game/{gameID}')

def fakeUsers(request): # comment this function for production
    fakePassword = bcrypt.hashpw("password".encode(), bcrypt.gensalt()).decode()
    for i in range(1,11):
        if len(User.objects.filter(username=f"user{i}")) == 0: #this fake user doesn't yet exist
            User.objects.create(first_name="user", last_name=f"{i}", email=f"user{i}@email.com", username=f"user{i}", password=fakePassword)
    messages.success(request, "Generated fake users user1@email.com - user10@email.com with password 'password'")
    return redirect('/')

def addFakeUsers(request, gameID):
    if 'userID' not in request.session or request.session['userID'] == None:
        messages.error(request, "You must log in to view that page")
        return redirect('/')
    game = Game.objects.get(id=gameID)
    user = User.objects.get(id=request.session['userID'])
    if game.host == user:
        # add the fake users to the game
        fakeUserList = User.objects.filter(first_name="user")
        for fakeUser in fakeUserList:
            Role.objects.create(player=fakeUser, game=game)
            game.players.add(fakeUser)
    messages.success(request, "Added fake users to current game")
    return redirect(f'/home/game/{gameID}')