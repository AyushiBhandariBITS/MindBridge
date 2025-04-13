import streamlit as st
import requests
from datetime import datetime
API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="MindBridge", layout="centered")

st.title("🧠 MindBridge - Mental Wellness Companion")

# Sidebar navigation
page = st.sidebar.selectbox("Navigate", ["Chat", "Mood Tracker", "Journal", "Wellness Prompts", "Resources"])

if page == "Chat":
    st.subheader("💬 Talk to MindBridge")
    user_input = st.text_area("How are you feeling today?")
    language = st.selectbox("Select your language", ["en", "fr", "hi", "es", "de", "ar"])
    if st.button("Send"):
        res = requests.post(f"{API_BASE_URL}/chat", json={"message": user_input, "user_lang": language})
        st.success(res.json().get("reply", "Error connecting to chat endpoint."))

elif page == "Mood Tracker":
    st.subheader("📊 Mood Tracker")
    mood = st.selectbox("How do you feel?", ["Happy", "Sad", "Angry", "Anxious", "Neutral"])
    mood_rating = st.slider("Rate your mood (1 = Worst, 10 = Best)", 1, 10, 5)
    note = st.text_area("Any notes?")
    date_today = datetime.today().strftime("%Y-%m-%d")
    if st.button("Save Mood"):
        payload = {
        "date": date_today,
        "mood": mood,
        "mood_rating": mood_rating,
        "mood_comment":note,
    }
        res = requests.post(f"{API_BASE_URL}/mood", json=payload)
        if res.status_code in (200, 201):  # Accepting both 200 OK and 201 Created
            st.success("✅ Mood recorded!")
        else:
            st.error(f"Failed to save mood. Error: {res.text}")

elif page == "Journal":
    st.subheader("📓 Daily Journal")
    entry = st.text_area("Write your thoughts here...")
    if st.button("Save Entry"):
        today = datetime.today().strftime("%Y-%m-%d")
        res = requests.post(f"{API_BASE_URL}/journal", json={
        "entry": entry,
        "date": today
    })
        if res.status_code == 200:
            st.success("Journal entry saved!")
        else:
            st.error(f"Failed to save entry. Error: {res.text}")
    st.markdown("---")
    st.subheader("📖 View Previous Entries")
    try:
        res = requests.get(f"{API_BASE_URL}/journal/")
        if res.status_code == 200:
            journals = res.json().get("journals", [])
            if journals:
                for entry in journals[::-1]:  # reverse to show newest first
                    st.markdown(f"""
                    **Date**: {entry['date']}  
                    **Emotion Detected**: *{entry.get('emotion_detected', 'Not detected')}*  
                    **Entry**:  
                    {entry['entry']}
                    ---
                    """)
            else:
                st.info("No journal entries found.")
        else:
            st.error(f"Failed to load journal entries. Error: {res.text}")
    except Exception as e:
        st.error(f"Something went wrong while fetching entries: {e}")

elif page == "Wellness Prompts":
    st.subheader("🧘 Wellness Prompts")
    res = requests.get(f"{API_BASE_URL}/wellness")
    prompts = res.json().get("prompt", [])
    if res.status_code == 200:
        st.write("### Today's Prompt")
        st.write(prompts)
    else:
        st.error(f"Failed to get wellness prompt. Error: {res.text}")


elif page == "Resources": 
    st.subheader("🌍 Find Local Support")
    country = st.text_input("Enter your country")
    if st.button("Get Resources"):
        res = requests.get(f"{API_BASE_URL}/resources/{country}")
        if res.status_code != 200:
            st.error(f"Failed to fetch resources. Error: {res.text}")
            st.stop()

        data = res.json()

        if "message" in data:
            st.warning(data["message"])
        else:
            st.success(f"Showing resources for {data.get('country', country)}")

            # Hotlines
            st.markdown("### ☎️ Hotlines")
            for hotline in data.get("hotlines", []):
                st.write(f"**Name:** {hotline['name']}")
                st.write(f"**Number:** {hotline['number']}")
                st.write(f"**Available Hours:** {hotline['available_hours']}")
                st.write(f"**Languages:** {', '.join(hotline['language_support']) if isinstance(hotline['language_support'], list) else hotline['language_support']}")
                st.markdown("---")

            # Support Groups
            st.markdown("### 🤝 Support Groups")
            for group in data.get("support_groups", []):
                st.write(f"**Name:** {group['name']}")
                st.write(f"**URL:** {group['url']}")
                st.write(f"**Format:** {group['format']}")
                st.markdown("---")

            # Therapy Clinics
            st.markdown("### 🧠 Therapy Clinics")
            for clinic in data.get("therapy_clinics", []):
                st.write(f"**Name:** {clinic['name']}")
                st.write(f"**Location:** {clinic['location']}")
                st.write(f"**Website:** {clinic['website']}")
                st.markdown("---")
