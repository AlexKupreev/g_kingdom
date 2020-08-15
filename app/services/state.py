"""State Service"""


class StateService:
    """Basic State logic."""

    @classmethod
    def generate_state(cls, state, settings, last_states=None):
        """Wrapper for generation of a state."""

        if len(last_states) == 0:
            return StateService.generate_initial_state(settings)

        return state

    @classmethod
    def generate_initial_state(cls, settings):
        """Wrapper for generation of a new state."""

        # gold in a budget
        gold = db.Column(db.Integer, nullable=False, default=0)
        # population in a city
        population = db.Column(db.Integer, nullable=False, default=0)
        # army in a city (<= population)
        army = db.Column(db.Integer, nullable=False, default=0)
        # enemies around a city
        enemies = db.Column(db.Integer, nullable=False, default=0)
        # reaction move
        reaction_move = db.Column(db.Text, nullable=True, default=None)
