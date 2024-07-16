class Settings:
    def __init__(self) -> None:
        # TODO: show number of left bullets
        # TODO: add additional bullets as a bonus
        self.bg_color = (57, 117, 165)
        self.bullet_color = (60, 60, 60)
        self.bullet_height = 45
        self.bullet_width = 9
        self.bullets_allowed = 3
        self.fleet_drop_speed = 10
        self.screen_height = 800
        self.screen_width = 900
        self.ship_limit = 3
        self.speedup_scale = 1.2
        self.score_scale = 1.5
        self.score_shipts_image_scale = 0.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 5
        self.bullet_speed = 10
        self.alien_speed = 1.5
        self.fleet_direction = 1
        self.alien_points = 20

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
