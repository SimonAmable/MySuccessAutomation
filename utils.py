import docx
from docx import Document
import re

# import fitz  # This is PyMuPDF
import pymupdf4llm


# custom imports
# Credit for add_hyperlink & get_or_create_hyperlink_style : https://stackoverflow.com/questions/47666642/adding-an-hyperlink-in-msword-by-using-python-docx
# from configs import load_config

def add_hyperlink(paragraph, text, url):
    # This gets access to the document.xml.rels file and gets a new relation id value
    part = paragraph.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)

    # Create the w:hyperlink tag and add needed values
    hyperlink = docx.oxml.shared.OxmlElement('w:hyperlink')
    hyperlink.set(docx.oxml.shared.qn('r:id'), r_id, )

    # Create a new run object (a wrapper over a 'w:r' element)
    new_run = docx.text.run.Run(
        docx.oxml.shared.OxmlElement('w:r'), paragraph)
    new_run.text = text

    # Set the run's style to the builtin hyperlink style, defining it if necessary
    new_run.style = get_or_create_hyperlink_style(part.document)
    # Alternatively, set the run's formatting explicitly
    # new_run.font.color.rgb = docx.shared.RGBColor(0, 0, 255)
    # new_run.font.underline = True

    # Join all the xml elements together
    hyperlink.append(new_run._element)
    paragraph._p.append(hyperlink)
    return hyperlink


def get_or_create_hyperlink_style(d):
    """If this document had no hyperlinks so far, the builtin
       Hyperlink style will likely be missing and we need to add it.
       There's no predefined value, different Word versions
       define it differently.
       This version is how Word 2019 defines it in the
       default theme, excluding a theme reference.
    """
    if "Hyperlink" not in d.styles:
        if "Default Character Font" not in d.styles:
            ds = d.styles.add_style("Default Character Font",
                                    docx.enum.style.WD_STYLE_TYPE.CHARACTER,
                                    True)
            ds.element.set(docx.oxml.shared.qn('w:default'), "1")
            ds.priority = 1
            ds.hidden = True
            ds.unhide_when_used = True
            del ds
        hs = d.styles.add_style("Hyperlink",
                                docx.enum.style.WD_STYLE_TYPE.CHARACTER,
                                True)
        hs.base_style = d.styles["Default Character Font"]
        hs.unhide_when_used = True
        hs.font.color.rgb = docx.shared.RGBColor(0x05, 0x63, 0xC1)
        hs.font.underline = True
        del hs

    return "Hyperlink"

def JobToID(job_position: str) -> str:
    """Convert job position to a lowercase, alphanumeric ID."""
    return "".join(c.lower() for c in job_position if c.isalnum())




from langchain_community.document_loaders import PyPDFLoader

def get_document_text(file_path: str) -> str:
    """
    Extracts text from PDF or DOCX files.
    
    Parameters:
        file_path (str): Path to the PDF or DOCX file
        
    Returns:
        str: Combined text from the document
    """
    if file_path.lower().endswith('.pdf'):
        loader = PyPDFLoader(file_path)
    elif file_path.lower().endswith('.docx'):
        raise ValueError("Unsupported file format. Only PDF currently supported.")
    else:
        raise ValueError("Unsupported file format. Only PDF and DOCX are supported.")
    
    pages = loader.load()
    return ' '.join(page.page_content for page in pages)

# convert the document to markdown
# Write the text to some file in UTF8-encoding
# import pathlib
# pathlib.Path("output.md").write_bytes(md_text.encode())

# def get_document_text(file_path: str) -> str:
#     """
#     Converts PDF file to markdown format.
    
#     Parameters:
#         file_path (str): Path to the PDF file
        
#     Returns:
#         str: Markdown text from the document
#     """
#     if not file_path.lower().endswith('.pdf'):
#         raise ValueError("Unsupported file format. Only PDF is supported.")
    
#     md_text = pymupdf4llm.to_markdown(file_path)
#     md_text = md_text.encode('utf-8').decode('utf-8')
#     return md_text



#test the function
# document_path = "./data_folder/input/resume/resume.pdf"
# document_md = get_document_markdown(document_path)
# print(document_md)


