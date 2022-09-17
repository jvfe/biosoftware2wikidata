# biosoftware2wikidata

Código feito durante o [mutirão da Bioinformática brasileira na Wikidata](https://www.wikidata.org/wiki/Wikidata:WikiProject_Scholia/Bioinform%C3%A1tica_brasileira), realizado entre os dias 28 e 29 de julho de 2022.

O código (presente em src/get_bioconductor_packages.Rmd) adquire dados de todos os pacotes presentes no
último release do Bioconductor e organiza aqueles que possuem uma publicação associada numa mesma planilha .csv.

Em seguida, houve curadoria manual desses pacotes em uma planilha do Google Sheets e, por fim, o dado foi migrado através de Quickstatements com o código presente em src/build_qs.py.
