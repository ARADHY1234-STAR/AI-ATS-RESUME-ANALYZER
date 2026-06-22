import io
import logging
from xhtml2pdf import pisa

logger = logging.getLogger('ats_resume_scorer')

def generate_combined_pdf(html_docs: dict[str, str]) -> bytes:
    """
    Combines multiple HTML strings into a single PDF using xhtml2pdf.
    Works on Windows without any system dependencies.
    """
    # Merge all HTML bodies into one document
    combined_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @page { margin: 1cm; }
            .page-break { page-break-before: always; }
            body { font-family: Arial, sans-serif; font-size: 12px; }
        </style>
    </head>
    <body>
    """
    
    html_list = list(html_docs.values())
    
    for i, html_str in enumerate(html_list):
        if i > 0:
            combined_html += '<div class="page-break"></div>'
        combined_html += html_str
    
    combined_html += "</body></html>"
    
    # Convert to PDF
    pdf_buffer = io.BytesIO()
    result = pisa.CreatePDF(
        src=combined_html,
        dest=pdf_buffer,
        encoding='utf-8'
    )
    
    if result.err:
        logger.error(f"PDF generation failed with {result.err} errors")
        raise RuntimeError(f"PDF generation failed: {result.err} errors encountered")
    
    pdf_bytes = pdf_buffer.getvalue()
    logger.info(f"PDF generated successfully: {len(pdf_bytes)} bytes")
    return pdf_bytes