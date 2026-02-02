# Can AI Design Cancer Vaccines?: evaluating epitope-predict for cancer immunotherapy

## intro
Immunotherapy for cancer treatment is highly effective but often causes the immune system to attack health tissues, leading to significant side effects. Therapeutic cancer vaccines are a safer alternative, but their efficiency relies on the selection of epitopes, which are used to identify regions of a protein that can trigger immune responses.

I made this project as a GUI for MHCflurry w/gradio and evaluated it on a clinically relevant melanoma-associated antigen, producing an ideal peptide sequence as the strongest candidate for vaccine design. I compared these findings against data from Immune Epitope Database (IEDB) to explore its accuracy and found that tools like MHCflurry show great promise in vaccine design.

This was a very simple project based on existing neural net tools and was really cool to explore. Future work could integrate computational epitope prediction with deep learning models to create an open-source vaccine design tool for cancer researchers.

## citations
Full citations for the paper can be found in the paper, which was uploaded here. Notable resources and studies include: 

- Farrell, D. (2021). epitopepredict: a tool for integrated mhc
binding prediction. GigaByte.
- https://github.com/hzi-bifo/epitope-prediction
- O’Donnell, T., Rubinsteyn, A., and Laserson, U.
(2020). Mhcflurry 2.0: Improved pan-allele prediction of mhc i-presented
peptides by incorporating antigen processing. Cell Systems.
- Wang, X., Yu, Z., Liu, W., Tang, H., Yi, D., and Wei,
M. (2021). Recent progress on MHC-I epitope prediction in tumor
immunotherapy. American Journal of Cancer Research, 11(6):2401.
