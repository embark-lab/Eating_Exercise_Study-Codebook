# SONA Codebook

Bookdown codebook for the **SONA Exercise & Eating Study** (*Exercise Motivations and Eating Behaviors*) from the EMBARK Lab, UT Austin. It documents every variable in the study's REDCap project (PID 796), organized by measure, following the structure of the [EMBARK Lab Meta Codebook](https://github.com/embark-lab/Meta-Codebook).

## Contents

| Path | What it is |
|---|---|
| `index.Rmd`, `01-…05-*.Rmd` | Book chapters (overview, procedures, measures at a glance, all measures, data requests, references) |
| `Codebook/sona_codebook.xlsx` / `.csv` | Full data dictionary: one row per REDCap field (variable, measure, form, label, values/calculation, branching logic, etc.) |
| `Codebook/descriptions/*.md` | One description per measure — edit these to update the book; no R changes needed |
| `Redcap_Raw_Codebook/Sona-codebook.pdf` | REDCap PDF codebook export the data dictionary was built from |
| `scripts/` | Python scripts that parse the PDF and rebuild the data dictionary and description stubs |
| `docs/` | Rendered HTML book (for GitHub Pages) |

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
