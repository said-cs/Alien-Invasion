class GameStats:
    """Track sttistics for Alien Invasion"""

    def __init__(self, ai_game):
        """initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ship_left = self.settings.ship_limit