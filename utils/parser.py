import os
from pypdf import PdfReader

class parser_pdf:
    def __init__(self):
        self.destination = "data/resume_text"
        self.source = "data/resume_pdf"
    
    def parse(self, pdf_name: str):
        pdf_filepath = os.path.join(self.source,pdf_name)
        reader = PdfReader(pdf_filepath)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        os.makedirs(self.destination, exist_ok=True)
        txt_filename = pdf_name.replace(".pdf", ".txt")
        txt_filepath = os.path.join(self.destination, txt_filename)
        with open(txt_filepath,"w", encoding='utf-8') as file:
            file.write(text)
        print("Text file created")

if __name__ == "__main__":
    parser = parser_pdf()
    parser.parse("krishna_resume.pdf")