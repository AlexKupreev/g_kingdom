"""Settings Service"""
import os
import yaml

from flask import current_app


class SettingsService:
    """Basic Settings logic."""

    GAME_SETTINGS_ROOT = "settings"
    GAME_SETTINGS = ["gold_earn", "gold_spent_worker", "gold_spent_army",
                     "win_probability", "enemy_increase", "uncertain_gold",
                     "uncertain_population", "uncertain_army"]

    INITIAL_VALUES = []

    @classmethod
    def load_game_conf(cls):
        """Load game configuration.

        :return: dict of settings
        """
        settings_file = current_app.config.get('GAME_SETTINGS_FILE')
        if not settings_file:
            raise RuntimeError("GAME_SETTINGS_FILE is not set")

        settings_file = os.path.join(current_app.instance_path, settings_file)
        if not os.path.isfile(settings_file):
            raise RuntimeError("Configuration file not found")

        with open(settings_file) as f:
            settings = yaml.safe_load(f)

        return settings

    @classmethod
    def initialize(cls, settings):
        """Init settings at the start.

        :param settings: Settings model
        :return: Settings model - filled with data
        """

        settings_obj = SettingsService.load_game_conf()

        for entry in SettingsService.GAME_SETTINGS:
            value = settings_obj.get(SettingsService.GAME_SETTINGS_ROOT, {}).get(entry, None)
            if value is None:
                raise RuntimeError(f"Entry {entry} is missing in settings.")

            settings[entry] = float(value)

        return settings
