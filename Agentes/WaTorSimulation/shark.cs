namespace WaTorSimulation
{
    public class Shark : Creature
    {
        public int StarvationTime { get; set; }
        private int timeSinceLastMeal;

        public Shark()
        {
            Age = 0;
            StarvationTime = 4; // Ajusta según tus reglas
            HasMoved = false;
            timeSinceLastMeal = 0;
        }

        public override void Move(World world, int x, int y)
        {
            if (timeSinceLastMeal >= StarvationTime)
            {
                world.Grid[x, y] = null; // El tiburón muere de hambre
                return;
            }

            List<(int, int)> adjacentPositions = new List<(int, int)>
            {
                (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
            };

            var rand = new Random();
            // Prioriza comer peces si están disponibles
            List<(int, int)> fishPositions = adjacentPositions.FindAll(pos =>
                pos.Item1 >= 0 && pos.Item1 < world.Width && pos.Item2 >= 0 && pos.Item2 < world.Height && world.Grid[pos.Item1, pos.Item2] is Fish);

            if (fishPositions.Count > 0)
            {
                var (newX, newY) = fishPositions[rand.Next(fishPositions.Count)];
                world.Grid[x, y] = null; // Deja la posición actual vacía
                world.Grid[newX, newY] = this; // Mueve el tiburón a la nueva posición
                this.HasMoved = true;
                timeSinceLastMeal = 0; // Reinicia el contador de tiempo desde la última comida
            }
            else
            {
                // Si no hay peces, busca moverse a una posición vacía
                List<(int, int)> validPositions = adjacentPositions.FindAll(pos =>
                    pos.Item1 >= 0 && pos.Item1 < world.Width && pos.Item2 >= 0 && pos.Item2 < world.Height && world.Grid[pos.Item1, pos.Item2] == null);

                if (validPositions.Count > 0)
                {
                    var (newX, newY) = validPositions[rand.Next(validPositions.Count)];
                    world.Grid[x, y] = null; // Deja la posición actual vacía
                    world.Grid[newX, newY] = this; // Mueve el tiburón a la nueva posición
                    this.HasMoved = true;
                }
            }

            timeSinceLastMeal++;
            this.Age++; // Incrementa la edad del tiburón
        }

        public override Creature Reproduce()
        {
            // Lógica de reproducción de tiburones
            if (Age >= 5)
            {
                Age = 0;
                return new Shark();
            }
            return null;
        }
    }
}

