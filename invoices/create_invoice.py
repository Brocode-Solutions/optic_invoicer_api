from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from django.http import HttpResponse
from .create_invoice_pdf_helpers import draw_footer,draw_header,draw_invoice_info,draw_tearaway_section,draw_table_generator, create_custom_grid, hex_to_rgb


def create_invoice_pdf(filename, invoice, tear_away=True,only_tear_away=False):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    table_width = width - 100
    row_height = 20
    x_position=width
    y_position=height-50

    # Add blue border
    line_hex_color_code = '#3699ff'
    fill_hex_color_code = '#f5fdff'
    c.setStrokeColorRGB(*hex_to_rgb(line_hex_color_code))  # Set stroke color to blue
    c.setFillColorRGB(*hex_to_rgb(fill_hex_color_code))
    c.setLineWidth(10)  # Set line width
    c.rect(0, 0, width, height, stroke=1, fill=1)  # Draw rectangle border

    # Add logos
    logo_path_left = "organization_logos/logo_round_png.png"  # Update this with the path to your left logo file
    logo_path_right = "organization_logos/optic_invoicer_icon2.png"  # Update this with the path to your right logo file
    c.drawImage(logo_path_left, 10, height - 60, width=50, height=50)  # Draw left logo
    c.drawImage(logo_path_right, width - 90, height - 60, width=50, height=50)  # Draw right logo


      # Set line width
    c.setFillColorRGB(0,0,0)
    c.setStrokeColorRGB(0,0,0)
    draw_header(c,x_position,y_position, invoice)
    draw_invoice_info(c, height, invoice)
    
    # Prescription Section
    prescription_y_position = height - 200
    prescription_x_position = 60
    prescription_headers = ["", "SPH", "CYL", "AXIS", "PRISM", "ADD", "IPD."]
    prescription_data = [
        ("R", 
         str(invoice.prescription.right_sphere), 
         str(invoice.prescription.right_cylinder), 
         str(invoice.prescription.right_prism), 
         str(invoice.prescription.right_prism), 
         str(invoice.prescription.right_add), 
         str(invoice.prescription.right_ipd)),
                         
                         ("L", 
                          str(invoice.prescription.left_sphere), 
         str(invoice.prescription.left_cylinder), 
         str(invoice.prescription.left_axis), 
         str(invoice.prescription.left_prism), 
         str(invoice.prescription.left_add), 
         str(invoice.prescription.left_ipd)
                          )]
    next_table_y_position = draw_table_generator(c, 7, prescription_headers, prescription_x_position, prescription_y_position, row_height, table_width, prescription_data, "Prescription")

    # Frame Section
    frame_table_y_position = next_table_y_position
    frame_table_header = ["SKU", "Item", "Description", "Price"]
    frame_table_x_position = 60
    frame_table_data = [(item.SKU, item.name, item.description, str(item.sale_value)) for item in invoice.items.all() if item.item_type == "Frames"]
    next_table_y_position = draw_table_generator(c, 4, frame_table_header, frame_table_x_position, frame_table_y_position, row_height, table_width, frame_table_data, "Frames / SG")

    # Lens Section
    lens_table_y_position = next_table_y_position
    lens_table_header = ["S.no", "Item", "Description", "Price"]
    lens_table_x_position = 60
    lens_table_data =[(item.SKU, item.name, item.description, str(item.sale_value)) for item in invoice.items.all() if item.item_type == "Lens"]
    next_table_y_position = draw_table_generator(c, 4, lens_table_header, lens_table_x_position, lens_table_y_position, row_height, table_width, lens_table_data, "Lens")

    # Payment Section
    remarks_data = {"Remarks": invoice.remarks, "Total": invoice.total, "Advance": invoice.advance}
    grid_structure = [
        [('Remarks', 2, 3), ('Total', 2, 1), ('Advance', 2, 1)]
    ]
    next_table_y_position = create_custom_grid(c,grid_structure, 60, next_table_y_position, row_height, 100, remarks_data)

    # Delivery Section
    delivery_data = {"Delivery Date": invoice.delivery_date, "Balance": invoice.balance}
    grid_structure = [
        [('Delivery Date', 2, 4), ('Balance', 2, 1)]
    ]
    next_table_y_position = create_custom_grid(c,grid_structure, 60, next_table_y_position-30, row_height, 100, delivery_data)

    if (tear_away == True):
        c.setStrokeColorRGB(*hex_to_rgb(line_hex_color_code)) 
        print(tear_away)
        # Tear-away section
        tearaway_data = {
            'Invoice No': invoice.invoice_number,
            'Delivery Date': invoice.delivery_date,
            'Balance': invoice.balance,
        }
        next_table_y_position = draw_tearaway_section(c,invoice, 60,x_position, next_table_y_position -60, row_height, table_width, tearaway_data)

    # Footer
    draw_footer(c, width, invoice)

    c.showPage()
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=invoice.pdf'
    response.write(pdf)
    return response