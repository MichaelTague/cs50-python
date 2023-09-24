from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    pdf.cell(txt="CS50 Shirtificate", center=True)
    pdf.cell(txt=name + "took CS50", center=True)
    pdf.image("shirtificate.png")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()