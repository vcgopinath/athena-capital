from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

def create_capability_statement():
    output_path = "/Users/Nila/Desktop/cm-mcp-server/website/capability-statement.pdf"
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter  # 612 x 792

    # Colors
    navy = HexColor("#1a1a2e")
    gold = HexColor("#c9a84c")
    dark_gray = HexColor("#2d2d2d")
    medium_gray = HexColor("#555555")
    light_bg = HexColor("#f5f5f0")
    white = HexColor("#ffffff")

    margin = 40
    content_width = width - 2 * margin

    # === TOP HEADER BAR ===
    c.setFillColor(navy)
    c.rect(0, height - 100, width, 100, fill=True, stroke=False)

    # Company name
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(margin, height - 45, "ATHENA CAPITAL PARTNERS LLC")

    # Gold accent line
    c.setStrokeColor(gold)
    c.setLineWidth(2)
    c.line(margin, height - 55, margin + 280, height - 55)

    # Tagline
    c.setFont("Helvetica", 10)
    c.setFillColor(HexColor("#cccccc"))
    c.drawString(margin, height - 72, "Professional Business Services for Government Agencies")

    # WOSB badge area (right side of header)
    c.setFillColor(gold)
    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(width - margin, height - 40, "WOMAN-OWNED SMALL BUSINESS")
    c.setFont("Helvetica", 8)
    c.setFillColor(white)
    c.drawRightString(width - margin, height - 53, "NAICS 541611 | 459540")
    c.drawRightString(width - margin, height - 65, "UEI: F1VPSS7P7DM6")
    c.drawRightString(width - margin, height - 77, "SAM.gov Registered | Las Vegas, NV")

    # === CAPABILITY STATEMENT TITLE ===
    y = height - 125
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width / 2, y, "CAPABILITY STATEMENT")

    # Gold line under title
    c.setStrokeColor(gold)
    c.setLineWidth(1.5)
    c.line(margin, y - 8, width - margin, y - 8)

    # === ABOUT US SECTION ===
    y = y - 30
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(margin, y, "ABOUT US")

    # Gold underline
    c.setStrokeColor(gold)
    c.setLineWidth(1)
    c.line(margin, y - 3, margin + 65, y - 3)

    y -= 18
    c.setFillColor(dark_gray)
    c.setFont("Helvetica", 9)
    about_text = (
        "Athena Capital Partners LLC is a Woman-Owned Small Business (WOSB) based in Las Vegas, Nevada, "
        "delivering reliable, high-quality professional services to federal agencies through streamlined "
        "micro-purchase and contract vehicles. We specialize in administrative support, creative services, "
        "and supply procurement, enabling government teams to focus on their core mission."
    )
    # Use Paragraph for text wrapping
    style = ParagraphStyle('about', fontName='Helvetica', fontSize=9, leading=12,
                           textColor=dark_gray)
    p = Paragraph(about_text, style)
    pw, ph = p.wrap(content_width, 100)
    p.drawOn(c, margin, y - ph)
    y = y - ph - 15

    # === TWO COLUMN LAYOUT ===
    col1_x = margin
    col2_x = width / 2 + 10
    col_width = content_width / 2 - 10

    # === LEFT COLUMN: CORE COMPETENCIES ===
    left_y = y

    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(col1_x, left_y, "CORE COMPETENCIES")
    c.setStrokeColor(gold)
    c.line(col1_x, left_y - 3, col1_x + 140, left_y - 3)

    left_y -= 20

    competencies = [
        ("Administrative Support", "Virtual assistants, data entry, scheduling,\ndocument management"),
        ("Writing, Editing & Translation", "Technical writing, proofreading,\nmultilingual translation services"),
        ("Graphic Design & Printing", "Branding, marketing collateral,\nlarge-format printing"),
        ("IT Accessories & Office Supplies", "Bulk ordering, procurement,\ndelivery coordination"),
        ("Photography Services", "Event photography, headshots,\nvideo production & editing"),
        ("Breakroom & Facility Supplies", "Procurement and delivery of\nbreakroom and facility items"),
    ]

    for title, desc in competencies:
        # Gold bullet
        c.setFillColor(gold)
        c.circle(col1_x + 5, left_y - 2, 3, fill=True, stroke=False)

        # Title
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(col1_x + 14, left_y, title)

        # Description
        left_y -= 12
        c.setFillColor(medium_gray)
        c.setFont("Helvetica", 7.5)
        for line in desc.split('\n'):
            c.drawString(col1_x + 14, left_y, line)
            left_y -= 10
        left_y -= 8

    # === RIGHT COLUMN ===
    right_y = y

    # DIFFERENTIATORS
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(col2_x, right_y, "DIFFERENTIATORS")
    c.setStrokeColor(gold)
    c.line(col2_x, right_y - 3, col2_x + 120, right_y - 3)

    right_y -= 20

    # Differentiator box
    box_height = 130
    c.setFillColor(light_bg)
    c.roundRect(col2_x, right_y - box_height + 10, col_width, box_height, 5, fill=True, stroke=False)

    differentiators = [
        "Woman-Owned Small Business (WOSB)",
        "SAM.gov Registered | UEI: F1VPSS7P7DM6",
        "CAGE Code: 1NGH5",
        "Micro-Purchase & GPC Ready",
        "FAR Compliant Operations",
        "24-Hour Quote Turnaround",
    ]

    diff_y = right_y - 5
    for diff in differentiators:
        c.setFillColor(gold)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(col2_x + 10, diff_y, "\u2713")
        c.setFillColor(dark_gray)
        c.setFont("Helvetica", 8.5)
        c.drawString(col2_x + 25, diff_y, diff)
        diff_y -= 18

    right_y = diff_y - 15

    # NAICS / CODES
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(col2_x, right_y, "NAICS CODES")
    c.setStrokeColor(gold)
    c.line(col2_x, right_y - 3, col2_x + 95, right_y - 3)

    right_y -= 18
    c.setFillColor(dark_gray)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(col2_x, right_y, "541611")
    c.setFont("Helvetica", 8)
    c.drawString(col2_x + 45, right_y, "Administrative Management &")
    right_y -= 12
    c.drawString(col2_x + 45, right_y, "General Management Consulting")

    right_y -= 18
    c.setFillColor(dark_gray)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(col2_x, right_y, "459540")
    c.setFont("Helvetica", 8)
    c.drawString(col2_x + 45, right_y, "Office Supplies &")
    right_y -= 12
    c.drawString(col2_x + 45, right_y, "Stationery Retailers")

    right_y -= 20
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(col2_x, right_y, "PSC CODES")
    c.setStrokeColor(gold)
    c.line(col2_x, right_y - 3, col2_x + 75, right_y - 3)

    right_y -= 18
    psc_codes = [
        ("7510", "Office Supplies"),
        ("R706", "Administrative Support Services"),
        ("R410", "Technical Writing"),
        ("R412", "Translation & Interpreting"),
    ]
    for code, desc in psc_codes:
        c.setFillColor(dark_gray)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(col2_x, right_y, code)
        c.setFont("Helvetica", 8)
        c.drawString(col2_x + 42, right_y, desc)
        right_y -= 14

    right_y -= 10

    # PAST PERFORMANCE
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(col2_x, right_y, "PAST PERFORMANCE")
    c.setStrokeColor(gold)
    c.line(col2_x, right_y - 3, col2_x + 135, right_y - 3)

    right_y -= 18
    c.setFillColor(medium_gray)
    c.setFont("Helvetica", 8.5)
    c.drawString(col2_x, right_y, "Available upon request.")
    right_y -= 12
    c.drawString(col2_x, right_y, "Contact us for project references")
    c.drawString(col2_x, right_y - 12, "and detailed case studies.")

    # === BOTTOM CONTACT BAR ===
    bar_height = 50
    c.setFillColor(navy)
    c.rect(0, 0, width, bar_height, fill=True, stroke=False)

    # Gold accent line at top of bar
    c.setStrokeColor(gold)
    c.setLineWidth(2)
    c.line(0, bar_height, width, bar_height)

    # Contact info
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 8)

    # Website
    c.drawString(margin, 28, "WEB")
    c.setFont("Helvetica", 8)
    c.drawString(margin, 14, "athenacapitalnv.com")

    # Email
    c.setFont("Helvetica-Bold", 8)
    c.drawString(margin + 140, 28, "EMAIL")
    c.setFont("Helvetica", 8)
    c.drawString(margin + 140, 14, "janani@athenacapitalnv.com")

    # Phone
    c.setFont("Helvetica-Bold", 8)
    c.drawString(margin + 310, 28, "PHONE")
    c.setFont("Helvetica", 8)
    c.drawString(margin + 310, 14, "(702) 301-9535")

    # Location
    c.setFont("Helvetica-Bold", 8)
    c.drawString(margin + 440, 28, "LOCATION")
    c.setFont("Helvetica", 8)
    c.drawString(margin + 440, 14, "Las Vegas, Nevada")

    c.save()
    print(f"PDF created: {output_path}")

create_capability_statement()
