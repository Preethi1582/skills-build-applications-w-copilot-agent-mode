"""
Script to populate the octofit_db MongoDB database with test data for users, teams, activities, leaderboard, and workouts collections.
Run this script with the Django environment loaded.
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

def run():

# Import models
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

def run():
    # Clear existing data
    User.objects.all().delete()
    Team.objects.all().delete()
    Activity.objects.all().delete()
    Workout.objects.all().delete()
    Leaderboard.objects.all().delete()

    # Create users
    user1 = User.objects.create(username='alice', email='alice@example.com', first_name='Alice', last_name='Smith')
    user2 = User.objects.create(username='bob', email='bob@example.com', first_name='Bob', last_name='Jones')

    # Create teams
    team1 = Team.objects.create(name='Team Alpha')
    team1.members.add(user1, user2)

    # Create activities
    Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2026-04-01')
    Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2026-04-02')

    # Create workouts
    workout1 = Workout.objects.create(name='Morning Cardio', description='A quick cardio session', difficulty='Easy')
    workout2 = Workout.objects.create(name='Strength Training', description='Full body strength workout', difficulty='Medium')

    # Create leaderboard
    Leaderboard.objects.create(user=user1, score=100)
    Leaderboard.objects.create(user=user2, score=80)

    print("Test data created for users, teams, activities, workouts, and leaderboard.")

if __name__ == "__main__":
    run()
