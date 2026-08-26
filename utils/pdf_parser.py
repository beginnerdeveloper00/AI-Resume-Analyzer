import fitz


def extract_text_from_pdf(uploaded_file):
    """
    Extract text from an uploaded PDF resume.
    """

    try:
        pdf_document = fitz.open(
            stream=uploaded_file.read(),
            filetype="pdf"
        )

        text = ""

        for page in pdf_document:
            text += page.get_text()

        pdf_document.close()

        text = text.strip()

        if not text:
            raise ValueError(
                "No readable text found in the PDF. "
                "The resume may be scanned or image-based."
            )

        return text

    except Exception as error:
        raise ValueError(
            f"Unable to read the PDF file: {error}"
        )