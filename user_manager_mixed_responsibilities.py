class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class UserRepository:
    def save(self, user):
        print(f"Saving user {user.username} to database")


class EmailService:
    def send_welcome_email(self, user):
        print(f"Sending welcome email to {user.email}")


class UserReport:
    def generate(self, user):
        print(f"User report for {user.username}")