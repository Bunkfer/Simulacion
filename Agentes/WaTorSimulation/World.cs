using System;
using System.Collections.Generic;

namespace WaTorSimulation
{
    public class World
    {
        public Creature[,] Grid { get; private set; }
        public int Width { get; private set; }
        public int Height { get; private set; }
        private Random rand = new Random();

        public World(int width, int height)
        {
            Width = width;
            Height = height;
            Grid = new Creature[width, height];
            InitializeWorld();
        }

        private void InitializeWorld()
        {
            for (int i = 0; i < Width; i++)
            {
                for (int j = 0; j < Height; j++)
                {
                    if (rand.NextDouble() < 0.1) // 10% de posibilidad de un tiburón
                    {
                        Grid[i, j] = new Shark();
                    }
                    else if (rand.NextDouble() < 0.3) // 20% de posibilidad de un pez, después de quitar tiburones
                    {
                        Grid[i, j] = new Fish();
                    }
                }
            }
        }

        public void SimulateStep()
        {
            // Primero, restablece el estado de movimiento para todas las criaturas
            foreach (var creature in Grid)
            {
                if (creature != null)
                {
                    creature.HasMoved = false;
                }
            }

            // Luego, mueve cada criatura
            for (int x = 0; x < Width; x++)
            {
                for (int y = 0; y < Height; y++)
                {
                    Creature creature = Grid[x, y];
                    if (creature != null && !creature.HasMoved)
                    {
                        creature.Move(this, x, y);
                        creature.HasMoved = true; // Asegúrate de marcar la criatura como movida después del movimiento
                    }
                }
            }

            // Finalmente, maneja la reproducción
            for (int x = 0; x < Width; x++)
            {
                for (int y = 0; y < Height; y++)
                {
                    Creature creature = Grid[x, y];
                    if (creature != null && creature.HasMoved)
                    {
                        Creature baby = creature.Reproduce();
                        if (baby != null)
                        {
                            PlaceNewCreature(x, y, baby); // Coloca el nuevo bebé en una ubicación válida si es posible
                        }
                    }
                }
            }
        }

        private void PlaceNewCreature(int x, int y, Creature baby)
        {
            List<(int, int)> adjacentPositions = new List<(int, int)>
            {
                (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),
                (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1)
            };

            List<(int, int)> validPositions = adjacentPositions.FindAll(pos =>
                pos.Item1 >= 0 && pos.Item1 < Width && pos.Item2 >= 0 && pos.Item2 < Height && Grid[pos.Item1, pos.Item2] == null);

            if (validPositions.Count > 0)
            {
                var (newX, newY) = validPositions[rand.Next(validPositions.Count)];
                Grid[newX, newY] = baby;
            }
            // Si no hay espacio disponible, la criatura no se coloca.
        }
    }
}


