from datetime import datetime, date, timedelta

from django.db import models

ANDROID = "android"
IOS = "ios"
UNKNOWN = "unknown"
OSes = [(ANDROID, "Android"), (IOS, "iOS"), (UNKNOWN, "Unknown OS")]

WARNING = "warning"
CLEAN = "clean"
SCAN_RESULTS = [
    (WARNING, "The scan has produced at least one warning."),
    (CLEAN, "The scan is clean! It has produced no warnings, nor detections."),
]


class ScanResult(models.Model):
    name = models.CharField("name of the scanResult", max_length=215)
    date_added = models.DateTimeField(
        "date and time when a scanResult was added to the database"
    )
    path = models.CharField("scanResult directory file system path",
        max_length=1000)
    operating_system = models.CharField(
        "device OS", max_length=100, choices=OSes
    )
    mvt_version = models.CharField(
        "version of MVT used for the scan", max_length=215
    )
    overall_result = models.CharField(
        "the overall result of the scan",
        max_length=100,
        choices=SCAN_RESULTS
    )
    last_security_path_date = models.DateField("date of the last security scan", 
        default=date.today
    )
    scan_date = models.DateField("date when the forensic scan was run", default=date.today)
    warnings = models.CharField("warings resulted from the MVT scan", max_length=10000, blank=True, null=True)

    installed_apps = models.JSONField(blank=True, null=True)

    def __str__(self):
        return " ".join([self.name, self.date_added.strftime("%d/%m/%y %H:%M:%S.%f")])

    @property
    def old_security_patch(self):
        if (self.scan_date - self.last_security_path_date) > timedelta(weeks=24):
            return True
        else:
            return False
