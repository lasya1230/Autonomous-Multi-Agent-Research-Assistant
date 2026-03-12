from pathlib import Path
from pypdf import PdfReader


def load_text_file(file_path: str) -> str:
    """
    Load text from a .txt file.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return path.read_text(encoding="utf-8")


def load_pdf_file(file_path: str) -> str:
    """
    Load text from a .pdf file.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return text


def load_document(file_path: str) -> str:
    """
    Load text from a supported document type.
    Supported types: .txt, .pdf
    """
    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix == ".txt":
        return load_text_file(file_path)
    elif suffix == ".pdf":
        return load_pdf_file(file_path)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")