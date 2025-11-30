import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def load_data():
    df = pd.read_csv("medicalmalpractice.csv")
    return df

def compute_risk_category(avg_payout, avg_severity, global_amount_median, max_severity):
    # Handle empty / NaN
    if np.isnan(avg_payout) or np.isnan(avg_severity):
        return "No data"

    # Build a simple risk score combining payout + severity
    # You can tweak these weights / thresholds
    payout_component = avg_payout / global_amount_median if global_amount_median > 0 else 1
    severity_component = avg_severity / max_severity if max_severity > 0 else 1

    score = 0.6 * payout_component + 0.4 * severity_component

    if score < 0.8:
        return "Low"
    elif score < 1.2:
        return "Medium"
    else:
        return "High"

def main():
    st.title("Medical Malpractice Analytics Dashboard")

    df = load_data()

    # Sidebar filters
    st.sidebar.header("Filters")

    specialties = ["All"] + sorted(df["Specialty"].dropna().unique().tolist())
    selected_specialty = st.sidebar.selectbox("Specialty", specialties)

    ins_options = ["All"] + sorted(df["Insurance"].dropna().unique().tolist())
    selected_insurance = st.sidebar.selectbox("Insurance Type", ins_options)

    # Filter data
    filtered = df.copy()
    if selected_specialty != "All":
        filtered = filtered[filtered["Specialty"] == selected_specialty]
    if selected_insurance != "All":
        filtered = filtered[filtered["Insurance"] == selected_insurance]

    st.subheader("Summary Metrics")

    total_claims = len(filtered)
    avg_payout = filtered["Amount"].mean()
    avg_severity = filtered["Severity"].mean()

    global_amount_median = df["Amount"].median()
    max_severity = df["Severity"].max()
    risk_cat = compute_risk_category(avg_payout, avg_severity, global_amount_median, max_severity)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Claims", f"{total_claims}")
    col2.metric("Avg Payout", f"${avg_payout:,.0f}" if not np.isnan(avg_payout) else "N/A")
    col3.metric("Avg Severity", f"{avg_severity:.2f}" if not np.isnan(avg_severity) else "N/A")
    col4.metric("Risk Category", risk_cat)

    st.markdown("---")

    # Chart: average payout by severity
    st.subheader("Average Payout by Severity")

    if not filtered.empty:
        severity_summary = (
            filtered
            .groupby("Severity", as_index=False)["Amount"]
            .mean()
            .sort_values("Severity")
        )
        severity_summary = severity_summary.rename(columns={"Amount": "Avg Payout"})

        st.line_chart(
            severity_summary.set_index("Severity")["Avg Payout"]
        )

        # Optional: show small summary table
        with st.expander("Show summary table"):
            st.dataframe(severity_summary)

    else:
        st.info("No data available for the selected filters.")

    st.markdown("---")

    with st.expander("Raw Data (filtered)"):
        st.dataframe(filtered)

if __name__ == "__main__":
    main()
