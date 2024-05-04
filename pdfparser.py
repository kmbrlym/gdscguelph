from pdfquery import PDFQuery

pdfStudent = PDFQuery('static/examplestudentans.pdf')
pdfStudent.load()
text_elements1 = pdfStudent.pq('LTTextLineHorizontal')
studentAnswer = [t.text for t in text_elements1]

pdfMarkingScheme = PDFQuery('static/markingScheme.pdf')
pdfMarkingScheme.load()
text_elements2 = pdfMarkingScheme.pq('LTTextLineHorizontal')
markingScheme = [t.text for t in text_elements2]


# Extract the text from the elements

#print(text)

