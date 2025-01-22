from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, Group, Permission, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.postgres.fields import ArrayField

username_validator = RegexValidator(
    regex=r'^[A-Za-zА-Яа-яЁё\s]+$',  # Разрешаем только заглавные буквы и символы
    message='Имя пользователя может содержать только заглавные буквы и символы . @ + -'
)

class User(AbstractUser):
    ROLES = [
        ('student', 'Student'),
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
    ]
    role = models.CharField(max_length=10, choices=ROLES)
    
    username = models.CharField(
        max_length=20,
        unique=True,
        validators=[username_validator]
    )
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions', 
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

class Institute(models.Model):
    abbreviation = models.CharField(max_length=50, verbose_name="Аббревиатура института")  # Аббревиатура
    name = models.CharField(max_length=255, verbose_name="Полное название института")      # Полное название
    address = models.TextField(verbose_name="Адрес института")                             # Адрес
    rating = models.FloatField(default=0, verbose_name="Рейтинг института")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.abbreviation} - {self.name}"
    
class Course(models.Model):
    name = models.CharField(max_length=255)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='courses')
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'teacher'})
    schedule = models.CharField(max_length=255)
    settings = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Rating(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='rating')
    average_rating = models.FloatField(default=0)
    total_reviews = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

class Lesson(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='lessons')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    topic = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    room = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    average_rating = models.FloatField(default=0)  # Средняя оценка
    total_reviews = models.IntegerField(default=0)  # Количество отзывов

    def __str__(self):
        return f"{self.topic} - {self.date} {self.time}"

class Review(models.Model):
    ADVANTAGES_CHOICES = [
        ('usefulness', 'Полезность материала'),
        ('delivery', 'Подача материала'),
        ('kindness', 'Доброжелательность преподавателя'),
        ('interaction', 'Взаимодействие со студентами'),
        ('equipment', 'Аудитория и оборудование'),
        ('difficulty', 'Сложность заданий на паре'),
        ('materials', 'Предоставление материалов'),
    ]

    user = models.CharField(max_length=255, verbose_name="User")
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True, verbose_name="Comment") 
    advantages = ArrayField(
        models.CharField(max_length=50, choices=ADVANTAGES_CHOICES),
        blank=True,
        default=list,
        help_text="Выберите преимущества пары"
    )
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} for {self.lesson} - {self.rating}"