from django.db import models

class FilledQuestionnaire(models.Model):
    """FilledQuestionnaire model for cloud_test app.

    Stores the months and days in database by their order number.
    Uses choices to enable form selction by name.
    """
    MONTHS= ((1, "January"),
              (2,"February"),
              (3,"March"),
              (4,"April"),
              (5,"May"),
              (6,"June"),
              (7,"July"),
              (8,"August"),
              (9,"September"),
              (10,"October"),
              (11,"November"),
              (12,"December"),)
    DAYS = ((1, "Monday"),
            (2, "Tuesday"),
            (3, "Wednesday"),
            (4, "Thursday"),
            (5, "Friday"),
            (6, "Saturday"),
            (7, "Sunday"), )

    month = models.IntegerField(choices=MONTHS)
    day = models.IntegerField(choices=DAYS)
