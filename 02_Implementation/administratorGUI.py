"""
this module offers the functionality to display statistics in a GUI.
All data will be displayed in a pie chart
"""

# python imports
from pylab import *

# project imports

def display_statistic(statistic, parameter, group):
    """
    displays statistic result data as piechart. this assumes that all input data
    is already validated.
    @params:
        statistic:
            the statistical data to display. should be in this format:
            {group: [average, total]}
    @return: -
    """

    figure(1, figsize=(7, 7))                     # define figure

    ax = axes([0.1, 0.1, 0.8, 0.8])

    groups = statistic.keys()                       # labels
    values = [statistic[a][1] for a in groups]
    ls = "{} total: {} average: {}"                 # raw label string
    labels = [ls.format(k, statistic[k][1], statistic[k][0]) for k in groups]
    [print(l, type(l)) for l in labels]
    print("groups:")
    print(groups)
    print("values:")
    print(values)

    pie(values, labels=labels, shadow=True, autopct="%1.2f%%", startangle=90)

    title_string = "Plotting {} grouped by {}".format(parameter, group)
    title(title_string, bbox={"facecolor":"0.8", "pad":5})

    show()