import pygal  # First import pygal
import subprocess
# class Graphy_display:


class Bar_chart(pygal.Bar):

    def __init__(self):
        pygal.Bar.__init__(self)

    def show_in_chrome(self, svg_file):
        subprocess.call(
            ["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", svg_file])


# bar_chart.title = 'Browser usage in February 2012 (in %)'
# bar_chart = pygal.Bar()  # Then create a bar graph object
# bar_chart.add('Fibonacci',
#               [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values
# bar_chart.x_labels = map(str, range(2002, 2013))
# bar_chart.render_to_file('bar_chart.svg')  # Save the svg to a file
# subprocess.call(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "bar_chart.svg"])
