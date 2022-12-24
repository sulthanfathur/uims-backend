from django.db import models

class TeamMember(models.Model):

    # DIVISIONS
    OTHERS = "OTHERS"
    GOKART = "GOKART"
    EV = "EV"
    MARKETING = "MARKETING"

    DIVISIONS =[
        (OTHERS, "Lainnya (Team Principal, Finance, Advisor, dll.)"),
        (GOKART, "Gokart"),
        (EV, "Electric Vehicle"),
        (MARKETING, "Marketing"),
    ]

    # SUB-DIVISIONS
    #    GOKART
    GOKART_550 = "GOKART 550"
    GOKART_551 = "GOKART 551"
    RESEARCH_AND_DEVELOPMENT = "RESEARCH & DEVELOPMENT"
    #    EV
    E_POWERTRAIN = "E-POWERTRAIN"
    VEHICLE = "VEHICLE"
    AERODYNAMICS = "AERODYNAMICS"
    #    MARKETING
    MEDIA = "MEDIA"
    RELATION = "RELATION"
    SPONSORSHIP = "SPONSORSHIP"

    SUB_DIVISIONS = [
        (OTHERS, "Lainnya (Team Principal, Finance, Advisor, dll.)"),
        (GOKART_550, "Gokart 550"),
        (GOKART_551, "Gokart 551"),
        (RESEARCH_AND_DEVELOPMENT, "Research & Development")
        (E_POWERTRAIN, "E-Powertrain"),
        (VEHICLE, "Vehicle"),
        (AERODYNAMICS, "Aerodynamics"),
        (MEDIA, "Media"),
        (RELATION, "Relation"),
        (SPONSORSHIP, "Sponsorship"),
    ]

    # ROLES / JABATAN
    TEAM_PRINCIPAL = "TEAM PRINCIPAL"
    FINANCE = "FINANCE"
    ADVISOR = "ADVISOR"
    SECRETARY = "SECRETARY"
    DRIVER = "DRIVER"
    CTO = "CTO"
    MANAGER = "MANAGER"
    STAFF = "STAFF"
    MECHANIC = "MECHANIC"

    JABATAN = [
        (TEAM_PRINCIPAL, "Team Principal"),
        (FINANCE, "Finance"),
        (ADVISOR, "Advisor"),
        (SECRETARY, "Secretary"),
        (DRIVER, "Driver"),
        (CTO, "Chief Technical Officer"),
        (MANAGER, "Manager"),
        (STAFF, "Staff"),
        (MECHANIC, "Mechanic"),
    ]

    name = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='UIMS', default='/UIMS/default_avatar_xugf2l.png', null=True)
    division = models.CharField(max_length=200, choices=DIVISIONS, null=True, blank=True)
    sub_division = models.CharField(max_length=200, choices=SUB_DIVISIONS, null=True, blank=True)
    jabatan = models.CharField(max_length=200, choices=JABATAN, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    def __str__(self, other = OTHERS) :
        if self.division == other or self.sub_division == other:
            return f"{self.name} | {self.jabatan}"
        return f"{self.name} | {self.sub_division} {self.jabatan} | {self.division} DIVISION"