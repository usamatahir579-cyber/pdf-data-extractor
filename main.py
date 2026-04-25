import PyPDF2


def extract_pdf(input_file, output_file):
    with open(input_file, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:   
                text += extracted

    with open(output_file, "w", encoding="utf-8") as out:
        out.write(text)

    print("Extraction complete!")


extract_pdf("sample.pdf", "output.txt")
