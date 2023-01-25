from django.db import models

class Sponsor(models.Model):

    # DIVISIONS
    GOKART = "GOKART"
    EV = "EV"

    DIVISIONS =[
        (GOKART, "Gokart"),
        (EV, "Electric Vehicle"),
    ]

    brand = models.CharField(max_length=50)
    division = models.CharField(max_length=200, choices=DIVISIONS, null=True, blank=True)
    image = models.ImageField(upload_to='UIMS/Sponsors', null=True)