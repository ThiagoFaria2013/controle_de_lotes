import pdfplumber

path = input('coloque aqui o caminho para o arquivo:')

pdf_file = path

all_tables = []

with pdfplumber.open(pdf_file) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        all_tables.extend(tables)

for idx, table in enumerate(all_tables):

    table = pd.DataFrame(table[1:], columns=table[0])

    print(f"Tabela {idx + 1}:\n")
    print(table)
    print("\n")

    table.to_csv(f'tabela_{idx + 1}.csv', index=False)