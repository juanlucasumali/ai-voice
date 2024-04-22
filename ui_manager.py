import pygame
import logging

# Constants
BACK_COLOR = (0, 0, 0)
REC_COLOR = (255, 188, 107)
TEXT_COLOR = (255, 255, 255)
REC_SIZE = 80
KWIDTH, KHEIGHT = 20, 6
MAX_TEXT_LEN_DISPLAY = 32

class UIManager:
    def __init__(self, config):
        self.config = config
        self.width = config.ui.width
        self.height = config.ui.height
        self.fontSize = config.ui.fontSize
        pygame.display.set_icon(pygame.image.load('uno.png'))
        pygame.display.set_caption("Uno")
        self.windowSurface = pygame.display.set_mode((config.ui.width, config.ui.height), 0, 32)
        self.font = pygame.font.SysFont(None, config.ui.fontSize)

    def display_message(self, text: str):
        """
        Displays a message on the Uno application window.

        Args:
            text (str): The message text to be displayed.
        """
        logging.info(f"Displaying message: {text}")
        self.windowSurface.fill(BACK_COLOR)

        text = text[:MAX_TEXT_LEN_DISPLAY] + "..." if len(text) > MAX_TEXT_LEN_DISPLAY else text
        label = self.font.render(text, 1, TEXT_COLOR)
        size = label.get_rect()[2:4]
        self.windowSurface.blit(label, (self.width // 2 - size[0] // 2, self.height // 2 - size[1] // 2))

        pygame.display.flip()

    def display_rec_start(self):
        """
        Displays the recording start indicator on the Uno application window.
        """
        logging.info("Displaying recording start")
        self.windowSurface.fill(BACK_COLOR)
        pygame.draw.circle(self.windowSurface, REC_COLOR, (self.width // 2, self.height // 2), REC_SIZE)
        pygame.display.flip()