import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QListWidget, QVBoxLayout, QMessageBox
import shutil
from documents_processor import make_file

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Предобработчик документов'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.vbox = QVBoxLayout(self)
        template_button = QPushButton('Загрузить шаблон', self)
        template_button.clicked.connect(self.save_template)
        self.vbox.addWidget(template_button)

        prepare_docs_button = QPushButton('Сформировать документы', self)
        prepare_docs_button.clicked.connect(self.prepare_docs)
        self.vbox.addWidget(prepare_docs_button)

        self.reload_templates_list(False)

        self.show()

    def reload_templates_list(self, delete_needs=True):
        if delete_needs:
            self.vbox.removeWidget(self.list_widget)

        self.list_widget = QListWidget()
        for number, filename in enumerate(os.listdir('templates')):
            self.list_widget.addItem(filename)
        self.list_widget.itemDoubleClicked.connect(self.delete_template)
        self.vbox.addWidget(self.list_widget)

    def delete_template(self, file):
        filename = file.text()
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setText(f"Удалить шаблон: {filename}")
        message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = message_box.exec()
        if returnValue == QMessageBox.Ok:
            os.remove(f'templates/{filename}')

    def save_template(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self, "Загрузите шаблон", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if filename:
            with open(f'templates/{os.path.basename(filename)}', 'wb') as write_file:
                with open(filename, 'rb') as read_file:
                    write_file.write(read_file.read())
        self.reload_templates_list()


    def prepare_docs(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self, "Загрузите эПТС", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if filename:
            dir_name = os.path.dirname(filename)
            evl_filename = f'evls/{os.path.basename(filename)}'
            with open(evl_filename, 'wb') as write_file:
                with open(filename, 'rb') as read_file:
                    write_file.write(read_file.read())

            for template_filename in os.listdir('templates'):
                vin = make_file(evl_filename, f'templates/{template_filename}')
            shutil.make_archive(f'{dir_name}/docs_archive_{os.path.basename(filename).split(".")[0]}_{vin}', 'zip', 'ready')

            for ready_filename in os.listdir('ready'):
                os.remove(f'ready/{ready_filename}')
            os.remove(evl_filename)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
