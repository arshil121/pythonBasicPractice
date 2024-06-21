import pygame


class LimitLine:
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.color = ai_settings.line_color
        self.width = ai_settings.line_width
        self.height = ai_settings.screen_height * 0.7

    def draw_line(self):
        pygame.draw.line(
            self.screen,
            self.color,
            (0, self.height),
            (self.screen.get_rect().width, self.height),
            self.width,
        )
