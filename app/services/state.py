from app.models import State


class StateService:
    """Basic State logic."""

    @classmethod
    def generate_state(cls, settings, last_states=None):
        """Wrapper for generation of a new state."""

        if len(last_states) == 0:
            return StateService.generate_initial_state()

        return state

    @classmethod
    def generate_initial_state(self):
        """Wrapper for generation of a new state."""
