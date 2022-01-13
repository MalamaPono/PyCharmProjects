
# Generating PDFs with ReportLab module

# We can create a title, some text in paragraphs, and some charts and images. For that, we're going to use what
# reportlab calls Flowables. Flowables are sort of like chunks of a document that reportlab can arrange
# to make a complete report. Let's import some Flowable classes.

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

report = SimpleDocTemplate("report.pdf")

# Each of these items (Paragraph, Spacer, Table, and Image) are classes that build individual elements in the final
# document. We have to tell reportlab what style we want each part of the document to have, so let's import some more
# things from the module to describe style. Styles are similar to html tags like h1 and so on.
styles = getSampleStyleSheet()

report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

# convert fruit dictionary to list of lists aka 2D array so we can insert as chart in PDF
table_data = []
for k,v in fruit.items():
  table_data.append([k,v])

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

report_pie = Pie(width=6, height=6)

# to add data into a pie chart for ReportLab, we must have 2 different list data sets.
# One for the actual values in the pie chart, and one for the labels of each of those values
report_pie.labels = sorted(list(fruit.keys()))
# labels attribute of a pie chart
report_pie.data = sorted(list(fruit.values()))
# data attribute of a pie chart


# The Pie object isn’t Flowable, but it can be placed inside of a Flowable Drawing.
report_chart = Drawing()
report_chart.add(report_pie)

# Let's take a look at what this will look like. We can build the PDF now by using the build() method of our report.
# It takes a list of Flowable elements, and generates a PDF with them.
report.build([report_title, report_table, report_chart])