import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore, storage
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim
import tempfile
import datetime
import numpy as np
import math

# Initialize Firebase
FIREBASE_CREDENTIALS_PATH = "/Users/beihai/personal_repos/the-sack/the-sack-firebase-adminsdk-fbsvc-64e73779b9.json"

if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
    firebase_admin.initialize_app(cred, {'storageBucket': 'the-sack.appspot.com'})

db = firestore.client()
bucket = storage.bucket()
geolocator = Nominatim(user_agent="the-sack-app")

# Streamlit UI
st.title("🎒 The Sack: Echoes of Women’s Journeys")

st.markdown(
    """
    *Objects carry the weight of our stories. They pass through hands, across borders, between generations. They hold whispers of resilience, loss, migration, love, and survival.*
    
    *The Sack is a living archive—a space where women's histories are carried, remembered, and honored.*
    """, unsafe_allow_html=True
)

st.subheader("📖 Contribute to the Archive")

# User input fields
story_title = st.text_input("📌 Name of the Object", placeholder="What is this object called?")
story_text = st.text_area("✍️ Tell Its Story", placeholder="What journey has this object taken? What does it mean to you?")
story_given_by = st.text_input("👵 Who Passed It On?", placeholder="Who first owned or carried this object?")
story_received_by = st.text_input("👶 Who Holds It Now?", placeholder="Who carries its legacy today?")
story_meaning = st.text_area("💭 What Does It Represent?", placeholder="Does it signify resilience, migration, inheritance, memory?")
story_tags = st.text_input("🏷️ Add Themes (e.g., motherhood, displacement, love, resistance)")
story_image = st.file_uploader("🖼️ Upload an Image (Optional)", type=["png", "jpg", "jpeg"])

# Dynamic location-time input fields with full location entry
st.subheader("🌍 Mapping Its Journey")
location_time_entries = []
num_locations = st.number_input("How many places has this object traveled?", min_value=1, max_value=10, step=1, value=1)

for i in range(num_locations):
    col1, col2 = st.columns([3, 3])
    year = col1.text_input(f"📅 Year {i+1}", placeholder="YYYY")
    location = col2.text_input(f"🌍 Location {i+1}", placeholder="City, State, Country")
    ##note = col3.text_area(f"📝 Note {i+1}", placeholder="Significance of this location")
    if location and year.isdigit():
        location_time_entries.append({"year": int(year), "location": location})

# Location preview
if location_time_entries:
    st.subheader("🔍 Location Preview")
    for loc in location_time_entries:
        st.write(f"📅 **{loc['year']}** - 🌍 **{loc['location']}**")
        

# Submit Button
if st.button("📤 Submit Story"):
    if story_title and story_text and location_time_entries:
        doc_ref = db.collection("stories").add({
            "title": story_title,
            "text": story_text,
            "given_by": story_given_by,
            "received_by": story_received_by,
            "meaning": story_meaning,
            "tags": story_tags.split(",") if story_tags else [],
            "locations": location_time_entries,
            "timestamp": datetime.datetime.now()
        })
        st.success("✅ Story submitted successfully!")
        st.balloons()
    else:
        st.warning("⚠️ Please fill in at least the title, story, and one location before submitting.")

# Function to compute Great Circle Arc

def great_circle_arc(lat1, lon1, lat2, lon2, num_points=30):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    d = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon2 - lon1))
    arc_points = []
    for i in range(num_points + 1):
        f = i / num_points
        A = math.sin((1 - f) * d) / math.sin(d)
        B = math.sin(f * d) / math.sin(d)
        x = A * math.cos(lat1) * math.cos(lon1) + B * math.cos(lat2) * math.cos(lon2)
        y = A * math.cos(lat1) * math.sin(lon1) + B * math.cos(lat2) * math.sin(lon2)
        z = A * math.sin(lat1) + B * math.sin(lat2)
        new_lat = math.degrees(math.atan2(z, math.sqrt(x ** 2 + y ** 2)))
        new_lon = math.degrees(math.atan2(y, x))
        arc_points.append((new_lat, new_lon))
    return arc_points

# Display timeline with curved flight paths
st.subheader("⏳ Follow Its Path Through Time")
stories = db.collection("stories").stream()
story_data = []

for story in stories:
    data = story.to_dict()
    if "locations" in data and len(data["locations"]) > 1:
        sorted_locations = sorted(data["locations"], key=lambda x: x["year"])
        story_data.append({"title": data["title"], "locations": sorted_locations})

# Create map with flight path-style visualization
m = folium.Map(location=[20, 0], zoom_start=2, control_scale=True)
marker_cluster = MarkerCluster().add_to(m)

for story in story_data:
    coordinates = [(loc["latitude"], loc["longitude"]) for loc in story["locations"]]
    if len(coordinates) > 1:
        for i in range(len(coordinates) - 1):
            arc = great_circle_arc(*coordinates[i], *coordinates[i+1])
            folium.PolyLine(
                locations=arc,
                color="blue",
                weight=2.5,
                opacity=0.7,
                dash_array="5, 5"
            ).add_to(m)
    
    for idx, loc in enumerate(story["locations"], start=1):
        folium.Marker(
            [loc["latitude"], loc["longitude"]],
            popup=f"{story['title']}\n📍 {loc['location']} ({loc['year']})",
            tooltip=f"{story['title']} - Stage {idx}"
        ).add_to(marker_cluster)

folium_static(m)




