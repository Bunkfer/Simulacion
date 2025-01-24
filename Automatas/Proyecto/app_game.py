import pygame
import numpy as np
import random

class Game1D:
    def __init__(self, screen, screen_width, screen_height, rule='', rule_type='Decimal'):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Colores
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # Variables del autómata
        self.cells_per_row = 100  # Número de celdas por fila
        self.cell_size = screen_width // self.cells_per_row
        self.max_rows = screen_height // self.cell_size  # Máximo de filas que caben en la pantalla
        
        # Regla inicial
        self.rule_number = random.randint(0, 256) if rule == '' else int(rule)
        self.rule_type = rule_type

        # Estado inicial (fila central activa)
        self.current_state = np.random.choice([0, 1], size=self.cells_per_row)

    def set_rule(self, rule):
        """Establece una nueva regla para el autómata."""
        self.rule_number = int(rule)

    def get_next_state(self, current_state, rule_binary):
        """Calcula el siguiente estado del autómata basado en la regla."""
        next_state = np.zeros_like(current_state)
        for i in range(1, len(current_state)-1):
            pattern = ''.join(str(x) for x in current_state[i-1:i+2])
            next_state[i] = rule_binary[7-int(pattern, 2)]
        return next_state

    def draw_row(self, row, state):
        """Dibuja una fila del autómata en la pantalla."""
        for i, cell in enumerate(state):
            color = self.BLACK if cell == 1 else self.WHITE
            pygame.draw.rect(self.screen, color, (i * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

    def run(self):
        """Ejecuta el bucle principal del autómata 1D."""
        running = True
        row = 0  # Contador de filas dibujadas
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Cambiar la regla con la tecla 'r'
                        self.rule_number = (self.rule_number + 1) % 256
                        print(f"Regla cambiada a: {self.rule_number}")

            # Convertir el número de regla a binario
            rule_binary = np.array([int(x) for x in np.binary_repr(self.rule_number, width=8)])

            # Dibujar el estado actual
            self.draw_row(row, self.current_state)

            # Actualizar para el siguiente estado
            if row < self.max_rows - 1:
                self.current_state = self.get_next_state(self.current_state, rule_binary)
                row += 1
            else:
                # Reiniciar el autómata para demostración
                self.current_state = np.random.choice([0, 1], size=self.cells_per_row)
                row = 0
                self.screen.fill(self.BLACK)  # Limpia la pantalla

            pygame.display.flip()
