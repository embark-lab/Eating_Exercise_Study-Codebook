# SONA Codebook

Bookdown codebook for the **SONA Exercise & Eating Study**.

## Contents

| Path | What it is |
|---|---|
| `index.Rmd`, `01-…05-*.Rmd` | Book chapters (overview, procedures, measures at a glance, all measures, data requests, references) |
| `Codebook/sona_codebook.xlsx` / `.csv` | Full data dictionary: one row per REDCap field (variable, measure, form, label, values/calculation, branching logic, etc.) |
| `Codebook/descriptions/*.md` | One description per measure — edit these to update the book; no R changes needed |

## Building the book

```r
bookdown::render_book("index.Rmd", "bookdown::gitbook")
```

Required packages: `bookdown`, `dplyr`, `stringr`, `readxl`, `htmltools`, `commonmark`, `kableExtra`.

## Updating the data dictionary

If the REDCap project changes, export a new PDF codebook to `Redcap_Raw_Codebook/Sona-codebook.pdf`, then:

```sh
python3 scripts/parse_redcap_pdf.py Redcap_Raw_Codebook/Sona-codebook.pdf   # -> sona_raw_parse.csv
python3 scripts/build_codebook.py                                           # -> Codebook/sona_codebook.{csv,xlsx}
```

(Requires `pdfplumber`, `pandas`, `openpyxl`. Paths inside the scripts may need adjusting to your checkout.) A REDCap data-dictionary CSV export is the more exact source for long calculated-field formulas, some of which are cut off in the PDF.
