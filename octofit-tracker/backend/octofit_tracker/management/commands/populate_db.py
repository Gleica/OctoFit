from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Popula o banco de dados octofit_db com dados de teste.'

    def handle(self, *args, **kwargs):
        # Limpa os dados existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Cria usuários com _id gerado automaticamente
        users = [
            User(_id=ObjectId(), username='john_doe', email='john_doe@example.com', password='password123'),
            User(_id=ObjectId(), username='jane_smith', email='jane_smith@example.com', password='password123'),
            User(_id=ObjectId(), username='alice_wonder', email='alice_wonder@example.com', password='password123'),
        ]
        for user in users:
            user.save()

        # Cria equipes
        team1 = Team(name='Team Alpha')
        team2 = Team(name='Team Beta')
        team1.save()
        team2.save()
        team1.members.add(users[0], users[1])
        team2.members.add(users[2])

        # Cria atividades
        activities = [
            Activity(user=users[0], activity_type='Running', duration=timedelta(minutes=30)),
            Activity(user=users[1], activity_type='Cycling', duration=timedelta(minutes=45)),
            Activity(user=users[2], activity_type='Swimming', duration=timedelta(minutes=60)),
        ]
        for activity in activities:
            activity.save()

        # Cria placares
        leaderboard_entries = [
            Leaderboard(user=users[0], score=100),
            Leaderboard(user=users[1], score=150),
            Leaderboard(user=users[2], score=200),
        ]
        for entry in leaderboard_entries:
            entry.save()

        # Cria treinos
        workouts = [
            Workout(name='Morning Run', description='A 5km run to start the day'),
            Workout(name='Cycling Session', description='A 20km cycling session'),
            Workout(name='Swimming Laps', description='30 minutes of swimming laps'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))