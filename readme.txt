# PDF Data Extractor

A simple Python project that extracts text from PDF files and saves it into a `.txt` file.

## Features

* Read PDF files using PyPDF2
* Extract text from all pages
* Save extracted text into output.txt
* Handles missing files and errors gracefully

## Technologies Used

* Python
* PyPDF2

## Installation

Install required library:

```bash
pip install PyPDF2
```

## How to Run

1. Place your PDF file in the project folder
2. Rename it as `sample.pdf`
3. Run:

```bash
python main.py
```

4. Extracted text will be saved in:

```text
output.txt
```

## Example

Input:

```text
sample.pdf
```

Output:

```text
output.txt
```

## Future Improvements

* Extract tables from PDFs
* Support multiple PDF files
* Build web version using Streamlit
* Add GUI version

## Author

Usama
