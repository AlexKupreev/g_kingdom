import os

from flask import current_app


class SettingsService:
    """Basic Settings logic."""

    @classmethod
    def load_game_conf(cls):
        """Load game configuration."""
        settings_file = current_app.config.get('GAME_SETTINGS_FILE')
        if not settings_file:
            raise RuntimeError("GAME_SETTINGS_FILE is not set")

        settings_file = os.path.join(current_app.instance_path, settings_file)
        if not os.path.isfile(settings_file):
            raise RuntimeError("Configuration file not found")

        


    @classmethod
    def initialize(cls, settings):
        """Init settings at the start."""

        settings.gold_earn = 1.0
        settings.gold_spent_worker = 0.5
        settings.gold_spent_army = 0.8
        settings.win_probability = 0.5
        settings.enemy_increase = 1.5
        settings.uncertain_gold = 0.2
        settings.uncertain_population = 0.1
        settings.uncertain_army = 0.1

        return settings
