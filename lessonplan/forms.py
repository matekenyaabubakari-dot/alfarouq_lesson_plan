from django import forms
from .models import LessonPlan


class LessonPlanForm(forms.ModelForm):

    class Meta:
        model = LessonPlan
        fields = [
            "teacher_name",
            "school_name",
            "subject",
            "class_name",
            "date",
            "main_competence",
            "specific_competence",
            "learning_activities",
            "teaching_materials",
            "assessment",
            "reflection",
            "references",
        ]

        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "main_competence": forms.Textarea(
                attrs={"rows": 3}
            ),

            "specific_competence": forms.Textarea(
                attrs={"rows": 3}
            ),

            "learning_activities": forms.Textarea(
                attrs={"rows": 5}
            ),

            "teaching_materials": forms.Textarea(
                attrs={"rows": 3}
            ),

            "assessment": forms.Textarea(
                attrs={"rows": 3}
            ),

            "reflection": forms.Textarea(
                attrs={"rows": 3}
            ),

            "references": forms.Textarea(
                attrs={"rows": 3}
            ),
        }