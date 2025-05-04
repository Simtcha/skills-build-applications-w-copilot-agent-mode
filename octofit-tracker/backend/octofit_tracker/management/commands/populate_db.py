from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate octofit_db with test data'

    def handle(self, *args, **kwargs):
        # Users
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        user1 = User.objects.create(email="alice@example.com", name="Alice", password="alicepass")
        user2 = User.objects.create(email="bob@example.com", name="Bob", password="bobpass")
        user3 = User.objects.create(email="carol@example.com", name="Carol", password="carolpass")

        # Teams
        team1 = Team.objects.create(name="Team Alpha", members=[user1.email, user2.email])
        team2 = Team.objects.create(name="Team Beta", members=[user3.email])

        # Activities
        Activity.objects.create(activity_id="a1", user=user1.email, type="run", duration=30, date=datetime(2025, 5, 1))
        Activity.objects.create(activity_id="a2", user=user2.email, type="walk", duration=45, date=datetime(2025, 5, 2))
        Activity.objects.create(activity_id="a3", user=user3.email, type="strength", duration=20, date=datetime(2025, 5, 3))

        # Leaderboard
        Leaderboard.objects.create(leaderboard_id="l1", team=team1.name, points=75)
        Leaderboard.objects.create(leaderboard_id="l2", team=team2.name, points=40)

        # Workouts
        Workout.objects.create(workout_id="w1", name="Pushups", description="Do 20 pushups")
        Workout.objects.create(workout_id="w2", name="Situps", description="Do 30 situps")
        Workout.objects.create(workout_id="w3", name="Jogging", description="Jog for 15 minutes")

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
