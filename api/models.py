from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    """This class represents the bucketlist model."""
    firstName = models.CharField(max_length=255, blank=False)
    lastName = models.CharField(max_length=255, blank=False)
    salaryClaims = models.IntegerField(validators=[MinValueValidator(10)])
    description = models.TextField()
    email = models.EmailField(verbose_name='email address',
                              max_length=255,
                              unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.firstName + " " + self.lastName)


class Skill(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False)
    userId = models.IntegerField()
    type = models.CharField(max_length=255, blank=False)
    note = models.IntegerField(validators=[MaxValueValidator(5),
                                             MinValueValidator(0)])
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class Project(models.Model):
    """This class repxresents the bucketlist model."""
    languages = models.TextField()
    name = models.CharField(max_length=255, blank=False)
    descriptive = models.TextField()
    userId = models.IntegerField()
    links = models.TextField()

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
