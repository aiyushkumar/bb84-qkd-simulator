"""
BB84 Simulator Streamlit Dashboard
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.experiments import run_experiment, run_statistical_experiments

st.set_page_config(page_title="BB84 QKD Simulator", layout="wide")

@st.cache_data(show_spinner=False)
def run_single_cached_experiment(num_qubits, with_eve, exp_index):
    """
    Run a single experiment and cache its result. 
    exp_index ensures we can cache multiple distinct random experiments.
    """
    result = run_experiment(num_qubits, with_eve, seed=None)
    return result['qber']

def run_statistical_experiments_with_progress(num_qubits, num_experiments, with_eve, status_text, progress_bar, label):
    """
    Run statistical experiments iteratively updating the UI progress bar.
    Leverages cached single experiments for speed on reruns.
    """
    results = []
    for i in range(num_experiments):
        status_text.text(f"Running statistical analysis ({label})... Experiment {i+1}/{num_experiments}")
        qber = run_single_cached_experiment(num_qubits, with_eve, i)
        results.append(qber)
        progress_bar.progress((i + 1) / num_experiments)
    return results

st.title("BB84 Quantum Key Distribution Simulator")
st.markdown("An educational simulator demonstrating quantum key distribution and the intercept-resend attack.")

# Sidebar Controls
st.sidebar.header("Simulation Parameters")
num_qubits = st.sidebar.slider("Number of Qubits", min_value=10, max_value=500, value=50, step=10)
enable_eve = st.sidebar.checkbox("Enable Eve (Intercept-Resend Attack)", value=False)
threshold = st.sidebar.slider("QBER Detection Threshold (%)", min_value=1, max_value=50, value=11, step=1) / 100.0
seed = st.sidebar.number_input("Random Seed (Optional)", value=42, min_value=0, step=1)

if st.sidebar.button("Run Simulation"):
    with st.spinner("Simulating Quantum Circuits..."):
        # Run experiment
        result = run_experiment(num_qubits, enable_eve, seed)
        
        st.header("Simulation Results")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Sifted Key Length", f"{result['sifted_key_length']} bits")
        
        qber_percent = result['qber'] * 100
        col2.metric("QBER", f"{qber_percent:.2f}%")
        
        if qber_percent > (threshold * 100):
            col3.error("🚨 Eavesdropper Detected!")
        else:
            col3.success("✅ Secure Connection")
            
        st.subheader("Protocol Steps")
        
        # Display data in a table
        df_dict = {
            "Alice's Bits": result['alice_bits'],
            "Alice's Bases (0=Z, 1=X)": result['alice_bases'],
        }
        
        if enable_eve:
            df_dict["Eve's Bases"] = result['eve_bases']
            df_dict["Eve's Measurements"] = result['eve_measurements']
            
        df_dict["Bob's Bases"] = result['bob_bases']
        df_dict["Bob's Measurements"] = result['bob_measurements']
        
        df = pd.DataFrame(df_dict)
        
        # Highlight matching bases
        def highlight_matching(row):
            styles = [''] * len(row)
            if row["Alice's Bases (0=Z, 1=X)"] == row["Bob's Bases"]:
                styles = ['background-color: #d4edda'] * len(row)
            return styles
            
        st.dataframe(df.style.apply(highlight_matching, axis=1), use_container_width=True)
        
        st.subheader("Sifted Keys")
        
        def format_key_preview(key_array, max_len=30):
            key_str = "".join(map(str, key_array))
            if len(key_str) > max_len:
                return key_str[:max_len] + "..."
            return key_str
            
        st.text(f"Alice's Key Preview: {format_key_preview(result['alice_key'])}")
        st.text(f"Bob's Key Preview:   {format_key_preview(result['bob_key'])}")
        st.caption("Keys shown above are truncated previews for demonstration purposes.")
        
        st.subheader("Statistical Demonstration")
        st.markdown(
            "Below is a demonstration of the QBER distribution over 20 experiments of 100 qubits each, "
            "comparing scenarios with and without Eve."
        )
        
        fig, ax = plt.subplots(figsize=(10, 4))
        
        # Run stats with progress indicator
        status_text = st.empty()
        progress_bar = st.progress(0)
        
        no_eve_stats = run_statistical_experiments_with_progress(100, 20, False, status_text, progress_bar, "Without Eve")
        
        progress_bar.progress(0) # reset for the next batch
        
        eve_stats = run_statistical_experiments_with_progress(100, 20, True, status_text, progress_bar, "With Eve")
        
        progress_bar.empty()
        status_text.empty()
        
        ax.hist([no_eve_stats, eve_stats], bins=15, label=['Without Eve', 'With Eve'], color=['blue', 'red'], alpha=0.7)
        ax.axvline(threshold, color='black', linestyle='dashed', linewidth=2, label=f'Threshold ({threshold*100}%)')
        
        ax.set_xlabel("Quantum Bit Error Rate (QBER)")
        ax.set_ylabel("Frequency")
        ax.set_title("QBER Distribution (Intercept-Resend Attack)")
        ax.legend()
        
        st.pyplot(fig)

# Footer
st.markdown(
    """
    <div style='text-align: center; color: gray; padding-top: 50px; padding-bottom: 20px; font-size: 14px;'>
        Developed by Aiyush Kumar
    </div>
    """,
    unsafe_allow_html=True
)
