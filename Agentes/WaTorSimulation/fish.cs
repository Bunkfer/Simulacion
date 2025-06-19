namespace WaTorSimulation
{
    public class Fish : Creature
    {
        public Fish()
        {
            Age = 0;
            HasMoved = false;
        }

        public override void Move(World world, int x, int y)
        {
            List<(int, int)> adjacentPositions = new List<(int, int)>
            {
                (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
            };

            List<(int, int)> validPositions = adjacentPositions.FindAll(pos =>
                pos.Item1 >= 0 && pos.Item1 < world.Width && pos.Item2 >= 0 && pos.Item2 < world.Height && world.Grid[pos.Item1, pos.Item2] == null);

            if (validPositions.Count > 0)
            {
                var rand = new Random();
                var (newX, newY) = validPositions[rand.Next(validPositions.Count)];

                world.Grid[x, y] = null; // Deja la posición actual vacía
                world.Grid[newX, newY] = this; // Mueve el pez a la nueva posición
                this.HasMoved = true;
            }

            this.Age++; // Incrementa la edad del pez
        }

        public override Creature Reproduce()
        {
            // Lógica de reproducción de peces
            if (Age >= 4)
            {
                Age = 0;
                return new Fish();
            }
            return null;
        }
    }
}

