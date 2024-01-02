from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

class Text:
    # If using a custom font, pass in the font_path to the font parameter instead
    def __init__(self, text: str, font: str, size: int, color: tuple, x: int, y: int, antialiasing=False, to_blit=True):
        '''
        If you wish to draw a pygame text onto the screen, here is an example
        if text.to_blit:
            window.blit(text.render, text.rect_obj)
        '''
        self.text = text
        self.font = font
        self.size = size
        self.color = color
        self.x, self.y = x, y # The X position where the text will begin to be printed from left to right
        self.antialiasing = antialiasing
        # This is if the text should be drawn onto the screen or not. 
        self.to_blit = to_blit

        # Get the font render, the font rect obj and calculate its center, and the font obj
        self.render, self.rect_obj, self.rect_obj.center, font_obj = self.get_render_and_rect_obj()

        # Uses the font obj to calculate the width and height of the text in pixels
        self.width, self.height = font_obj.size(self.text)

    def get_render_and_rect_obj(self):
        # input: (self)
        # output: The font render, the font_obj as a rectangle, and the font object itself
        font_obj = pygame.font.Font(self.font, self.size)
        render = font_obj.render(self.text, self.antialiasing, self.color)
        rect_obj = render.get_rect()

        text_width, text_height = font_obj.size(self.text)

        # Calculating the coords of the midpoint of the rectangle of the font obj
        midpoint_x = (self.x + text_width) / 2 + 1/2 * self.x
        midpoint_y = (self.y + (self.y + text_height)) / 2
        
        return render, rect_obj, (midpoint_x, midpoint_y), font_obj
      