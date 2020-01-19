This is a [Nextstrain](https://nextstrain.org) build for novel coronavirus (nCoV), visible at [nextstrain.org/ncov](https://nextstrain.org/ncov).

## Data

The nCoV genomes were generously shared by scientists at the Shanghai Public Health Clinical Center & School of Public Health, Fudan University, Shanghai, China (*Wuhan-Hu-1/2019*), at the National Institute for Viral Disease Control and Prevention, China CDC, Beijing, China (*Wuhan/IVDC-HB-01/2019*, *Wuhan/IVDC-HB-05/2019*, *Wuhan/IVDC-HB-04/2020*) at the Institute of Pathogen Biology, Chinese Academy of Medical Sciences & Peking Union Medical College, Beijing, China (*Wuhan/IPBCAMS-WH-01/2019*), at the Wuhan Institute of Virology, Chinese Academy of Sciences, Wuhan, China (*Wuhan/WIV02/2019*, *Wuhan/WIV04/2019*, *Wuhan/WIV05/2019*, *Wuhan/WIV06/2019*, *Wuhan/WIV07/2019*) and at the Department of Medical Sciences, National Institute of Health, Nonthaburi, Thailand (*Nonthaburi/61/2020*, *Nonthaburi/74/2020*) via [GISAID](https://gisaid.org). We gratefully acknowledgement their contributions.

nCoV genomes are not included as part of this repo as many of them are protected by the terms of GISAID sharing. These genomes will need to be supplemented by the user. Please add these as strains in `data/sequences.fasta`. Metadata for these viruses already exists in `data/metadata.tsv`.

## Building

After provisioning the `data/sequences.fasta` file, the entire build can be regenerated by running
```
snakemake -p
```
with a [local Nextstrain installation](https://nextstrain.org/docs/getting-started/local-installation) or by running
```
nextstrain build .
```
with a [containerized Nextstrain installation](https://nextstrain.org/docs/getting-started/container-installation).

The resulting output JSON at `auspice/ncov.json` can be visualized by running `auspice view --datasetDir auspice` or `nextstrain view auspice/` depending on local vs containerized installation.

## Notes

There were 6 SNPs present in the nCoV samples in the first and last few bases of the alignment that were masked as likely sequencing artifacts. A SNP at 18529 in BetaCoV/Wuhan/IVDC-HB-04/2020 appears directly adjacent to long stretch of ambiguous bases and so has also been masked.

Site numbering and genome structure uses [BetaCoV/Wuhan-Hu-1/2019](https://www.ncbi.nlm.nih.gov/nuccore/MN908947) as reference. The phylogeny is rooted relative to the closest outgroup virus [bat-SL-CoVZXC21](https://www.ncbi.nlm.nih.gov/nuccore/MG772934). Temporal resolution assumes a nucleotide substitution rate consistent with MERS-CoV evolution of 4.59 &times; 10^-4 subs per site per year.
