from pdfquery import PDFQuery

pdf = PDFQuery('static/example.pdf')
pdf.load()

text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]

#print(text)

