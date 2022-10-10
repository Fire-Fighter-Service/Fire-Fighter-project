#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineFire_ReportingSystem.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()



class Firereport(models.Model):
    FullName = models.CharField(max_length=250, null=True)
    MobileNumber = models.CharField(max_length=12, null=True)
    Location = models.CharField(max_length=200, null=True)
    Message = models.CharField(max_length=200, null=True)
    AssignTo = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True)
    Status = models.CharField(max_length=150, null=True)
    Postingdate = models.DateTimeField(auto_now_add=True)
    AssignedTime = models.CharField(max_length=150, null=True)
    UpdationDate = models.DateTimeField(null=True)

    def __str__(self):
        return self.FullName

    class Firereport(models.Model):
        FullName = models.CharField(max_length=250, null=True)
        MobileNumber = models.CharField(max_length=12, null=True)
        Location = models.CharField(max_length=200, null=True)
        Message = models.CharField(max_length=200, null=True)
        AssignTo = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True)
        Status = models.CharField(max_length=150, null=True)
        Postingdate = models.DateTimeField(auto_now_add=True)
        AssignedTime = models.CharField(max_length=150, null=True)
        UpdationDate = models.DateTimeField(null=True)

        def __str__(self):
            return self.FullName

