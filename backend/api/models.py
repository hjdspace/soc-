from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Release(models.Model):
    STATUS_CHOICES = [
        ('In Progress', 'In Progress'),
        ('Released', 'Released'),
        ('Cancelled', 'Cancelled'),
    ]
    project = models.ForeignKey(Project, related_name='releases', on_delete=models.CASCADE)
    version = models.CharField(max_length=50)
    release_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='In Progress')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.name} - {self.version}"

class TestPlan(models.Model):
    project = models.ForeignKey(Project, related_name='test_plans', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    # Using FileField to handle file uploads
    upload = models.FileField(upload_to='testplans/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TestCase(models.Model):
    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('In Progress', 'In Progress'),
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('Blocked', 'Blocked'),
    ]
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    project = models.ForeignKey(Project, related_name='test_cases', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Planned')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Medium')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Bug(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]
    SEVERITY_CHOICES = [
        ('Critical', 'Critical'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    project = models.ForeignKey(Project, related_name='bugs', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default='Medium')
    reporter = models.CharField(max_length=100, blank=True) # Simple text field for now
    assignee = models.CharField(max_length=100, blank=True) # Simple text field for now
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
