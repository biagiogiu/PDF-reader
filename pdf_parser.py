from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from io import StringIO
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter


class MyParser(object):
    def __init__(self, pdf):
        """The pdf file is read and parsed. Every line of the pdf
        is stored in a list. The lines are then merged together
        inti paragraphs considering their lenght and the final
        punctuation"""
        parser = PDFParser(open(pdf, 'rb'))
        document = PDFDocument(parser)
        # Try to parse the document
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed
        # Create a PDF resource manager object
        # that stores shared resources.
        rsrcmgr = PDFResourceManager()
        # Create a buffer for the parsed text
        retstr = StringIO()
        # Spacing parameters for parsing
        laparams = LAParams()
        codec = 'utf-8'

        # Create a PDF device object
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        # Create a PDF interpreter object
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # Process each page contained in the document.
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)

        self.records = []
        self.current_line = ""

        lines = retstr.getvalue().splitlines()
        for line in lines:
            if len(line) > 95 and line[-1] not in [".", ":", "?", "!"]:
                self.current_line = " ".join([self.current_line, line])
            elif self.current_line != "":
                self.current_line = " ".join([self.current_line, line])
                self.records.append(self.current_line)
                self.current_line = ""
            elif line != "":
                self.records.append(line)
