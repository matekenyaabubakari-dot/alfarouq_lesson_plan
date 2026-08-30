from django.db import models


class LessonPlan(models.Model):
    teacher_name = models.CharField(max_length=200)
    school_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    date = models.DateField()

    main_competence = models.TextField(blank=True)
    specific_competence = models.TextField(blank=True)
    learning_activities = models.TextField(blank=True)
    teaching_materials = models.TextField(blank=True)
    assessment = models.TextField(blank=True)
    reflection = models.TextField(blank=True)
    references = models.TextField(blank=True)

    total_students = models.PositiveIntegerField(default=0)
    students_present = models.PositiveIntegerField(default=0)
    students_absent = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject} - {self.class_name} - {self.date}"


class TeacherProfile(models.Model):
    full_name = models.CharField(
        max_length=200,
        default="Teacher"
    )

    school_name = models.CharField(
        max_length=200,
        blank=True
    )

    subjects = models.CharField(
        max_length=300,
        blank=True
    )

    qualification = models.CharField(
        max_length=200,
        blank=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    teacher_id = models.CharField(
        max_length=100,
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.full_name