using System;
using System.Windows.Forms;

namespace WaTorSimulation
{
    static class Program
    {
        /// <summary>
        /// Punto de entrada principal para la aplicación.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1()); // Ejecuta la forma principal que contiene la simulación.
        }
    }
}

