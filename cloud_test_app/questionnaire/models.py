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

MON, TUE, WED, THU, FRI, SAT, SUN = 1, 2, 3, 4, 5, 6, 7
DAYS = ((MON, "Monday"),
        (TUE, "Tuesday"),
        (WED, "Wednesday"),
        (THU, "Thursday"),
        (FRI, "Friday"),
        (SAT, "Saturday"),
        (SUN, "Sunday"), )


class FilledQuestionnaire(models.Model):
    """FilledQuestionnaire model for cloud_test app.

    Stores the months and days in database by their order number.
    Uses choices to enable form selction by name.
    """

    month = models.IntegerField(choices=MONTHS, default=JAN)
    day = models.IntegerField(choices=DAYS, default=MON)
