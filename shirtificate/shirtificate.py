from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    pdf.cell(txt="CS50 Shirtificate", center=True)
    pdf.cell(txt="Michael Tague", center=True, new_y=100)
    pdf.image("shirtificate.png", center=True)
    pdf.output("shirtificate.pdf")

name = input("Name: ")
print(name)

if __name__ == "__main__":
    main()