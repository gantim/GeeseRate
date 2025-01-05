from django.db.models import Avg  # Импортируем Avg для агрегации
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Review, Lesson

@receiver(post_save, sender=Review)
def update_lesson_rating_on_save(sender, instance, **kwargs):
    lesson = instance.lesson
    reviews = lesson.reviews.all()
    lesson.average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    lesson.total_reviews = reviews.count()
    lesson.save()

@receiver(post_delete, sender=Review)
def update_lesson_rating_on_delete(sender, instance, **kwargs):
    lesson = instance.lesson
    reviews = lesson.reviews.all()
    lesson.average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    lesson.total_reviews = reviews.count()
    lesson.save()
