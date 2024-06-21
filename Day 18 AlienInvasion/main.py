import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from limit_line import LimitLine  # Import the LimitLine class


def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    limit_line = LimitLine(ai_settings, screen)  # Create an instance of LimitLine

    pygame.display.set_caption("Alien Invasion")

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        limit_line.draw_line()  # Draw the limit line
        pygame.display.flip()  # Update the display


run_game()
