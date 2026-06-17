from pypdf import PdfReader
import logging

logger = logging.getLogger(__name__)

class PDFService:

    @staticmethod
    def extract_text(pdf_path: str) -> str:
        """
        Extract text from PDF.
        """
        try:

            logger.info(f"Reading PDF from {pdf_path}")

            reader = PdfReader(pdf_path)

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            logger.info(
                f"Successfully extracted {len(text)} characters"
            )

            return text

        except Exception as e:

            logger.error(
                f"extract_text failed: {str(e)}"
            )

            raise