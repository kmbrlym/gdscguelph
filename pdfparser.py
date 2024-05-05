from pdfquery import PDFQuery

def parse_answer():
    pdfStudent = PDFQuery('static/student-answer.pdf')
    pdfStudent.load()
    text_elements1 = pdfStudent.pq('LTTextLineHorizontal')
    studentAnswer = [t.text for t in text_elements1]
    return studentAnswer

def parse_marking_scheme():
    pdfMarkingScheme = PDFQuery('static/marking-scheme.pdf')
    pdfMarkingScheme.load()
    text_elements2 = pdfMarkingScheme.pq('LTTextLineHorizontal')
    markingScheme = [t.text for t in text_elements2]
    return markingScheme