#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(attatchment_path,title,paragraph):
    styles = getSampleStyleSheet()

    report = SimpleDocTemplate(attatchment_path)

    report_title = Paragraph(title, styles["h1"])

    report_info = Paragraph(paragraph, styles["BodyText"])

    report.build([report_title,report_info])