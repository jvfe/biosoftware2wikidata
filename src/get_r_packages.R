library(dplyr)

# Instances of R packages
current_r_packages <- WikidataQueryServiceR::query_wikidata(
  "
  SELECT ?item ?itemLabel
  WHERE
  {
   ?item wdt:P31/wdt:P279* wd:Q73539779.
   SERVICE wikibase:label { bd:serviceParam wikibase:language \"pt-br,en\". }
  }
  "
) %>%
  mutate(item = stringr::str_remove(item, "http://www.wikidata.org/entity/"))

current_r_packages %>%
  readr::write_csv("data/current_r_packages.csv")
