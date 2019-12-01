import random
import django
django.setup()
import os

from admin_tools.models import Department



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


depts = [
    'Computer Technology',
    'Electrical Engineering',
    'Civil Engineering',
    'AIDT',
    'Textile Engineering',
    'Telecommunication Engineering',
]

def generate_dept(n=6):
    for i in range(0, n):
        name = depts[i]

        try:
            teacher = Department.objects.get_or_create(
                name=name)
        except:
            continue
        
        


if __name__ == "__main__":
    print('Creating Departments....')
    generate_dept()
    print('Departments created successfully.')
