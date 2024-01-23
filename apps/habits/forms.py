from django import forms

from .models import Habit


class AddHabitForm(forms.ModelForm):
    """
    A form used to add a new habit to the user's habit list.
    """

    class Meta:
        model = Habit
        fields = ["title"]
