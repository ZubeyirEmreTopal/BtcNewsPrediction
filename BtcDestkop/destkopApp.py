from duzenle import Binary
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit,QLabel,QDesktopWidget,QMainWindow
from PyQt5 import QtWidgets, QtGui,QtCore
import joblib

model=joblib.load("104_model_63.pkl")
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.bn=Binary()

    def initUI(self):
        #self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle('BTC-HBRTR')
        # Creating the widgets
        self.edit_input = QTextEdit(self)  # use a QTextEdit element instead of a QLineEdit element
        self.edit_input.resize(500, 200)
        self.edit_input.move(50, 10)
        self.edit_input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)  # enable the vertical scroll bar
        self.btn_predict = QPushButton('Predict', self)
        self.btn_predict.move(250, 240)
        self.btn_predict.clicked.connect(self.on_predict_clicked)
        self.text_output = QTextEdit(self)
        self.text_output.move(50, 240+40)  # move the text edit down by the height of the button
        self.text_output.resize(500, 20)
        # Setting the style sheet for the space theme
        self.setStyleSheet("""
QWidget {
    background-color: black;
    color: white;
}

QPushButton {
    background-color: darkblue;
    color: white;
    border: none;
    font-size: 16px;
    border-radius: 5px; /* adds rounded corners to the button */
    padding: 10px 20px; /* adds padding to the button */
    transition: background-color 0.2s; /* adds a smooth transition effect when hovering over the button */
    min-width: 80px; /* sets a minimum width for the button */
    text-align: center; /* centers the button text */
    font-weight: bold; /* makes the button text bold */
}

QPushButton:hover {
    background-color: blue;
    cursor: pointer; /* changes the cursor to a hand when hovering over the button */
}

QPushButton:pressed {
    background-color: lightblue;
    box-shadow: inset 0 0 10px #333; /* adds a pressed effect to the button */
}
"""
        )

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_predict_clicked(self):
        input_text = self.edit_input.toPlainText()
        # Burada eğitilmiş metin işleme modelini kullanarak tahmin yapın
        duzenle=self.bn.kok_temizlik(input_text)
        predict=model.predict([duzenle])
        if predict == 1:    
            self.text_output.setText("artar")
        else:
            self.text_output.setText("azalır")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
