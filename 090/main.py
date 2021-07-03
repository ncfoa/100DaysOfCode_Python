import pyttsx3
import PyPDF2

# Read the PDF file binary mode
pdf_file = open('./The-Complete-works-of-Nostradamus.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)
# Find the number of pages in the PDF document
number_of_pages = read_pdf.getNumPages()
# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
rate = engine.getProperty('rate')

engine.setProperty('rate', rate-50)
# Read from page 3 to the end of the PDF document
for i in range(3, number_of_pages):
    # Read the PDF page
    page = read_pdf.getPage(i)

    # Extract the text of the PDF page
    page_content = page.extractText()

    # say method on the engine that passing input text to be spoken
    engine.say(page_content)

    # run and wait method to processes the voice commands.
    engine.runAndWait()