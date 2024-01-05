# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QFileDialog


class Controller2:
    def __init__(self, ui):
        super().__init__()
        self.ui = ui


    def handle_upload_button_click(self):
        options = QFileDialog.Options() # 配置文件對話框物件
        file_path, _ = QFileDialog.getOpenFileName(None, "選擇 CSV 文件", "", "CSV Files (*.csv);;All Files (*)", options=options)

        if file_path:
            self.ui.csv_path.setText(f"已選擇檔案：{file_path}")

#      def handle_combobox_changed(self, index):
#         # 取得所選擇的模型名稱
#         model_name = self.ui.comboBox.currentText()
        
# self.model_pages = {"Kmeans": 0, "模型2": 1, "模型3": 2}
        
        # self.ui.stackedWidget.setCurrentIndex(self.ui.model_pages[model_name])
        # # 切換到對應的頁面
        # if model_name == "Kmeans":
        #     self.ui.stackedWidget.setCurrentIndex(0)  # 顯示第一個頁面
        # elif model_name == "模型2":
        #     self.ui.stackedWidget.setCurrentIndex(1)  # 顯示第二個頁面，依此類推
        # elif model_name == "模型3":
        #     self.ui.stackedWidget.setCurrentIndex(2)  # 顯示第三個頁面，依此類推