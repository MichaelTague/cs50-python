from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    pdf.image("shirtificate.png", x=0.5, y=60)

    pdf.set_font("Arial", size=50)
    pdf.set_y(25)
    pdf.cell(txt="CS50 Shirtificate", center=True)

    pdf.set_font("Arial", size=30)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(130)
    pdf.cell(txt=name + " took CS50", center=True)

    pdf.output("shirtificate.pdf")
    print("pdf.eph, pdf.epw:", pdf.eph, pdf.epw)

if __name__ == "__main__":
    main()