import pygame
import numpy as np

class Vida:
    def __init__(self, screen, screen_width, screen_height):
        # Inicializa los atributos de la clase
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Colores
        self.bg_color = (10, 10, 10)  # Fondo: casi negro
        self.alive_color = (255, 255, 255)  # Células vivas: blanco
        self.dead_color = self.bg_color  # Células muertas: mismo color que el fondo

        # Celdas
        self.n_x_cells = 80
        self.n_y_cells = 60
        self.cell_width = screen_width / self.n_x_cells
        self.cell_height = screen_height / self.n_y_cells

        # Estado del tablero: 1 = Viva, 0 = Muerta
        self.state = np.random.randint(0, 2, (self.n_x_cells, self.n_y_cells))

        # Control del juego
        self.pause = False
        self.clock = pygame.time.Clock()

    def draw_grid(self):
        """Dibuja la cuadrícula en la pantalla."""
        for y in range(self.n_y_cells):
            for x in range(self.n_x_cells):
                poly = [
                    (x * self.cell_width, y * self.cell_height),
                    ((x+1) * self.cell_width, y * self.cell_height),
                    ((x+1) * self.cell_width, (y+1) * self.cell_height),
                    (x * self.cell_width, (y+1) * self.cell_height)
                ]

                if self.state[x, y] == 0:
                    pygame.draw.polygon(self.screen, self.dead_color, poly, 1)
                else:
                    pygame.draw.polygon(self.screen, self.alive_color, poly, 0)

    def update_state(self):
        """Actualiza el estado de las células según las reglas del Juego de la Vida."""
        new_state = np.copy(self.state)
        for y in range(self.n_y_cells):
            for x in range(self.n_x_cells):
                # Número de vecinos vivos
                n_neighbors = (
                    self.state[(x-1) % self.n_x_cells, (y-1) % self.n_y_cells] +
                    self.state[x % self.n_x_cells, (y-1) % self.n_y_cells] +
                    self.state[(x+1) % self.n_x_cells, (y-1) % self.n_y_cells] +
                    self.state[(x-1) % self.n_x_cells, y % self.n_y_cells] +
                    self.state[(x+1) % self.n_x_cells, y % self.n_y_cells] +
                    self.state[(x-1) % self.n_x_cells, (y+1) % self.n_y_cells] +
                    self.state[x % self.n_x_cells, (y+1) % self.n_y_cells] +
                    self.state[(x+1) % self.n_x_cells, (y+1) % self.n_y_cells]
                )

                # Reglas del Juego de la Vida
                if self.state[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                    new_state[x, y] = 0
                elif self.state[x, y] == 0 and n_neighbors == 3:
                    new_state[x, y] = 1

        self.state = new_state

    def run(self):
        """Ejecuta el bucle principal del Juego de la Vida."""
        running = True
        while running:
            self.screen.fill(self.bg_color)
            self.clock.tick(5)

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Actualización y dibujo del estado
            self.draw_grid()
            if not self.pause:
                self.update_state()

            pygame.display.flip()
