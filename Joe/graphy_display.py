import pygal  
import subprocess


class Bar_chart(pygal.Bar):

    def __init__(self):
        pygal.Bar.__init__(self)

    def show_in_chrome(self, svg_file):
        subprocess.call(
            ["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", svg_file])

