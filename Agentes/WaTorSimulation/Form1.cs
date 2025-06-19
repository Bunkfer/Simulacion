namespace WaTorSimulation;

using System;
using System.Drawing;
using System.Windows.Forms;

public partial class Form1 : Form
{
    private World world;
    private Timer timer;
    // Tamaño de cada celda en la cuadrícula ajustado para ser más grande
    private const int CellSize = 10; 
    // Factor de escala para el tamaño de la ventana ajustado para ser más grande
    private const int WindowScale = 2; 

    public Form1()
    {
        InitializeComponent();
        // Configura el tamaño de tu mundo aquí
        world = new World(30, 30); 

        // Para reducir el parpadeo durante la re-dibujación
        this.DoubleBuffered = true; 
        // Ajusta el tamaño de la ventana para ser mucho más grande
        this.ClientSize = new Size(world.Width * CellSize * WindowScale, world.Height * CellSize * WindowScale); 

        SetupTimer();
    }

    private void SetupTimer()
    {
        timer = new Timer
        {
            // Intervalo de tiempo (en milisegundos) para la simulación
            Interval = 1000 
        };
        timer.Tick += (sender, e) => {
            world.SimulateStep();
            // Marca el formulario para ser repintado, lo que desencadena el evento Paint
            this.Invalidate(); 
        };
        timer.Start();
    }

    protected override void OnPaint(PaintEventArgs e)
    {
        base.OnPaint(e);
        DrawWorld(e.Graphics);
    }

    private void DrawWorld(Graphics graphics)
    {
        // Calcula el tamaño de celda escalado
        int scaledCellSize = CellSize * WindowScale; 

        for (int x = 0; x < world.Width; x++)
        {
            for (int y = 0; y < world.Height; y++)
            {
                // Usa el tamaño de celda escalado aquí para cada celda
                Rectangle cellRect = new Rectangle(x * scaledCellSize, y * scaledCellSize, scaledCellSize, scaledCellSize); 

                if (world.Grid[x, y] is Fish)
                {
                    graphics.FillRectangle(Brushes.Blue, cellRect);
                }
                else if (world.Grid[x, y] is Shark)
                {
                    graphics.FillRectangle(Brushes.Red, cellRect);
                }
            }
        }
    }
}

