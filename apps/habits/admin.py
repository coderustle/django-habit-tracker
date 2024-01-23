from django.contrib import admin

from apps.habits.models import Habit, HabitLog


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    pass


@admin.register(HabitLog)
class HabitLogAdmin(admin.ModelAdmin):
    pass
