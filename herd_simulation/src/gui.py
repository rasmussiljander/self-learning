"""GUI class.

    Inits and implementations largely based on Exercise week 5, RobotWorld."""
from PyQt5 import QtWidgets, QtCore, QtGui
from vehicle_graphics_item import VehicleGraphicsItem


class GUI(QtWidgets.QMainWindow):
    def __init__(self, world):
        super().__init__()

        self.world = world

        self.show_window()
        self.exit_button()
        self.add_vehicle_graphics_item()

        self.timer = QtCore.QBasicTimer()
        self.timer.start(
            10, self
        )  # Timer event: Important for creating movement! Essential in setting up the
        # Repainting and update-event'''

    """Builds window for viewer to see."""

    def show_window(self):
        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.setWindowTitle("Traffic Simulation")  # creating window
        self.centralWidget().setLayout(self.horizontal)
        self.setGeometry(300, 100, 1000, 800)
        self.show()

        self.scene = QtWidgets.QGraphicsScene()  # creating scene for adding items
        self.scene.setSceneRect(0, 0, 700, 700)

        self.view = QtWidgets.QGraphicsView(
            self.scene, self
        )  # view must be added for showing the scene
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)

    """Adding exit button for easy termination of program"""

    def exit_button(self):
        self.exit_btn = QtWidgets.QPushButton("Press to exit")
        self.horizontal.addWidget(self.exit_btn)

        self.exit_btn.clicked.connect(self.close)

    """Adding all vehicle graphics items (created in class VehicleGraphicsItem)"""

    def add_vehicle_graphics_item(self):
        vehicle_list = self.world.get_vehicles()
        for vehicle in vehicle_list:
            vehicle_graphics = VehicleGraphicsItem(vehicle)
            self.scene.addItem(vehicle_graphics)

    """methods for updating vehicle position, direction, etc. All methods written in graphicsItem class."""

    def update_vehicles(self):
        vehicles = self.scene.items()
        for i in range(len(vehicles)):
            graphics__veh = vehicles[i]
            graphics__veh.vehicle.path_following()
            graphics__veh.update_position()
            graphics__veh.update_rotation()

        self.update()

    """Call for repainting the world and showing movement in the vehicles"""

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.update_vehicles()
        else:
            QtGui.QFrame.timerEvent(self, event)
