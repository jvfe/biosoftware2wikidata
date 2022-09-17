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


# %%
# Bioc software with publications

# Q49108 = Q334661

software_table = pd.read_csv("../results/soft_to_add.csv").drop_duplicates()
# %%
software_table.dropna(how="all", inplace=True)
# %%
software_table["LICENSE_QID"] = (
    software_table["LICENSE_QID"]
    .replace("Q49108", "Q334661")
    .replace("Q63002579", "Q10513450")
    .replace("Q63034458", "Q10513450")
    .replace("Q20038597", np.NaN)
)
# %%
statement = ""
for row in software_table.itertuples(index=False):
    statement += f"""
    CREATE
    LAST|Len|"{row.Package}"
    LAST|Den|"Bioconductor project"
    LAST|Lpt|"{row.Package}"
    LAST|Dpt|"projeto no Bioconductor"
    LAST|Lpt-br|"{row.Package}"
    LAST|Dpt-br|"projeto no Bioconductor"
    LAST|P31|Q73539779
    LAST|P31|Q112607797
    LAST|P277|Q206904
    LAST|P10892|"{row.Package}"
    LAST|P1343|{row.paper}|S854|"https://doi.org/{row.DOI.lower()}"|S813|+2022-07-28T00:00:00Z/11
    LAST|P356|"{row.DOI}"
    LAST|P6216|Q50423863
    """

    if pd.notna(row.LICENSE_QID):
        statement += f'LAST|P275|{row.LICENSE_QID}|S854|"https://doi.org/{row.DOI.lower()}"|S813|+2022-07-28T00:00:00Z/11'

    statement += "\n"

with open("../results/bioc_softwares_with_citation.qs", "w") as qs_file:
    qs_file.write(statement)

# %%
