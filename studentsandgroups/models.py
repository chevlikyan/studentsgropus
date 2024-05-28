from django.db import models

COURSES = [
    ('Mathematics', 'Mathematics'),
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    ('English', 'English'),
    ('Russian', 'Russian'),
    ('French', 'French'),
    ('Spanish', 'Spanish'),
    ('Armenian', 'Armenian'),
    ('Python', 'Python'),
    ('JavaScript', 'JavaScript'),
    ('Java', 'Java')

]

DURATION = [
    ('1 hour', '1 hour'),
    ('2 hours', '2 hours'),
    ('3 hours', '3 hours'),
    ('4 hours', '4 hours')
]


class Group(models.Model):
    name = models.CharField(choices=COURSES, max_length=20)
    description = models.TextField(max_length=100)
    duration = models.CharField(choices=DURATION, max_length=10)
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='student', blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name}{self.surname}{self.group}"
