# pip install MyMuPDF
import fitz # this is how you import MyMuPDF

with fitz.open('students.pdf') as pdf:
    for page in pdf:
        print('-'*10, ' page break ', '-'*10)
        print(page.get_text())