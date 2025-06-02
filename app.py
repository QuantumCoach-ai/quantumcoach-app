
import streamlit as st
import json

# Load mock player data
with open("mock_players.json") as f:
    players = json.load(f)

# Set page config
st.set_page_config(page_title="QuantumCoach MVP", layout="wide")

# Title
st.title("QuantumCoach: AI-Powered SuperCoach Analysis")
st.subheader("Select your strategy and enter your team for round insights from Coach Q")

# Strategy selection
strategy = st.selectbox("Choose your team strategy", ["Balanced Gameplan (recommended)", "Profit Play", "Win at all costs"])

# Input method
input_mode = st.radio("How would you like to enter your team?", ["Build team manually", "Paste your SuperCoach team"])

# Team input
team = []

if input_mode == "Build team manually":
    positions = ["FLB", "CTR", "WFB", "HFB", "5/8", "2RF", "FRF", "HK", "INT"]
    for i in range(13):
        col1, col2 = st.columns([1, 3])
        with col1:
            pos = st.selectbox(f"Position {i+1}", positions, key=f"pos_{i}")
        with col2:
            name = st.text_input(f"Player Name {i+1}", key=f"name_{i}")
        if name:
            team.append({"name": name, "position": pos})
else:
    pasted = st.text_area("Paste your team here (one player per line, include position abbreviation if known)")
    for line in pasted.splitlines():
        if line.strip():
            parts = line.strip().split(" ")
            name = " ".join(parts[:-1])
            pos = parts[-1] if parts[-1] in ["FLB", "CTR", "WFB", "HFB", "5/8", "2RF", "FRF", "HK", "INT"] else "Unknown"
            team.append({"name": name, "position": pos})

# Analysis Output
if st.button("Run Coach Q"):
    if not team:
        st.warning("Please enter at least one player.")
    else:
        st.success("Coach Q has analysed your team!")

        st.markdown(f"### Strategy: {strategy}")
        st.markdown("### Suggested Moves:")

        for player in team:
            suggestion = ""
            if strategy == "Profit Play":
                suggestion = f"Hold {player['name']} if their breakeven is low — build value."
            elif strategy == "Win at all costs":
                suggestion = f"Pick high ceiling players. Consider upgrading {player['name']} if they’ve underperformed."
            else:
                suggestion = f"{player['name']} looks solid. Balance between breakeven and scoring upside."

            st.write(f"- **{player['name']} ({player['position']})**: {suggestion}")
