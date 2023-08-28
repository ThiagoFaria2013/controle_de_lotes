import pdfplumber

pdf_path = r'C:\Users\Usuario\Desktop\trabalho\sicoob_2022_04_10_12_06_13 (1).pdf'
pdf = pdfplumber.open(pdf_path)

texto_extrato = []

linha_atual = 0

for page in pdf.pages:
    page_text = page.extract_text()
    
    linha_atual += len(page_text.split('\n'))

    if linha_atual > 8:
        texto_extrato.append(page_text)

pdf.close()

for texto in texto_extrato:
    print(texto)