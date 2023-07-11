import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
print("Init modules")

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # create a QTabWidget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.showMaximized()
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        print("Creating widget")

        self.home_url = "https://www.google.com"

        # Create a new tab and set it as the current tab
        self.add_new_tab(self.home_url, "qStyle Home")
        print("Init new tab")

        # create a navigation toolbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        print("Creating toolbar")

        back_btn = QAction(QIcon('icons/qs_backward.png'),'', self)
        back_btn.triggered.connect(self.tabs.currentWidget().back)
        navbar.addAction(back_btn)

        forward_btn = QAction(QIcon('icons/qs_forward.png'),'', self)
        forward_btn.triggered.connect(self.tabs.currentWidget().forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(QIcon('icons/qs_reload.png'),'', self)
        reload_btn.triggered.connect(self.tabs.currentWidget().reload)
        navbar.addAction(reload_btn)

        home_btn = QAction(QIcon('icons/qs_home.png'),'', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        new_tab_btn = QAction(QIcon('icons/qs_adder.png'),'', self)
        new_tab_btn.triggered.connect(self.add_new_tab)
        navbar.addAction(new_tab_btn)

        # create a search bar
        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.search)
        navbar.addWidget(self.search_bar)
        print("Init search bar")

        # make the tabs closable
        self.tabs.setTabsClosable(True)

        # adding action when tab close is requested
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("Option 1")
        file.addAction("Option 2")
        file.addAction("Option 3")

        self.setWindowIcon(QIcon('logo.png'))

    def add_new_tab(self, url=None, title="New Tab"):
        browser = QWebEngineView()
        print("Starting WebEngine")

        # set url if given
        if url:
            browser.setUrl(QUrl(url))

        # create a new tab and set browser as its widget
        tab_index = self.tabs.addTab(browser, title)
        print("Setting new tab widget")

        # make the new tab the current tab
        self.tabs.setCurrentIndex(tab_index)

        # update the url bar
        browser.urlChanged.connect(self.update_url)
    
    def search(self):
        url = self.search_bar.text()
        current_tab = self.tabs.currentWidget()
        current_tab.setUrl(QUrl(f"https://google.com/search?q={url}"))


    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl(self.home_url))

    def update_url(self, q):
        self.search_bar.setText(q.toString())

    # when tab is closed
    def close_current_tab(self, i):
 
        # if there is only one tab
        if self.tabs.count() < 2:
            # do nothing
            return
 
        # else remove the tab
        self.tabs.removeTab(i)

    # method for updating the title
    def update_title(self, browser):
 
        # if signal is not from the current tab
        if browser != self.tabs.currentWidget():
            # do nothing
            return
 
        # get the page title
        title = self.tabs.currentWidget().page().title()
 
        # set the window title
        self.setWindowTitle("% s - qStyle" % title)

    


app = QApplication([])
# Force the style to be the same on all OSs:
app.setStyle("Fusion")
print("Init app style")

# Now use a palette to switch to dark colors:
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.black)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(palette)
QApplication.setApplicationName('qStyle')
window = MainWindow()
app.exec_()

