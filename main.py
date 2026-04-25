import PyPDF2


def extract_pdf(input_file, output_file):
    try:
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

    except FileNotFoundError:
        print("Error: PDF file not found.")

    except Exception as e:
        print("Something went wrong:", e)


extract_pdf("sample.pdf", "output.txt")
