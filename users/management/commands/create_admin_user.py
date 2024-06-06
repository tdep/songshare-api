from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError


class Command(createsuperuser.Command):
    help = "Method for creating admin user"

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "--password",
            dest='password',
            default=None,
            help='Set the admin password',
        )
        parser.add_argument(
            "--phone_number",
            dest='phone_number',
            default=None,
            help='Set the admin phone number'
        )
        parser.add_argument(
            "--first_name",
            dest='first_name',
            default=None,
            help='Set the admin account holder\'s first name'
        )

    def handle(self, *args, **options):
        options.setdefault('interactive', False)
        database = options.get('database')
        password = options.get('password')
        username = options.get('username')
        email = options.get('email')
        phone_number = options.get('phone_number')
        first_name = options.get('first_name')

        if not password or not username or not email or not phone_number or not first_name:
            raise CommandError(
                "--email, --username, --password, --phone_number, and --first_name are required options."
            )

        user_data = {
            'username': username,
            'password': password,
            'phone_number': phone_number,
            'email': email,
            'first_name': first_name
        }

        self.UserModel._default_manager.db_manager(
            database).create_superuser(**user_data)
        if options.get('verbosity', 0) >= 1:
            self.stdout.write("Admin user created successfully.")



