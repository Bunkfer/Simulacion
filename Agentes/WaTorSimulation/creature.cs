namespace WaTorSimulation
{
    public abstract class Creature
    {
        public int Age { get; set; }
        public bool HasMoved { get; set; }

        public abstract void Move(World world, int x, int y);
        public abstract Creature Reproduce();
    }
}
