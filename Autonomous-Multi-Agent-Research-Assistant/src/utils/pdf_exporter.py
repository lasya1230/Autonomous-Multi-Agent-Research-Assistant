import os
import textwrap
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def export_report_to_pdf(report_text: str, output_path: str = "data/outputs/research_report.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    y = height - 50

    c.setFont("Helvetica", 11)

    for line in report_text.split("\n"):
        wrapped_lines = textwrap.wrap(line, width=95) if line.strip() else [""]
        for wrapped_line in wrapped_lines:
            c.drawString(40, y, wrapped_line)
            y -= 18

            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 11)
                y = height - 50

    c.save()
    return output_path