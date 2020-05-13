import sys
from PySide2 import QtWidgets, QtGui, QtCore
from workspace_widget import WorkspaceWidget
from fileHandlerFactory import FileHandlerFactory
import os


if __name__ == "__main__":

    def file_clicked(index):
        # print(file_system_model.filePath(index))
        index = tree_view.currentIndex()
        file_clicked_param = os.path.basename(
            file_system_model.filePath(index))
        tip_baze_podataka = ""
        if "sequential" in file_clicked_param:
            tip_baze_podataka = "sequential"
        if "serial" in file_clicked_param:
            tip_baze_podataka = "serial"

        splitovan_metapath = file_clicked_param.split(
            "_")[0] + "_metadata.json"

        file_handler = FileHandlerFactory.check_file(
            tip_baze_podataka, file_clicked_param, splitovan_metapath)
        central_widget = QtWidgets.QTabWidget(main_window)
        #text_edit = QtWidgets.QTextEdit(central_widget)
        #central_widget.addTab(text_edit, QtGui.QIcon("icons8-edit-file-64.png"), "Tekstualni editor")
        workspace = WorkspaceWidget(central_widget, file_handler)
        central_widget.addTab(workspace, QtGui.QIcon(
            "icons8-edit-file-64.png"), "Prikaz tabele")
        central_widget.setTabsClosable(True)
        main_window.setCentralWidget(central_widget)

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.resize(640, 480)
    main_window.setWindowTitle("Editor generickih podataka")
    main_window.setWindowIcon(QtGui.QIcon("icons8-edit-file-64.png"))

    menu_bar = QtWidgets.QMenuBar(main_window)
    file_menu = QtWidgets.QMenu("File", menu_bar)
    edit_menu = QtWidgets.QMenu("Edit", menu_bar)
    view_menu = QtWidgets.QMenu("View", menu_bar)
    help_menu = QtWidgets.QMenu("Help", menu_bar)

    menu_bar.addMenu(file_menu)
    menu_bar.addMenu(edit_menu)
    menu_bar.addMenu(view_menu)
    menu_bar.addMenu(help_menu)

    tool_bar = QtWidgets.QToolBar(main_window)

    structure_dock = QtWidgets.QDockWidget("File Explorer", main_window)

    file_system_model = QtWidgets.QFileSystemModel()
    file_system_model.setRootPath(QtCore.QDir.currentPath())

    tree_view = QtWidgets.QTreeView()
    tree_view.setModel(file_system_model)

    tree_view.setRootIndex(file_system_model.index(QtCore.QDir.currentPath()))

    structure_dock.setWidget(tree_view)

    toggle_structure_dock_action = structure_dock.toggleViewAction()
    view_menu.addAction(toggle_structure_dock_action)

    # tree_view.clicked.connect(file_clicked)

    status_bar = QtWidgets.QStatusBar(main_window)
    # varijabla u koju cuvamo putanju kliknutog fajla
    # onClick

    # def dummy(item):
    #     index = tree_view.currentIndex()
    #     file_clicked_param = file_system_model.filePath(index)
    #     print(file_clicked_param)
    #     status_bar.showMessage(file_system_model.filePath(index), 3000)
    #     return file_clicked_param

    # na klik nekog elementa u tree viewu se uzima index i pokazuje njegova putanja u status baru.
    tree_view.clicked.connect(file_clicked)

    main_window.setMenuBar(menu_bar)
    main_window.addToolBar(tool_bar)
    main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, structure_dock)

    main_window.setStatusBar(status_bar)
    main_window.show()
    # menu_bar.setParent(main_window)
    sys.exit(app.exec_())
