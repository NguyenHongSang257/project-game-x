import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox

class YesNoApp(QMainWindow):

    def __init__(self):

        super().__init__()


        # Set the window properties (title and initial size)
        self.setWindowTitle("Pushbutton widgets (Yes or No)?")
        self.setGeometry(100, 100, 400, 400) # (x, y, width, height)

       
        # Create a central widget for the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        yes_button = QPushButton("Bắt đầu game ")
        no_button = QPushButton("Kết thúc game")
        
        yes_button.clicked.connect(self.show_yes_message)
        no_button.clicked.connect(self.show_no_message)
        
        layout = QVBoxLayout()
        layout.addWidget(yes_button)
        layout.addWidget(no_button)
        
        central_widget.setLayout(layout)
        
    def show_yes_message(self):
        QMessageBox().information(self, "Choice", "You chose 'Yes'.")
        
    def show_no_message(self):
         QMessageBox().information(self, "Choice", "You chose 'No'.")


     

        




def main():
    app = QApplication(sys.argv)
    window = YesNoApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":

    main()
