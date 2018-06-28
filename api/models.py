from django.db import models

# Create your models here.


class User(models.Model):
    """This class represents the bucketlist model."""
    firstName = models.CharField(max_length=255, blank=False)
    lastName = models.CharField(max_length=255, blank=False)
    salaryClaims = models.IntegerField()
    description = models.TextField()
    email = models.EmailField(verbose_name='email address',
                              max_length=255,
                              unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
