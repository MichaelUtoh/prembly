from django.db import models


class Gender(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"
    OTHERS = "O", "Others"


class Title(models.TextChoices):
    MR = "Mr", "Mr"
    MRS = "Mrs", "Mrs"
    MISS = "Miss", "Miss"


class MaritalStatus(models.TextChoices):
    SINGLE = "single", "Single"
    MARRIED = "married", "Married"
    DIVORCED = "divorced", "Divorced"
    WIDOWED = "widowed", "Widowed"


class UserStatus(models.TextChoices):
    NONE = "none", "None"
    BRONZE = "bronze", "Bronze"
    SILVER = "silver", "Silver"
    GOLD = "gold", "Gold"
    PLATINUM = "platinum", "Platinum"


class UserType(models.TextChoices):
    EXPERT = "expert", "Expert"
    FARMER = "farmer", "Farmer"


class PricingPlans(models.TextChoices):
    MONTHLY = "monthly", "Monthly"
    QUARTERLY = "quarterly", "Quarterly"
    ANNUALLY = "annually", "annually"