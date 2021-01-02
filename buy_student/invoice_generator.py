from fpdf import FPDF
import webbrowser


def generate(orderid, total, c):
    pdf = FPDF(format='letter', unit='in')
    data = []
    f = open('loggedin.txt', 'r')
    email = f.readline()

    for item in c:
        f = [item.Item_id, item.Item_title, item.Item_price]
        data.append(f)
    pdf.add_page()

    pdf.set_font('Times', '', 10.0)

    epw = pdf.w - 2 * pdf.l_margin
    col_width = epw / 4

    pdf.set_font('Times', 'B', 14.0)
    pdf.cell(epw, 0.0, 'NIRVAAS', align='C')
    pdf.ln(0.5)
    pdf.set_font('Times', 'B', 14.0)
    pdf.cell(epw, 0.0, 'Invoice', align='C')
    pdf.ln(0.5)
    pdf.set_font('Times', 'B', 14.0)
    w = "Email ID : " + str(email)
    pdf.cell(epw, 0.0, w, align='C')
    pdf.ln(0.5)
    pdf.set_font('Times', 'B', 14.0)
    pdf.cell(epw, 0.0, 'ITEMS ORDERED', align='C')
    pdf.ln(0.5)
    pdf.set_font('Times', 'B', 14.0)
    pdf.cell(epw, 0.0, 'Order ID: ' + str(orderid), align='L')
    pdf.ln(0.5)
    pdf.set_font('Times', 'B', 14.0)
    pdf.ln(0.5)

    th = pdf.font_size

    for row in data:
        for datum in row:
            pdf.cell(col_width, th, str(datum), border=1, align='C')

        pdf.ln(th)

    pdf.ln(4 * th)
    pdf.set_font('Times', 'B', 14.0)
    pdf.cell(epw, 0.0, 'Order Total: ' + str(total), align='R')
    pdf.ln(0.5)
    pdf.set_font('Times', 'B', 14.0)
    pdf.cell(epw, 0.0, 'Payment by cash only', align='L')
    pdf.ln(0.5)

    name = 'Invoice_' + str(orderid) + '.pdf'
    pdf.output(name, 'F')
    webbrowser.open(name)
