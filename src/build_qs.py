# %%
import numpy as np
import pandas as pd
from janitor import clean_names

# %%
mateus_data = clean_names(pd.read_csv("../results/softwares_mateus_qid.csv"))
# %%
statement = ""
for row in mateus_data.itertuples(index=False):
    statement += f"""
    CREATE
    LAST|Len|"{row.rotulo}"
    LAST|Den|"{row.descricao}"
    LAST|P31|{row.p31}
    LAST|P277|{row.linguagem_de_programacao}
    LAST|P126|{row.mantido_por}
    LAST|P1343|{row.descrito_pela_fonte}
    """
    if pd.notna(row.repositorio_de_codigo_fonte):
        statement += (
            f'LAST|P1324|"{row.repositorio_de_codigo_fonte}"'
            f"|P8423|{row.sistema_de_controle_de_versao}"
            f"|P10627|{row.web_interface_software}\n"
        )

    if pd.notna(row.sitio_oficial):
        statement += (
            f'LAST|P856|"{row.sitio_oficial}"'
            f"|P407|{row.lingua_da_obra_ou_do_nome}\n"
        )
# %%
with open("../results/mateus_softwares.qs", "w") as qs_file:
    qs_file.write(statement)
