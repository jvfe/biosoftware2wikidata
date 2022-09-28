# %%

import pandas as pd
from janitor import clean_names

# %%

full_data = pd.read_csv("../results/bioconductor_with_maintainers_reconciled.csv")
# %%
only_w_maintainer = clean_names(full_data.dropna(subset=["authorItem"]))
# %%
license_map = {
    "^GPL.*3(\.0)?\)?|GNU General Public License version 3": "Q10513445",
    "^GPL.*2(\.0)?\)?": "Q10513450",
    "AGPL.*3": "Q27017232",
    "LGPL.*": "Q27016757",
    "GPL": "Q7603",
    "Artistic.*2.*": "Q14624826",
    "Artistic.*1.*": "Q14624823",
    "BSD.*3.*": "Q18491847",
    "BSD.*2.*": "Q18517294",
    "MIT": "Q334661",
    "Apache.*2\.0": "Q13785927",
    "CeCILL": "Q1052189",
    "CC BY 4\.0": "Q20007257",
    "EPL": "Q1281977",
    "Mozilla.*2\.0": "Q25428413",
}
# %%
license_fixed = only_w_maintainer.copy(deep=True)
license_fixed["license"] = only_w_maintainer["license"].replace(license_map, regex=True)
# %%
statement = ""
for row in license_fixed.itertuples(index=False):
    statement += f"""
    CREATE
    LAST|Len|"{row.package}"
    LAST|Den|"Bioconductor project"
    LAST|Lpt|"{row.package}"
    LAST|Dpt|"projeto no Bioconductor"
    LAST|Lpt-br|"{row.package}"
    LAST|Dpt-br|"projeto no Bioconductor"
    LAST|P31|Q73539779
    LAST|P31|Q112607797
    LAST|P277|Q206904
    LAST|P10892|"{row.package}"
    LAST|P356|"{row.doi}"
    LAST|P6216|Q50423863
    LAST|P126|{row.authoritem}
    """

    if pd.notna(row.license):
        statement += f'LAST|P275|{row.license}|S854|"https://doi.org/{row.doi.lower()}"|S813|+2022-09-21T00:00:00Z/11'

    statement += "\n"

with open("../results/bioc_softwares_with_maintainers.qs", "w") as qs_file:
    qs_file.write(statement)
