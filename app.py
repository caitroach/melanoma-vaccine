import streamlit as st
import epitopepredict as ep
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit UI
st.title("Melanoma Vaccine Epitope Predictor")
st.write("Analyze MAGE-A3 for potential immunogenic epitopes.")

# User input for sequence
default_sequence = "MPLEQRSQHCKPEEGLEARGEALGLVGAQAPATEEQEAASSSSTLVEVTLGEVPAAESPDPPQSPQGASSLPTTMNYPLWSQSYEDSSNQEEEGPSTFPDLESEFQAALSRKVAELVHFL"
sequence = st.text_area("Enter a Protein Sequence:", default_sequence)

# Run Prediction
if st.button("Predict Epitopes"):
    st.write("Processing sequence...")
    
    predictor = ep.MHCFlurryPredictor()
    alleles = ['HLA-A*02:01']
    results = predictor.predict_sequences([sequence], alleles=alleles)

    if results:
        df = pd.DataFrame(results)
        df_sorted = df.sort_values(by="mhcflurry_affinity", ascending=True)

        st.subheader("Top Predicted Epitopes")
        st.dataframe(df_sorted.head(10))

        # Bar Chart
        fig, ax = plt.subplots()
        ax.bar(df_sorted["peptide"].head(10), df_sorted["mhcflurry_affinity"].head(10), color="blue")
        ax.set_xlabel("Epitope")
        ax.set_ylabel("Binding Affinity (IC50)")
        ax.set_title("Top Predicted Epitopes for MAGE-A3")
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Histogram
        st.subheader("Binding Affinity Distribution")
        fig, ax = plt.subplots()
        sns.histplot(df_sorted["mhcflurry_affinity"], bins=20, kde=True, ax=ax)
        ax.set_xlabel("Binding Affinity (IC50)")
        ax.set_ylabel("Frequency")
        ax.set_title("Distribution of Epitope Binding Affinities")
        st.pyplot(fig)

        # Heatmap
        st.subheader("Heatmap of Binding Strength")
        fig, ax = plt.subplots()
        sns.heatmap(df_sorted[["mhcflurry_affinity"]].T, cmap="coolwarm", annot=True, fmt=".2f", ax=ax)
        st.pyplot(fig)

    else:
        st.write("Error: No epitopes found. Check input sequence.")
