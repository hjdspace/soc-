from django.core.management.base import BaseCommand
from api.models import Project

class Command(BaseCommand):
    help = 'Creates a test project'

    def handle(self, *args, **options):
        if not Project.objects.filter(name='Test Project').exists():
            Project.objects.create(name='Test Project', description='A project created for testing purposes.')
            self.stdout.write(self.style.SUCCESS('Successfully created test project "Test Project"'))
        else:
            self.stdout.write(self.style.WARNING('Test project "Test Project" already exists.'))
