class GameStats:
    """Track statistics for the game"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start the game in an active state
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
