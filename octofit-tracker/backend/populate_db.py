"""
Script to populate the octofit_db MongoDB database with test data for users, teams, activities, leaderboard, and workouts collections.
Run this script with the Django environment loaded.
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

# Example: Add your models and test data creation logic here
# from octofit_tracker.models import ...

def run():
    # TODO: Implement test data creation for users, teams, activities, leaderboard, and workouts
    print("Test data creation not yet implemented.")

if __name__ == "__main__":
    run()
