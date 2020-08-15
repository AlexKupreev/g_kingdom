import click
from flask.cli import FlaskGroup

from app.app import create_app


def create_app(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Create a new admin user
    """
    from app.extensions import db
    from app.models import User

    click.echo("create user")
    user = User(
        username="admin", email="admin@example.com", password="password", active=True
    )
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()
