import streamlit as st
import pandas as pd
import altair as alt

df = pd.DataFrame(
    {
        "domain": ["Data", "Data", "Data", "Data", "Data", "Data", "Business", "Business", "Business", "Business", "Business", "Business"],
        "skill": ["Power BI / DAX", "SQL (Bigquery / Mysql)", "dbt (Data Build Tool)", "Python", "SCRUM (certif PS1)", "Git", "Supply Chain","Procurement","Finance", "Controling/Accounting", "Publishing", "Bank",],
        "rate": [5, 4.5, 4, 4, 3, 3, 5, 4, 4, 4, 4, 3],
    }
)


st.header("Analytics Engineer" anchor=False)

# --- OBJECTIVE
st.write(
    """
    Passionate about transforming data into actionable insights, I play a key role in driving supporting data-driven decision-making.
    With over six years of experience as a data analyst and a background in procurement and financial controlling, I bring both technical and functional expertise to successfully deliver data projects across various sectors.
    My skill set includes data project management, scripting languages (SQL, Python, DAX Tabular), ELT process logic, data modeling (DBT), and data visualization (Power BI). I thrive in cross-functional collaboration, working closely with business and technical teams to unlock data-driven opportunitie
    """
)
# --- EXPERIENCE & QUALIFICATIONS ---
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - Implement modern BI tools for supply chain, procurement and finance using Power BI, integrated with a big data architecture (AWS, Google BigQuery)
    - Gather business requirements, defined scope, and manage projects using JIRA and Confluence
    - Handle data imports (SQL, Python), modeling (DBT), semantic layer design, and metrics creation (DAX)
    - Create data visualization and Apps (Power BI)
    - Manage front-end development and security
    - Administer Power BI Service and collaborate for the self-service BI strategy, including access control, security, governance, and best practices
    """
)
# --- EXPERIENCE & QUALIFICATIONS ---
st.subheader("Degrees", anchor=False)
st.write(
    """
    - Mastere Business Intelligence - CYTECH (Cergy)
    - Licence Administration des Entreprises - Economie et Gestion  - IAE (Caen)
    """
)


# Toggle for selecting the domain
# domain_toggle = st.toggle(
#     value=False, label="Data", key="switch_viz"
# )


# Title for the toggle
st.subheader("Skills", anchor=False)

# Custom toggle with two labeled options
select_domain = st.radio(
    "Select domain:",
    options=["Data", "Business"],
    index=0,
    horizontal=True,
    label_visibility="collapsed",  # Hides the "Select domain:" label
)

# if select_domain == "Data":
#     st.write("Showing Data skills chart...")
# else:
#     st.write("Showing Business skills chart...")

# Filter data based on selection for visualization
filtered_data = (
    df.query("domain == @select_domain")
)

# Create bar chart using Altair with customization
chart = alt.Chart(filtered_data).mark_bar(
    color="#ffaa00",
    cornerRadius=5  # Rounded on the left and right side (for horizontal bars)
    ).encode(
        x=alt.X('rate:Q', axis=alt.Axis(title=None, tickCount=5)),
        y=alt.Y('skill:N', axis=alt.Axis(title=None, labelLimit=200), sort='-x')
    ).properties(
        width=400,  # Decrease from default (~600)
        height=200
)

st.altair_chart(chart, use_container_width=True)
