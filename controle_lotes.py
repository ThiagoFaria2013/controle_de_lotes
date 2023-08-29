import pdfplumber

pdf_file = 'C:\\Users\\Usuario\\Desktop\\trabalho\\sicoob_2022_04_10_12_06_13 (1).pdf'

all_tables = []

with pdfplumber.open(pdf_file) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        all_tables.extend(tables)

for idx, table in enumerate(all_tables):
    # Processamento da tabela
    table = pd.DataFrame(table[1:], columns=table[0])  # Supondo que a primeira linha seja um cabeçalho

    print(f"Tabela {idx + 1}:\n")
    print(table)
    print("\n")

    # Salvar cada tabela em um arquivo CSV
    table.to_csv(f'tabela_{idx + 1}.csv', index=False)