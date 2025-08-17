# utils/settings.py
"""
SettingsManager handles loading and saving settings to a JSON file.
"""
import json
import os

class SettingsManager:
    def __init__(self, filename):
        self.filename = filename
        self.settings = {}
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.settings = json.load(f)
        else:
            self.settings = {}

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.settings, f, indent=2)

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save()
