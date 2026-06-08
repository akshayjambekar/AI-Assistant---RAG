from services.pdf_services import PDFService

text = PDFService.extract_text(r'D:\AI\ai_backend\app\utils\Akshay_Jambekar_Resume_ML_DE.pdf')

print(text[:2000])