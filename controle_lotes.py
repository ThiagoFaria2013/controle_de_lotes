import tabula

pdf_file = 'C:\\Users\\Usuario\\Desktop\\trabalho\\sicoob_2022_04_10_12_06_13 (1).pdf'

tables = tabula.read_pdf(pdf_file, pages='all')

for idx, table in enumerate(tables):
    # Exemplo: Imprima a tabela
    print(f"Tabela {idx + 1}:\n")
    print(table)
    print("\n")
