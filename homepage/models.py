from __future__ import division
from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class NewsPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to='UIMS')
    excerpt = models.CharField(max_length=150)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = NewsPost.objects.all().filter(slug__iexact=original_slug).count()

        # Ensure url slugs with the same title are unique
        if queryset == 0:
            self.slug = original_slug
        else:
            self.slug = original_slug + '-' + str(queryset - 1)

        if self.featured:
            try:
                temp = NewsPost.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except NewsPost.DoesNotExist:
                pass

        super(NewsPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    angkatan = models.CharField(max_length=5, null=True, blank=True)
    role = models.ForeignKey(
        'TeamRole',
        on_delete=models.CASCADE,
        related_name="team_role",
        null=True,
        blank=True
    )
    def __str__(self) :
        return f"{self.name} ({self.role})"

class TeamRole(models.Model):
    
    TECHNICAL_DIVISION = 1
    NON_TECHNICAL_DIVISION = 2


    DIVISION_TYPE = [
        (TECHNICAL_DIVISION, "Technical Division"),
        (NON_TECHNICAL_DIVISION, "Non-Technical Division"),
    ]

    TEAM_PRINCIPAL = 0
    DIRECTOR = 1
    POWERTRAIN = 2
    VEHICLE = 3
    INTERNAL = 4
    EXTERNAL = 5

    DIVISIONS =[
        (TEAM_PRINCIPAL, "Team Principal"),
        (DIRECTOR, "Director"),
        (POWERTRAIN, "Powertrain"),
        (VEHICLE, "Vehicle"),
        (INTERNAL, "Internal"),
        (EXTERNAL, "External")
    ]

    division_type = models.IntegerField(choices=DIVISION_TYPE, null=True, blank=True)
    division = models.IntegerField(choices=DIVISIONS)
    role_name = models.CharField(max_length=200)

    def __str__(self, divisions = DIVISIONS) :
        if self.division == 0:
            return f"{divisions[self.division][1]}"
        return f"{divisions[self.division][1]}, {self.role_name}"


