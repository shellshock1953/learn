class Settings:
    def __init__(self) -> None:
        # width and height will be overriten if in fullscreen
        self.screen_width = 900
        self.screen_height = 800
        self.bg_color = (57, 117, 165)
        self.ship_speed = 1.5

        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # TODO: show number of left bullets
        # TODO: add additional bullets as a bonus
        self.bullets_allowed = 3
