from PyQt6.QtWidgets import *
from new_gui import *
import os
import csv


class Logic(QMainWindow, Ui_MainWindow):
    """
    Class that houses all logic for Gui
    """
    def __init__(self) -> None:
        """
        function that sets up the data retrieved from new_gui.py and creates header
        """
        super().__init__()
        self.setupUi(self)

        self.message_label.setVisible(False)

        self.count = 0

        if os.stat('project_data.csv').st_size == 0:
            with open('project_data.csv', 'a', newline='') as csv_file:
                header = csv.DictWriter(csv_file, fieldnames=['ID ', ' Voted ', ' Vote'])
                header.writeheader()

        self.submit_button.clicked.connect(lambda: self.submit())

    def submit(self) -> None:
        """
        Function that defines what happens when the "Submit" but is pressed
        """
        if self.count == 0:
            try:
                ID = self.ID_input.text().strip()
                ID = ID.replace(' ', '')
                assert int(ID)
                assert len(ID) > 0 and ID.isdigit()
                assert self.button_cass.isChecked() or self.button_jade.isChecked()

                ID = int(ID)
                assert 1000 < ID < 9999

                with open('project_data.csv', 'r') as read_csv:
                    reader = csv.reader(read_csv)
                    for row in reader:
                        assert str(ID) != row[0]

                if self.button_cass.isChecked():
                    vote = 'Cass'
                elif self.button_jade.isChecked():
                    vote = 'Jade'

                self.message_label.setVisible(True)
                self.message_label.setText('Thanks For Voting!')

                with open('project_data.csv', 'a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([ID, 'Voted', vote])

                self.count = 1

            except AssertionError:
                self.message_label.setVisible(True)
                self.message_label.setText('Please Enter a Valid ID or Candidate')

        else:
            self.message_label.setText('Already Voted')
