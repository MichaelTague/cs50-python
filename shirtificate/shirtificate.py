from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    pdf.cell(txt="CS50 Shirtificate", center=True)
    pdf.cell(txt=name + "took CS50", center=True)
    pdf.image("shirtificate.png", x=0, y=60)
    pdf.output("shirtificate.pdf")
    print("pdf.eph, pdf.epw:", pdf.eph, pdf.epw)

if __name__ == "__main__":
    main()