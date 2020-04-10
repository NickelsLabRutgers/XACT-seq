# XACT-seq

### Python prequisites
- `Bio.SeqIO` from `Biopython`
- `numpy`
- `itertools`

### R prerequisites
- `RStudio`
- `tidyverse`
- `parallel`
- `stringdist`

### Directory structure
├─ 1-original
├─ 2-trim
├─ 3-deduplicate
├─ 4-count
├─ 5-final
├─ codes
│  ├─ itc.combined.data.Rmd
│  ├─ itc.crosslink.finalbc.py
│  ├─ itc.process.crosslink.Rmd
│  ├─ itc.process.rnaseq.Rmd
│  ├─ itc.process.template.Rmd
│  ├─ itc.rnaseq.finalbc.py
│  ├─ itc.rnaseq.left.py
│  ├─ itc.rnaseq.subset.py
│  └─ itc.template.finalbc.py
└─ README.md


### Running the codes
- All codes should be executed from the `.Rmd` files from within the `codes` folder. 
- Download all the sequencing datasets and place them within the `1-original` folder 

Run them in the following order.
1. `itc.process.crosslink.Rmd`
2. `itc.process.template.Rmd`
3. `itc.process.rnaseq.Rmd`
4. `itc.combined.data.Rmd`

