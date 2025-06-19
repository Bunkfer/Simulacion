# Automatas

## 📜 **Description**

Cellular automata, such as 1D automata and the Game of Life, are dynamic systems composed of cells that evolve over time based on simple rules and the state of their neighbors. In one-dimensional automata, a single row of cells updates according to a predefined rule, producing patterns that range from predictable to chaotic. The Game of Life, set on a two-dimensional grid, generates surprisingly complex and self-organizing structures from minimal rules governing cell birth and death. Both models showcase how complexity can emerge from simplicity, making them powerful tools for exploring self-organization, natural computation, and the simulation of real-world systems.

---

## 🚀 *How to Run the Project*

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:

   ```bash
   python main.py
   ```

---

## 🚀 *How to Run the Project in docker*

You need to have a server installed like Xlaunch of vcxsrv

1. Build the image:

   ```bash
   docker build -t bunkfer/automatas .
   ```

2. Run the container:

   ```bash
   docker run -dit --name automatas -e DISPLAY=host.docker.internal:0.0 bunkfer/automatas
   ```

---

## 🖼️ **Appendix**

We created a Docker image that is use as the base for this project.

PyQt5 = 5.15.11
matplotlib = 3.10.1
pandas = 2.2.3
numpy = 2.2.4
scipy = 1.15.2

[Base Image](https://hub.docker.com/r/bunkfer/pyqt5)

---

## 📚 **References**

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Numpy Documentation](https://numpy.org/doc/)
---