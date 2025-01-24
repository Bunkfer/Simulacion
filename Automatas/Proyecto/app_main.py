import pygame
import sys
import random
from app_game import Game1D
from app_vida import Vida
from app_menu import GameMenu

class MainApp:
    def __init__(self):
        # Inicialización de Pygame
        pygame.init()
        pygame.display.set_caption("Simulacion de automatas celulares")

        # Configuración de la ventana
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Crear instancias de las clases
        self.vida_game = Vida(self.screen, self.screen_width, self.screen_height)
        self.automata_1d = Game1D(self.screen, self.screen_width, self.screen_height)
        self.menu = GameMenu(self.screen, self.screen_width, self.screen_height)

        # Variables de entrada y checkboxes
        self.checkbox_Dec = pygame.Rect(50, 200, 20, 20)
        self.checkbox_Bin = pygame.Rect(50, 300, 20, 20)
        self.menu.checkbox_Dec_checked = True
        self.menu.checkbox_Bin_checked = False
        self.rule_dec = ""
        self.rule_bin = ""

    def start_vida(self):
        self.vida_game.run()

    def start_game1d(self):
        self.automata_1d.run()

    def run(self):
        while True:
            self.menu.screen.fill(self.menu.BLACK)
            self.menu.draw_text('Automatas celulares', self.menu.WHITE, 20, 20)

            # Dibujar botones del menú
            mx, my = pygame.mouse.get_pos()
            button_1 = pygame.Rect(50, 100, 300, 50)
            button_2 = pygame.Rect(450, 100, 300, 50)

            pygame.draw.rect(self.menu.screen, self.menu.GREEN, button_1)
            self.menu.draw_text('Juego de la Vida', self.menu.BLACK, button_1.x + 50, button_1.y + 10)

            pygame.draw.rect(self.menu.screen, self.menu.GREEN, button_2)
            self.menu.draw_text('Automatas 1D', self.menu.BLACK, button_2.x + 70, button_2.y + 10)

            # Dibujar y manejar checkboxes
            self.menu.draw_checkbox(self.checkbox_Dec, self.menu.checkbox_Dec_checked, "Decimal", 100, 200)
            self.menu.draw_checkbox(self.checkbox_Bin, self.menu.checkbox_Bin_checked, "Binario", 100, 300)

            # Mostrar y manejar cuadros de texto
            if self.menu.checkbox_Dec_checked:
                input_box_dec = self.menu.draw_input_box(450, 200, "Regla Dec:", True, self.rule_dec)
            if self.menu.checkbox_Bin_checked:
                input_box_bin = self.menu.draw_input_box(450, 300, "Regla Bin:", True, self.rule_bin)
                self.menu.draw_rules()

            # Manejando clics en botones
            if button_1.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    self.start_vida()

            if button_2.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    if self.menu.checkbox_Dec_checked:
                        if self.rule_dec == "":
                            self.automata_1d.set_rule(random.randint(0, 255))  # Si no hay regla, usa un valor aleatorio
                        elif int(self.rule_dec) < 256:
                            self.automata_1d.set_rule(self.rule_dec)  # Usa la regla decimal ingresada
                        else:
                            print("El máximo aceptado son 255")
                    elif self.menu.checkbox_Bin_checked:
                        try:
                            rule_conv_bin = int(self.rule_bin, 2)  # Convierte la regla binaria a decimal
                            self.automata_1d.set_rule(rule_conv_bin)
                        except ValueError:
                            print("La regla debe ser escrita en binario")
                    self.automata_1d.run()  # Ejecuta el autómata con la regla configurada

            # Manejando eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.checkbox_Dec.collidepoint(event.pos):
                            self.menu.checkbox_Dec_checked = not self.menu.checkbox_Dec_checked
                            self.menu.checkbox_Bin_checked = False
                        elif self.checkbox_Bin.collidepoint(event.pos):
                            self.menu.checkbox_Bin_checked = not self.menu.checkbox_Bin_checked
                            self.menu.checkbox_Dec_checked = False
                elif event.type == pygame.KEYDOWN:
                    if self.menu.checkbox_Dec_checked:
                        if event.key == pygame.K_BACKSPACE:
                            self.rule_dec = self.rule_dec[:-1]
                        elif event.key == pygame.K_RETURN:
                            print(f"Regla decimal seleccionada: {self.rule_dec}")
                        elif len(self.rule_dec) < 3 and event.unicode.isdigit():
                            self.rule_dec += event.unicode
                    elif self.menu.checkbox_Bin_checked:
                        if event.key == pygame.K_BACKSPACE:
                            self.rule_bin = self.rule_bin[:-1]
                        elif event.key == pygame.K_RETURN:
                            print(f"Regla binaria seleccionada: {self.rule_bin}")
                        elif len(self.rule_bin) < 8 and event.unicode in '01':
                            self.rule_bin += event.unicode

            pygame.display.update()

