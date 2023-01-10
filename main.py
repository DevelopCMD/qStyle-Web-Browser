import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # create a QTabWidget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.showMaximized()

        self.home_url = "https://you.com/"

        # Create a new tab and set it as the current tab
        self.add_new_tab(self.home_url, "Home")

        # create a navigation toolbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction(QIcon('back.svg'),'', self)
        back_btn.triggered.connect(self.tabs.currentWidget().back)
        navbar.addAction(back_btn)

        forward_btn = QAction(QIcon('forward.svg'),'', self)
        forward_btn.triggered.connect(self.tabs.currentWidget().forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(QIcon('reload.svg'),'', self)
        reload_btn.triggered.connect(self.tabs.currentWidget().reload)
        navbar.addAction(reload_btn)

        home_btn = QAction(QIcon('home.svg'),'', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        new_tab_btn = QAction(QIcon('add.svg'),'', self)
        new_tab_btn.triggered.connect(self.add_new_tab)
        navbar.addAction(new_tab_btn)

        # create a search bar
        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.search)
        navbar.addWidget(self.search_bar)


    def add_new_tab(self, url=None, title="blank"):
        browser = QWebEngineView()

        # set url if given
        if url:
            browser.setUrl(QUrl(url))

        # create a new tab and set browser as its widget
        tab_index = self.tabs.addTab(browser, title)

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

    


app = QApplication(sys.argv)
QApplication.setApplicationName('The Silly Surfer')
window = MainWindow()
app.exec_()

