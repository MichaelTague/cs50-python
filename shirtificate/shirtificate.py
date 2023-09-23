from fpdf import FPDF

def main():
    pdf = pdf()
    pdf.add_page()
    pdf_set_font("Arial", size=20)
    pdf.cell(100, 20, txt="Michael Tague", ln=True, align='C')
    pdf.image("shirtificate.png", x=10, y=30, w=190)
    pdf.output("shirtificate.pdf")

name = input("Name: ")
print(name)

if __name__ == "__main__":
    main()