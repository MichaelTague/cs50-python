from fpdf import FPDF

def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    pdf.cell(txt="Michael Tague", new_x=100, new_y=20)
    pdf.image("shirtificate.png", x=10, y=30, w=190)
    pdf.output("shirtificate.pdf")

name = input("Name: ")
print(name)

if __name__ == "__main__":
    main()