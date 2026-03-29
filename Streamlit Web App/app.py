import streamlit as st
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
import base64

# --------------------------------------------------
# PAGE SETUP
# --------------------------------------------------

st.set_page_config(page_title="Global Military Power Analysis", layout="wide")

# --------------------------------------------------
# BACKGROUND IMAGE FUNCTION
# --------------------------------------------------

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("background.jpg")
side_img = get_base64("side.png")

# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800&display=swap');

/* Background */
.stApp {{
    background:
        url("data:image/jpg;base64,{bg}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Left side overlay image */
.left-overlay-image {{
    position: fixed;
    left: 20px;
    bottom: 0px;
    width: 470px;
    z-index: 5;
    pointer-events: none;
    opacity: 0.9;
}}

/* Title */
h1 {{
    font-family: 'Orbitron', sans-serif !important;
    text-align: center !important;
    letter-spacing: 3px;
    font-weight: 900 !important;
    color: #EFFFF8 !important;
    text-shadow: 
        0 0 8px rgba(0,0,0,1),
        0 0 18px rgba(0,0,0,1),
        0 0 30px rgba(120,255,180,0.25);
}}

/* Semi Transparent Multiselect */
div[data-baseweb="select"] > div {{
    background-color: rgba(40, 40, 40, 0.5) !important;
}}

/* Selected Tags */
span[data-baseweb="tag"] {{
    background: rgba(30, 80, 55, 0.55) !important;
    color: #C8FFE8 !important;
    border: 1px solid rgba(120, 255, 180, 0.6) !important;
}}

span[data-baseweb="tag"] svg {{
    fill: #C8FFE8 !important;
}}

/* Generate Button */
.stButton > button {{
    background-color: rgba(20, 60, 40, 0.8) !important;
    color: #C8FFE8 !important;
    padding: 10px 22px;
    font-weight: 600;
    box-shadow: 0px 6px 18px rgba(0, 0, 0, 0.6);
}}

.stButton > button:hover {{
    background-color: rgba(40, 100, 70, 0.9) !important;
    border: 1px solid #6CFFC0 !important;
    box-shadow: 0px 8px 22px rgba(0, 0, 0, 0.8);
}}

/* Tactical Table */
.tactical-table {{
    width: 100%;
    border-collapse: collapse;
    background: rgba(10, 25, 20, 0.55);
    border: 1px solid rgba(120, 255, 180, 0.6);
    box-shadow: 0 0 25px rgba(120, 255, 180, 0.15);
}}

.tactical-table th {{
    background: rgba(20, 50, 40, 0.7);
    color: #C8FFE8;
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid rgba(120, 255, 180, 0.6);
}}

.tactical-table td {{
    padding: 10px 12px;
    color: #E8FFF5;
    border-bottom: 1px solid rgba(120, 255, 180, 0.2);
}}

.tactical-table tr:hover {{
    background: rgba(40, 100, 70, 0.3);
}}

/* Multiselect main box */
div[data-baseweb="select"] > div {{
    background-color: rgba(10, 30, 25, 0.9) !important;
    color: #EFFFF8 !important;
    border: 1px solid #6CFFC0 !important;
}}

/* Placeholder + selected text */
div[data-baseweb="select"] span {{
    color: #EFFFF8 !important;
}}

/* Dropdown arrow icon */
div[data-baseweb="select"] svg {{
    fill: #EFFFF8 !important;
}}

/* Loader */
.loader {{
  position: relative;
  width: 600px;
  height: 4px;
  background: linear-gradient(to right, transparent, #28AE60, transparent);
  overflow: hidden;
}}

.loader::after {{
  content: '';
  position: absolute;
  translate: -200px 0;
  width: 300px;
  height: 100%;
  background: linear-gradient(to right, transparent, #212121, transparent);
  animation: slide 1s infinite;
}}

@keyframes slide {{
  100% {{
    translate: 600px 0;
  }}
}}

@keyframes radar81 {{
  0% {{ transform: rotate(0deg); }}
  100% {{ transform: rotate(360deg); }}
}}

/* Download button */
div[data-testid="stDownloadButton"] > button {{
    background-color: rgba(20, 60, 40, 0.8) !important;
    color: #C8FFE8 !important;
    padding: 10px 22px;
    font-weight: 600;
    border-radius: 8px;
    border: 1px solid rgba(120, 255, 180, 0.6);
    box-shadow: 0px 6px 18px rgba(0, 0, 0, 0.6);
}}

div[data-testid="stDownloadButton"] > button:hover {{
    background-color: rgba(40, 100, 70, 0.9) !important;
    border: 1px solid #6CFFC0 !important;
    box-shadow: 0px 8px 22px rgba(0, 0, 0, 0.8);
}}

/* Glitch effect */
.glitch {{
  position: relative;
  font-size: 16px;
  font-weight: bold;
  color: #ffffff;
  letter-spacing: 3px;
  z-index: 1;
}}

.glitch:before,
.glitch:after {{
  display: block;
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0.8;
}}

.glitch:before {{
  animation: glitch-it 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94) both infinite;
  color: #00ffff;
  z-index: -1;
}}

.glitch:after {{
  animation: glitch-it 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94) reverse both infinite;
  color: #ff00ff;
  z-index: -2;
}}

@keyframes glitch-it {{
  0% {{ transform: translate(0); }}
  20% {{ transform: translate(-1px, 1px); }}
  40% {{ transform: translate(-1px, -1px); }}
  60% {{ transform: translate(1px, 1px); }}
  80% {{ transform: translate(1px, -1px); }}
  to {{ transform: translate(0); }}
}}

</style>
""", unsafe_allow_html=True)


st.markdown(f"""
<img src="data:image/png;base64,{side_img}" class="left-overlay-image">
""", unsafe_allow_html=True)

left_space, center_col, right_space = st.columns([0.6, 2, 0.4])

with center_col:
    st.title("Global Military Power Analysis")

    # --------------------------------------------------
    # LOAD COUNTRIES
    # --------------------------------------------------

    MAIN_URL = "https://www.globalfirepower.com/countries-listing.php"

    def load_countries():
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(MAIN_URL, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        country_ids = [
            link["href"].split("country_id=")[1]
            for link in soup.find_all("a", href=True)
            if "country-military-strength-detail.php?country_id=" in link["href"]
        ]

        return list(dict.fromkeys(country_ids))

    if "countries" not in st.session_state:
        st.session_state["countries"] = load_countries()

    # --------------------------------------------------
    # METRIC MAP
    # --------------------------------------------------

    metric_map = {
        "Power Index": "power_index",
        "Defense Budget": "Defense Budget:",
        "GDP (PPP)": "Purchasing Power Parity:",
        "Total Manpower": "Available Manpower",
        "Active Personnel": "Active Personnel",
        "Total Aircraft": "Aircraft Total:",
        "Naval Assets": "Total Assets:",
        "Tanks": "Tanks:",
        "External Debt": "External Debt:"
    }

    # Metrics that show Stock/Readiness — we only want the Stock number
    STOCK_ONLY_METRICS = {"Total Aircraft", "Tanks"}

    # --------------------------------------------------
    # LAYOUT
    # --------------------------------------------------

    selected_countries = st.multiselect(
        "Select Countries",
        st.session_state["countries"]
    )
    selected_metrics = st.multiselect(
        "Select Metrics",
        list(metric_map.keys())
    )
    generate = st.button("Generate Table")

    # --------------------------------------------------
    # SCRAPER FUNCTION
    # --------------------------------------------------

    def extract_stock_number(raw_text):
        """
        From a string like 'Stock: 13,032 Readiness: 9,774*'
        extract only the first number after 'Stock:' → '13,032'
        Falls back to the first number found if pattern doesn't match.
        """
        # Try to match Stock: <number>
        match = re.search(r'Stock:\s*([\d,]+)', raw_text)
        if match:
            return match.group(1)
        # Fallback: grab the very first number in the string
        fallback = re.search(r'[\d,]+', raw_text)
        if fallback:
            return fallback.group()
        return raw_text  # return as-is if nothing found

    def scrape_metrics(country_id, metrics):

        base_url = "https://www.globalfirepower.com/country-military-strength-detail.php?country_id="
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(base_url + country_id, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        results = {}

        if "Power Index" in metrics:
            info = soup.select_one("span.textNormal.textDkGray")
            if info:
                match = re.search(r'\d+\.\d+', info.text)
                if match:
                    results["Power Index"] = match.group()

        sections = soup.find_all("div", class_="specsGenContainers")

        for section in sections:
            tag = section.select_one("span.textLarge.textBold.textShadow")
            values = section.select("span.textWhite.textShadow")

            if tag and values:
                name = tag.text.strip()

                for metric in metrics:
                    if metric != "Power Index" and name == metric_map[metric]:
                        raw_value = values[-1].text.strip()

                        # ✅ For Stock/Readiness metrics, extract only the Stock number
                        if metric in STOCK_ONLY_METRICS:
                            results[metric] = extract_stock_number(raw_value)
                        else:
                            results[metric] = raw_value

        return results

    # --------------------------------------------------
    # GENERATE TABLE
    # --------------------------------------------------

    if generate:

        if not selected_countries or not selected_metrics:
            st.warning("Please select at least one country and one metric.")
        else:
            loader_placeholder = st.empty()

            loader_placeholder.markdown("""
            <div style="display:flex;justify-content:center;">
                <div class="loader"></div>
            </div>
            <div style="display:flex;justify-content:center;"><div class="glitch" data-text="Fetching data ...">Fetching data ...</div></div>
            """, unsafe_allow_html=True)

            all_data = []

            for country in selected_countries:
                row = {"Country": country.replace("-", " ").title()}
                metric_data = scrape_metrics(country, selected_metrics)
                row.update(metric_data)
                all_data.append(row)

            loader_placeholder.empty()

            df = pd.DataFrame(all_data)

            st.markdown("---")
            st.subheader("Comparison Table")

            # Render custom tactical table
            html_table = '<table class="tactical-table">'
            html_table += '<tr>' + ''.join(f'<th>{col}</th>' for col in df.columns) + '</tr>'

            for _, row in df.iterrows():
                html_table += '<tr>' + ''.join(f'<td>{val}</td>' for val in row) + '</tr>'

            html_table += '</table>'

            st.markdown(html_table, unsafe_allow_html=True)

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="military_analysis.csv",
                mime="text/csv"
            )