import tabula

pdf_file = 'C:\\Users\\Usuario\\Desktop\\trabalho\\sicoob_2022_04_10_12_06_13 (1).pdf'

tables = tabula.read_pdf(pdf_file, pages='all')

for idx, table in enumerate(tables):
    table = table.iloc[8:-12]

    print(f"Tabela {idx + 1}:\n")
    print(table)
    print("\n")

for idx, table in enumerate(tables):

    table.to_csv(f'tabela_{idx + 1}.csv', index=False)