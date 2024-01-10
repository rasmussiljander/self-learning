# Traffic Simulation
The following program is an elemetary traffic simulation where cars depart from random points on the screen and evade each other on their way to their destination. A comprehensive documentation (in Finnish) can be found in the folder  **doc**. The source code can be find in the folder **src**.

The program is animation-based, and is based on the physics features presented in two works, Daniel Shiffman's **The Nature of Code** (Chapter 6: Autonomous Agents) and Greg Reynolds' **Steering Behaviors for Autonomous Characters**. 

In principle, the program consists of two key class groups:
  a) User Interface classes (GUI, VehicleGraphicsItem, VehicleWorld)
  b) Vehicle feature and movement classes (Path, Vector, Vehicle)
The movement and positions of the vehicles were implemented by the classes of type b), and the UI and animation part of the program was done by classes of type a).

## Used Libraries
math, random, PyQt5 (for the UI, modules QtWidgets, QtCore, QtGui)

To run the project ensure that you have installed `PyQt5`. You can execute the code by running the script `src/main.py`.