# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QFileDialog


class Controller2:
    def __init__(self, ui):
        super().__init__()
        self.ui = ui


    def handle_upload_button_click(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(None, "選擇 CSV 文件", "", "CSV Files (*.csv);;All Files (*)", options=options)

        if file_path:
            self.ui.csv_path.setText(f"已選擇檔案：{file_path}")


