from django.db import models

JAN, FEB, MAR, APR, MAY, JUN = 1, 2, 3, 4, 5, 6
JUL, AUG, SEP, OCT, NOV, DEC = 7, 8, 9, 10, 11, 12
MONTHS= ((JAN, "January"),
         (FEB, "February"),
         (MAR, "March"),
         (APR, "April"),
         (MAY, "May"),
         (JUN, "June"),
         (JUL, "July"),
         (AUG, "August"),
         (SEP, "September"),
         (OCT, "October"),
         (NOV, "November"),
         (DEC, "December"),
        )
MONTHS_DICT = {key:value for (key, value) in MONTHS}

MON, TUE, WED, THU, FRI, SAT, SUN = 1, 2, 3, 4, 5, 6, 7
DAYS = ((MON, "Monday"),
        (TUE, "Tuesday"),
        (WED, "Wednesday"),
        (THU, "Thursday"),
        (FRI, "Friday"),
        (SAT, "Saturday"),
        (SUN, "Sunday"),
       )
DAYS_DICT = {key:value for (key, value) in DAYS}

class FilledQuestionnaire(models.Model):
    """FilledQuestionnaire model for cloud_test app.

    Stores the months and days in database by their order number.
    Uses choices to enable form selction by name.
    """

    month = models.IntegerField(choices=MONTHS, default=JAN)
    day = models.IntegerField(choices=DAYS, default=MON)

    def __str__(self):
         return f"{MONTHS_DICT[self.month]}, {DAYS_DICT[self.day]}"
