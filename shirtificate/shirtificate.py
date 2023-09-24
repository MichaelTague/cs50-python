from fpdf import FPDF

def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    pdf.cell(txt="Michael Tague", x=30, y=100)
    pdf.image("shirtificate.png", x=10, y=30, w=190)
    pdf.output("shirtificate.pdf")

name = input("Name: ")
print(name)

if __name__ == "__main__":
    main()