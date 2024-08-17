from project_logic import *


def main():
    """
    Function that starts the program logic and GUI
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
