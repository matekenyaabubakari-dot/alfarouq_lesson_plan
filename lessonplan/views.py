from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages

from .models import LessonPlan, TeacherProfile


def home(request):
    total_lessons = LessonPlan.objects.count()

    today = timezone.localdate()

    start_of_week = today - timezone.timedelta(
        days=today.weekday()
    )

    weekly_lessons = LessonPlan.objects.filter(
        date__gte=start_of_week,
        date__lte=today
    ).count()

    monthly_lessons = LessonPlan.objects.filter(
        date__year=today.year,
        date__month=today.month
    ).count()

    total_subjects = (
        LessonPlan.objects
        .values("subject")
        .distinct()
        .count()
    )

    recent_lessons = LessonPlan.objects.all().order_by(
        "-date",
        "-created_at"
    )[:5]

    context = {
        "total_lessons": total_lessons,
        "weekly_lessons": weekly_lessons,
        "monthly_lessons": monthly_lessons,
        "total_subjects": total_subjects,
        "recent_lessons": recent_lessons,
    }

    return render(
        request,
        "lessonplan/home.html",
        context
    )


def create_lesson_plan(request):
    if request.method == "POST":

        teacher_name = request.POST.get("teacher_name")
        school_name = request.POST.get("school_name")
        subject = request.POST.get("subject")
        class_name = request.POST.get("class_name")
        date = request.POST.get("date")

        main_competence = request.POST.get("main_competence")
        specific_competence = request.POST.get("specific_competence")
        learning_activities = request.POST.get("learning_activities")
        teaching_materials = request.POST.get("teaching_materials")
        assessment = request.POST.get("assessment")
        reflection = request.POST.get("reflection")
        references = request.POST.get("references")

        total_students = request.POST.get(
            "total_students",
            0
        )

        students_present = request.POST.get(
            "students_present",
            0
        )

        students_absent = request.POST.get(
            "students_absent",
            0
        )

        LessonPlan.objects.create(
            teacher_name=teacher_name,
            school_name=school_name,
            subject=subject,
            class_name=class_name,
            date=date,

            main_competence=main_competence,
            specific_competence=specific_competence,
            learning_activities=learning_activities,
            teaching_materials=teaching_materials,
            assessment=assessment,
            reflection=reflection,
            references=references,

            total_students=total_students,
            students_present=students_present,
            students_absent=students_absent,
        )

        messages.success(
            request,
            "Lesson Plan created successfully!"
        )

        return redirect("lesson_plan_list")

    return render(
        request,
        "lessonplan/create_lesson_plan.html"
    )


def lesson_plan_list(request):
    lesson_plans = LessonPlan.objects.all().order_by(
        "-date",
        "-created_at"
    )

    return render(
        request,
        "lessonplan/lesson_plan_list.html",
        {
            "lesson_plans": lesson_plans
        }
    )


def lesson_plan_detail(request, pk):
    lesson_plan = get_object_or_404(
        LessonPlan,
        pk=pk
    )

    attendance_percentage = 0

    if lesson_plan.total_students > 0:
        attendance_percentage = round(
            (
                lesson_plan.students_present
                / lesson_plan.total_students
            ) * 100,
            1
        )

    return render(
        request,
        "lessonplan/lesson_plan_detail.html",
        {
            "lesson_plan": lesson_plan,
            "attendance_percentage": attendance_percentage,
        }
    )


def edit_lesson_plan(request, pk):
    lesson_plan = get_object_or_404(
        LessonPlan,
        pk=pk
    )

    if request.method == "POST":

        lesson_plan.teacher_name = request.POST.get(
            "teacher_name"
        )

        lesson_plan.school_name = request.POST.get(
            "school_name"
        )

        lesson_plan.subject = request.POST.get(
            "subject"
        )

        lesson_plan.class_name = request.POST.get(
            "class_name"
        )

        lesson_plan.date = request.POST.get(
            "date"
        )

        lesson_plan.main_competence = request.POST.get(
            "main_competence"
        )

        lesson_plan.specific_competence = request.POST.get(
            "specific_competence"
        )

        lesson_plan.learning_activities = request.POST.get(
            "learning_activities"
        )

        lesson_plan.teaching_materials = request.POST.get(
            "teaching_materials"
        )

        lesson_plan.assessment = request.POST.get(
            "assessment"
        )

        lesson_plan.reflection = request.POST.get(
            "reflection"
        )

        lesson_plan.references = request.POST.get(
            "references"
        )

        lesson_plan.total_students = request.POST.get(
            "total_students",
            0
        )

        lesson_plan.students_present = request.POST.get(
            "students_present",
            0
        )

        lesson_plan.students_absent = request.POST.get(
            "students_absent",
            0
        )

        lesson_plan.save()

        messages.success(
            request,
            "Lesson Plan updated successfully!"
        )

        return redirect(
            "lesson_plan_detail",
            pk=lesson_plan.pk
        )

    return render(
        request,
        "lessonplan/edit_lesson_plan.html",
        {
            "lesson_plan": lesson_plan
        }
    )


def delete_lesson_plan(request, pk):
    lesson_plan = get_object_or_404(
        LessonPlan,
        pk=pk
    )

    if request.method == "POST":

        lesson_plan.delete()

        messages.success(
            request,
            "Lesson Plan deleted successfully!"
        )

        return redirect("lesson_plan_list")

    return render(
        request,
        "lessonplan/delete_lesson_plan.html",
        {
            "lesson_plan": lesson_plan
        }
    )


def reports(request):
    total_lessons = LessonPlan.objects.count()

    today = timezone.localdate()

    start_of_week = today - timezone.timedelta(
        days=today.weekday()
    )

    weekly_lessons = LessonPlan.objects.filter(
        date__gte=start_of_week,
        date__lte=today
    ).count()

    monthly_lessons = LessonPlan.objects.filter(
        date__year=today.year,
        date__month=today.month
    ).count()

    total_subjects = (
        LessonPlan.objects
        .values("subject")
        .distinct()
        .count()
    )

    total_students = sum(
        lesson.total_students
        for lesson in LessonPlan.objects.all()
    )

    total_present = sum(
        lesson.students_present
        for lesson in LessonPlan.objects.all()
    )

    total_absent = sum(
        lesson.students_absent
        for lesson in LessonPlan.objects.all()
    )

    subject_reports = (
        LessonPlan.objects
        .values("subject")
        .annotate()
    )

    class_reports = (
        LessonPlan.objects
        .values("class_name")
        .annotate()
    )

    return render(
        request,
        "lessonplan/reports.html",
        {
            "total_lessons": total_lessons,
            "weekly_lessons": weekly_lessons,
            "monthly_lessons": monthly_lessons,
            "total_subjects": total_subjects,

            "total_students": total_students,
            "total_present": total_present,
            "total_absent": total_absent,

            "subject_reports": subject_reports,
            "class_reports": class_reports,
        }
    )


def profile(request):

    profile, created = TeacherProfile.objects.get_or_create(
        id=1
    )

    if request.method == "POST":

        profile.full_name = request.POST.get(
            "full_name",
            ""
        )

        profile.school_name = request.POST.get(
            "school_name",
            ""
        )

        profile.subjects = request.POST.get(
            "subjects",
            ""
        )

        profile.qualification = request.POST.get(
            "qualification",
            ""
        )

        profile.phone = request.POST.get(
            "phone",
            ""
        )

        profile.email = request.POST.get(
            "email",
            ""
        )

        profile.teacher_id = request.POST.get(
            "teacher_id",
            ""
        )

        profile.bio = request.POST.get(
            "bio",
            ""
        )

        profile.save()

        messages.success(
            request,
            "Teacher profile updated successfully!"
        )

        return redirect("profile")

    total_lessons = LessonPlan.objects.count()

    total_subjects = (
        LessonPlan.objects
        .values("subject")
        .distinct()
        .count()
    )

    total_students = sum(
        lesson.total_students
        for lesson in LessonPlan.objects.all()
    )

    recent_lessons = LessonPlan.objects.all().order_by(
        "-date",
        "-created_at"
    )[:5]

    return render(
        request,
        "lessonplan/profile.html",
        {
            "profile": profile,
            "total_lessons": total_lessons,
            "total_subjects": total_subjects,
            "total_students": total_students,
            "recent_lessons": recent_lessons,
        }
    )


def settings(request):
    return render(
        request,
        "lessonplan/settings.html"
    )