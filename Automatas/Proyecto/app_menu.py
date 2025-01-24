import pygame
import sys

class GameMenu:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Colores
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        # Fuente
        self.font = pygame.font.Font(None, 36)
        
        # Variables de entrada
        self.active_dec = False
        self.rule_dec = ''
        self.active_bin = False
        self.rule_bin = ''

        # Estados iniciales de los checkboxes
        self.checkbox_Dec_checked = True
        self.checkbox_Bin_checked = False

    def draw_text(self, text, color, x, y):
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.screen.blit(textobj, textrect)

    def draw_input_box(self, x, y, label_text, is_active, text):
        input_box = pygame.Rect(x + 150, y, 140, 32)
        self.draw_text(label_text, self.WHITE, x, y + 5)
        pygame.draw.rect(self.screen, self.WHITE, input_box, 2)
        if is_active:
            self.draw_text(text, self.WHITE, input_box.x + 5, input_box.y + 5)
        return input_box

    def draw_checkbox(self, rect, checked, label_text, x, y):
        pygame.draw.rect(self.screen, self.WHITE, rect, 2)
        self.draw_text(label_text, self.WHITE, x, y)
        if checked:
            pygame.draw.line(self.screen, self.WHITE, rect.topleft, rect.bottomright, 2)
            pygame.draw.line(self.screen, self.WHITE, rect.bottomleft, rect.topright, 2)

    def draw_rules(self):
        def draw_square(x, y, filled):
            square = pygame.Rect(x, y, 10, 10)
            if filled:
                pygame.draw.rect(self.screen, self.BLUE, square)
            else:
                pygame.draw.rect(self.screen, self.BLUE, square, 2)

        positions = [
            ('Primer digito: ', 50, 400, 0, 0, 0),
            ('Segundo digito: ', 50, 450, 0, 0, 1),
            ('Tercer digito: ', 50, 500, 0, 1, 0),
            ('Cuarto digito: ', 50, 550, 0, 1, 1),
            ('Quinto digito: ', 450, 400, 1, 0, 0),
            ('Sexto digito: ', 450, 450, 1, 0, 1),
            ('Septimo digito: ', 450, 500, 1, 1, 0),
            ('Octavo digito: ', 450, 550, 1, 1, 1),
        ]

        for text, x, y, a, b, c in positions:
            self.draw_text(text, self.BLUE, x, y)
            draw_square(x + 200, y + 7, a == 1)
            draw_square(x + 212, y + 7, b == 1)
            draw_square(x + 224, y + 7, c == 1)

    def run(self):
        click = False
        while True:
            self.screen.fill(self.BLACK)
            self.draw_text('Automatas celulares', self.WHITE, 20, 20)

            mx, my = pygame.mouse.get_pos()
            button_1 = pygame.Rect(50, 100, 300, 50)
            button_2 = pygame.Rect(450, 100, 300, 50)

            checkbox_Dec = pygame.Rect(50, 200, 20, 20)
            self.draw_checkbox(checkbox_Dec, self.checkbox_Dec_checked, "Decimal", 100, 200)
            if self.checkbox_Dec_checked:
                input_box_dec = self.draw_input_box(450, 200, 'Regla Dec:', self.active_dec, self.rule_dec)

            checkbox_Bin = pygame.Rect(50, 300, 20, 20)
            self.draw_checkbox(checkbox_Bin, self.checkbox_Bin_checked, "Binario", 100, 300)
            if self.checkbox_Bin_checked:
                input_box_bin = self.draw_input_box(450, 300, 'Regla Bin:', self.active_bin, self.rule_bin)
                self.draw_rules()

            if button_1.collidepoint((mx, my)):
                if click:
                    # Aquí llamarías a la función para ejecutar el Juego de la Vida
                    pass

            if button_2.collidepoint((mx, my)):
                if click:
                    # Aquí llamarías a la función para ejecutar el autómata 1D
                    pass

            pygame.draw.rect(self.screen, self.GREEN, button_1)
            self.draw_text('Juego de la Vida', self.BLACK, button_1.x + 50, button_1.y + 10)

            pygame.draw.rect(self.screen, self.GREEN, button_2)
            self.draw_text('Automatas 1d', self.BLACK, button_2.x + 70, button_2.y + 10)

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if checkbox_Dec.collidepoint(event.pos):
                            self.checkbox_Dec_checked = not self.checkbox_Dec_checked
                            self.checkbox_Bin_checked = False
                        elif checkbox_Bin.collidepoint(event.pos):
                            self.checkbox_Bin_checked = not self.checkbox_Bin_checked
                            self.checkbox_Dec_checked = False
                        click = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.checkbox_Dec_checked and input_box_dec.collidepoint(event.pos):
                        self.active_dec = not self.active_dec
                    else:
                        self.active_dec = False

                    if self.checkbox_Bin_checked and input_box_bin.collidepoint(event.pos):
                        self.active_bin = not self.active_bin
                    else:
                        self.active_bin = False

                if event.type == pygame.KEYDOWN:
                    if self.active_dec:
                        if event.key == pygame.K_RETURN:
                            print(self.rule_dec)
                            self.rule_dec = ''
                        elif event.key == pygame.K_BACKSPACE:
                            self.rule_dec = self.rule_dec[:-1]
                        elif len(self.rule_dec) < 3:
                            self.rule_dec += event.unicode

                    if self.active_bin:
                        if event.key == pygame.K_RETURN:
                            print(self.rule_bin)
                            self.rule_bin = ''
                        elif event.key == pygame.K_BACKSPACE:
                            self.rule_bin = self.rule_bin[:-1]
                        elif len(self.rule_bin) < 8:
                            self.rule_bin += event.unicode

            pygame.display.update()
