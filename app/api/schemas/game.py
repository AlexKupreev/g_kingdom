from app.models import Game
from app.extensions import ma, db


class GameSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)

    class Meta:
        model = Game
        sqla_session = db.session
        load_instance = True
