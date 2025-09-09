# ==============================
# PySide6 Notes (Beginner to Advanced)
# Author: Your Name
# ==============================

# Import necessary PySide6 modules
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QPushButton, QLineEdit, QTextEdit,
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QTableWidget, QTableWidgetItem,
    QTabWidget, QStackedWidget, QMenuBar, QToolBar
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt


# Main Window Class
class NotesApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("PySide6 Notes - Beginner to Advanced")
        self.setGeometry(100, 100, 900, 600)

        # Central widget (container for everything inside main window)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a stacked widget (for navigation between different "pages")
        self.stacked_widget = QStackedWidget()

        # Create all pages (Beginner, Layouts, Tables, Tabs, Advanced)
        self.page1 = self.create_basic_page()
        self.page2 = self.create_layouts_page()
        self.page3 = self.create_table_page()
        self.page4 = self.create_tabs_page()
        self.page5 = self.create_styling_page()

        # Add all pages to stacked widget
        self.stacked_widget.addWidget(self.page1)  # index 0
        self.stacked_widget.addWidget(self.page2)  # index 1
        self.stacked_widget.addWidget(self.page3)  # index 2
        self.stacked_widget.addWidget(self.page4)  # index 3
        self.stacked_widget.addWidget(self.page5)  # index 4

        # Set default page
        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.stacked_widget)

        # Create Menu Bar for navigation
        self.create_menus()

        # Create Toolbar for quick navigation
        self.create_toolbar()

    # ====== PAGE 1: Basic Window Elements ======
    def create_basic_page(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Label
        label = QLabel("This is a QLabel (used to show text)")
        label.setAlignment(Qt.AlignCenter)

        # Button
        button = QPushButton("Click Me")
        button.clicked.connect(lambda: label.setText("Button Clicked!"))

        # Input Field
        input_field = QLineEdit()
        input_field.setPlaceholderText("Type something here...")

        # Multi-line Text Field
        text_area = QTextEdit()
        text_area.setPlaceholderText("Enter multiple lines of text...")

        layout.addWidget(label)
        layout.addWidget(button)
        layout.addWidget(input_field)
        layout.addWidget(text_area)

        return widget

    # ====== PAGE 2: Layouts (HBox, VBox, Grid) ======
    def create_layouts_page(self):
        widget = QWidget()
        grid = QGridLayout(widget)

        # Create labels and inputs in a grid form
        grid.addWidget(QLabel("Name:"), 0, 0)
        grid.addWidget(QLineEdit(), 0, 1)

        grid.addWidget(QLabel("Email:"), 1, 0)
        grid.addWidget(QLineEdit(), 1, 1)

        grid.addWidget(QLabel("Message:"), 2, 0)
        grid.addWidget(QTextEdit(), 2, 1)

        return widget

    # ====== PAGE 3: Table Example ======
    def create_table_page(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Create a Table with 3 rows and 3 columns
        table = QTableWidget(3, 3)
        table.setHorizontalHeaderLabels(["ID", "Name", "Course"])

        # Insert sample data
        table.setItem(0, 0, QTableWidgetItem("1"))
        table.setItem(0, 1, QTableWidgetItem("Alice"))
        table.setItem(0, 2, QTableWidgetItem("Python"))

        table.setItem(1, 0, QTableWidgetItem("2"))
        table.setItem(1, 1, QTableWidgetItem("Bob"))
        table.setItem(1, 2, QTableWidgetItem("Java"))

        table.setItem(2, 0, QTableWidgetItem("3"))
        table.setItem(2, 1, QTableWidgetItem("Charlie"))
        table.setItem(2, 2, QTableWidgetItem("C++"))

        layout.addWidget(table)
        return widget

    # ====== PAGE 4: Tabs Example ======
    def create_tabs_page(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Create Tabs
        tabs = QTabWidget()

        # Tab 1
        tab1 = QWidget()
        tab1_layout = QVBoxLayout(tab1)
        tab1_layout.addWidget(QLabel("This is Tab 1"))

        # Tab 2
        tab2 = QWidget()
        tab2_layout = QVBoxLayout(tab2)
        tab2_layout.addWidget(QLabel("This is Tab 2"))

        # Add tabs
        tabs.addTab(tab1, "Tab 1")
        tabs.addTab(tab2, "Tab 2")

        layout.addWidget(tabs)
        return widget

    # ====== PAGE 5: Styling with QSS (CSS-like) ======
    def create_styling_page(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Styled Button
        styled_button = QPushButton("Hover Me")
        styled_button.setStyleSheet("""
            QPushButton {
                background-color: #87CEEB;  /* Sky Blue */
                color: black;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #4682B4; /* Darker Blue */
                color: white;
            }
        """)

        layout.addWidget(QLabel("This page demonstrates QSS Styling"))
        layout.addWidget(styled_button)

        return widget

    # ====== MENU BAR ======
    def create_menus(self):
        menubar = QMenuBar(self)

        # Create Menu
        menu = menubar.addMenu("Navigate")

        # Add actions
        menu.addAction("Basic", lambda: self.stacked_widget.setCurrentIndex(0))
        menu.addAction("Layouts", lambda: self.stacked_widget.setCurrentIndex(1))
        menu.addAction("Table", lambda: self.stacked_widget.setCurrentIndex(2))
        menu.addAction("Tabs", lambda: self.stacked_widget.setCurrentIndex(3))
        menu.addAction("Styling", lambda: self.stacked_widget.setCurrentIndex(4))

        self.setMenuBar(menubar)

    # ====== TOOLBAR ======
    def create_toolbar(self):
        toolbar = QToolBar("Main Toolbar")

        # Add navigation actions
        action_basic = QAction("Basic", self)
        action_basic.triggered.connect(lambda: self.stacked_widget.setCurrentIndex(0))

        action_layouts = QAction("Layouts", self)
        action_layouts.triggered.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        action_table = QAction("Table", self)
        action_table.triggered.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        action_tabs = QAction("Tabs", self)
        action_tabs.triggered.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        action_styling = QAction("Styling", self)
        action_styling.triggered.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Add actions to toolbar
        toolbar.addAction(action_basic)
        toolbar.addAction(action_layouts)
        toolbar.addAction(action_table)
        toolbar.addAction(action_tabs)
        toolbar.addAction(action_styling)

        self.addToolBar(toolbar)


# Run the Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotesApp()
    window.show()
    sys.exit(app.exec())
