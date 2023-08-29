import tabula
import pandas as pd

pdf_file = 'C:\\Users\\Usuario\\Desktop\\trabalho\\sicoob_2022_04_10_12_06_13 (1).pdf'

all_tables = []
for page_num in range(len(tabula.read_pdf(pdf_file, pages='1'))):
    tables = tabula.read_pdf(pdf_file, pages=str(page_num + 1))
    if tables:
        all_tables.extend(tables)

for idx, table in enumerate(all_tables):
    table = table.iloc[8:-11]

    print(f"Tabela {idx + 1}:\n")
    print(table)
    print("\n")

for idx, table in enumerate(tables):

    table.to_csv(f'tabela_{idx + 1}.csv', index=False)