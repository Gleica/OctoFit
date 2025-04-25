from django.core.management.base import BaseCommand # type: ignore
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data for users, teams, activities, leaderboard, and workouts collections.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create and save users
        users = []
        user_data = [
            {'username': 'thundergod', 'email': 'thundergod@mhigh.edu', 'password': 'thundergodpassword'},
            {'username': 'metalgeek', 'email': 'metalgeek@mhigh.edu', 'password': 'metalgeekpassword'},
            {'username': 'zerocool', 'email': 'zerocool@mhigh.edu', 'password': 'zerocoolpassword'},
            {'username': 'crashoverride', 'email': 'crashoverride@hmhigh.edu', 'password': 'crashoverridepassword'},
            {'username': 'sleeptoken', 'email': 'sleeptoken@mhigh.edu', 'password': 'sleeptokenpassword'},
        ]
        for data in user_data:
            user = User.objects.create(**data)
            users.append(user)

        # Create and save teams
        team1 = Team.objects.create(name='Blue Team')
        team2 = Team.objects.create(name='Gold Team')
        team1.members.set([users[0], users[1]])
        team2.members.set([users[2], users[3], users[4]])

        # Create and save activities
        activity_data = [
            {'user': users[0], 'activity_type': 'Cycling', 'duration': timedelta(hours=1)},
            {'user': users[1], 'activity_type': 'Crossfit', 'duration': timedelta(hours=2)},
            {'user': users[2], 'activity_type': 'Running', 'duration': timedelta(hours=1, minutes=30)},
            {'user': users[3], 'activity_type': 'Strength', 'duration': timedelta(minutes=30)},
            {'user': users[4], 'activity_type': 'Swimming', 'duration': timedelta(hours=1, minutes=15)},
        ]
        for data in activity_data:
            Activity.objects.create(**data)

        # Create and save leaderboard entries
        leaderboard_data = [
            {'user': users[0], 'score': 100},
            {'user': users[1], 'score': 90},
            {'user': users[2], 'score': 95},
            {'user': users[3], 'score': 85},
            {'user': users[4], 'score': 80},
        ]
        for data in leaderboard_data:
            Leaderboard.objects.create(**data)

        # Create and save workouts
        workout_data = [
            {'name': 'Cycling Training', 'description': 'Training for a road cycling event'},
            {'name': 'Crossfit', 'description': 'Training for a crossfit competition'},
            {'name': 'Running Training', 'description': 'Training for a marathon'},
            {'name': 'Strength Training', 'description': 'Training for strength'},
            {'name': 'Swimming Training', 'description': 'Training for a swimming competition'},
        ]
        for data in workout_data:
            Workout.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the octofit_db database with test data.'))