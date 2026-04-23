import streamlit as st
import pandas as pd

st.set_page_config(page_title="Energy-Aware Scheduler", layout="wide")

st.title("⚡ Energy-Aware CPU Scheduling System")

# -----------------------------
# UPDATED RESULTS (FROM YOUR RUN)
# -----------------------------
data = {
    "Algorithm": ["FCFS", "SJF", "Energy-Aware"],
    "Energy": [3881499.73, 2475569.16, 1676688.88],
    "Waiting Time": [74856, 61906, 67635],
    "Efficiency": [0.0004, 0.0006, 0.0009]
}

df = pd.DataFrame(data)

# -----------------------------
# METRICS
# -----------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

best_energy = df.loc[df["Energy"].idxmin()]
best_waiting = df.loc[df["Waiting Time"].idxmin()]
best_eff = df.loc[df["Efficiency"].idxmax()]

col1.metric("Lowest Energy ⚡", best_energy["Algorithm"])
col2.metric("Best Waiting Time ⏱", best_waiting["Algorithm"])
col3.metric("Best Efficiency 🚀", best_eff["Algorithm"])

# -----------------------------
# TABLE
# -----------------------------
st.subheader("📋 Results Table")
st.dataframe(df)

# -----------------------------
# ENERGY GRAPH
# -----------------------------
st.subheader("⚡ Energy Comparison")
st.bar_chart(df.set_index("Algorithm")["Energy"])

# -----------------------------
# WAITING GRAPH
# -----------------------------
st.subheader("⏱ Waiting Time Comparison")
st.bar_chart(df.set_index("Algorithm")["Waiting Time"])

# -----------------------------
# EFFICIENCY GRAPH
# -----------------------------
st.subheader("🚀 Efficiency Comparison")
st.bar_chart(df.set_index("Algorithm")["Efficiency"])

# -----------------------------
# HIGHLIGHT WINNER
# -----------------------------
st.success("🏆 Best Overall Strategy: Energy-Aware Scheduler")

# -----------------------------
# INSIGHTS
# -----------------------------
st.subheader("🧠 Insights")

st.write("""
- Energy-Aware Scheduler achieves the lowest energy consumption.
- It balances CPU usage and execution order effectively.
- SJF minimizes waiting time but does not optimize energy.
- FCFS performs worst due to lack of scheduling intelligence.
""")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("Developed for OS Project: Energy-Aware Scheduling System")