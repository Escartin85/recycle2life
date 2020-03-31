# django imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MaxValueValidator
# third party imports

# APP imports

# Helps DJango work with our custom user model
class UserProfileManager(BaseUserManager):

    # Creates a new user profile object
    def create_user(self, email, name, password=None):
        # check if the email is not provided
        if not email:
            raise ValueError('Users must have an email address.')
        
        # normalize all character to lower case
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user
        
    # Creates a new user profile object
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

# Respents a "user profile" inside our system
class UserProfile(AbstractBaseUser, PermissionsMixin):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    dob = models.CharField(max_length=8)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=MALE)
    phone_prefix = models.PositiveIntegerField(validators=[MaxValueValidator(99)], default=0)
    phone = models.PositiveIntegerField(validators=[MaxValueValidator(99999999999)], default=0)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    post_code = models.CharField(max_length=8)
    picture = models.FileField(upload_to='uploads/images/user_profile', max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # used to get a user full name
    def get_full_name(self):
        return self.surname
    
    # used to get a users short name
    def get_short_name(self):
        return self.name
    
    # django uses this when it needs to convert the object to a string
    def __str__(self):
        return self.email