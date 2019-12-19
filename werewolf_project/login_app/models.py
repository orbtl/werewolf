from django.db import models
import bcrypt
from datetime import datetime
import re #import regular expressions for email validation

class UserManager(models.Manager):
    def new_user_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name_length'] = "First name must be at least 2 characters"
        if not postData['first_name'].isalpha():
            errors['first_name_alpha'] = "First name must be composed only of letters of the alphabet"
        if len(postData['last_name']) < 2:
            errors['last_name_length'] = "Last name must be at least 2 characters"
        if not postData['last_name'].isalpha():
            errors['last_name_alpha'] = "Last name must be composed only of letters of the alphabet"
        email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not re.search(email_regex, postData['email']):
            errors['invalidEmail'] = "Invalid email address"
        if len(User.objects.filter(email=postData['email'].lower())) > 0:
            errors['existingEmail'] = "Account with that email address already exists in database"
        if len(postData['password']) < 8:
            errors['pw_length'] = "Password must be at least 8 characters"
        if postData['password'] != postData['password2']:
            errors['pw_match'] = "Passwords do not match!"
        if len(postData['username']) < 2:
            errors['usernameTooSmall'] = "Username must be at least 2 characters"
        if len(postData['username']) > 18:
            errors['usernameTooBig'] = "Username may only be at most 18 characters"
        # ageDelta = (datetime.now() - datetime.strptime(postData['birthday'], '%Y-%m-%d'))
        # if ageDelta.days < 4745: #4745 days = 13 years
        #     errors['birthday'] = "Sorry, you must be at least 13 years of age to register for this website"
        return errors

    def login_validator(self, postData):
        errors = {}
        if len(User.objects.filter(email=postData['email'].lower())) == 0:
            errors['noEmail'] = "Email address not found in user database"
            return errors
        currUser = User.objects.filter(email=postData['email'].lower())[0]
        if not bcrypt.checkpw(postData['password'].encode(), currUser.password.encode()):
            errors['pwInvalid'] = "Invalid Password"
        return errors



class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # roles = each role this player is or has been for given games
    # games_hosted = game objects the player created
    # games_joined = game objects the player joined
    # games_won
    # games_lost














    ### this was the old setup of commented relationship related_names
    # 
    # games_werewolf = games the player is/was a werewolf
    # games_villager = games the player is/was a villager
    # games_village_idiot = games the player is/was the village idiot
    # games_cupid = games the player is/was cupid
    # games_lover = games the player is/was a lover
    # games_twin = games the player is/was a twin
    # games_accursed_one = games the player is/was the accursed_one
    # games_seer = '' seer
    # games_witch = '' witch
    # games_defender = '' defender
    # games_hunter = '' hunter
    # games_wild_child = '' wild child
    # games_role_model = '' role model (for the wild child)
    # games_rusty_knight = '' knight with the rusty sword
    # games_elder = '' elder
    # games_angel = '' angel
    # games_gypsy = '' gypsy