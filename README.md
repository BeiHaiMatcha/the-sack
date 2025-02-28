The Sack: A Digital Archive of Women’s Stories

About The Sack

The Sack is a digital humanities project dedicated to preserving the stories of objects carried by women across generations. Inspired by Tiya Miles’s book All That She Carried, this archive seeks to document personal artifacts and their journeys, offering a space for memory, history, and storytelling.

The project is named after Ashley’s Sack, a simple cloth bag given by an enslaved mother, Rose, to her daughter Ashley before they were forcibly separated. It contained a tattered dress, three handfuls of pecans, and a lock of hair—items chosen with care and love in the face of an uncertain future. Decades later, Ashley’s descendant, Ruth Middleton, embroidered its story onto the fabric, transforming it into a powerful testament to love, resilience, and historical survival.

The Sack continues this tradition by allowing individuals to share the personal objects that carry their own histories—whether it be a letter, a piece of jewelry, or a worn-out suitcase. Each object tells a story of migration, inheritance, memory, or resistance.

Features

1. Submit Stories
	•	Users can upload their object’s story, including its significance, history, and meaning.
	•	Submissions include a title, description, location, and tags for categorization.
	•	Users can also upload an image of the object.

2. Explore Objects on a Map
	•	View stories geographically, seeing where different objects originated and how they moved over time.
	•	Objects can be filtered by location, time period, and theme.

3. Trace Object Journeys Over Time
	•	Users can document multiple locations where an object has traveled, creating a timeline of its movement.
	•	A flight path visualization connects these locations, visually tracing an object’s history.

4. Search & Categorization
	•	Users can filter stories by themes such as migration, war & displacement, motherhood, inheritance, and resistance.
	•	Tags help users discover similar stories across different geographies and time periods.

Technology Stack
	•	Frontend: Streamlit (for UI & interactivity)
	•	Backend: Firebase Firestore (for data storage)
	•	Storage: Firebase Storage (for images)
	•	Geospatial Mapping: Folium & st_folium
	•	AI Assistance (Future Implementation): NLP-based text analysis for story summarization

Installation & Setup

1. Clone the Repository

git clone https://github.com/your-username/the-sack.git
cd the-sack

2. Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Configure Firebase Credentials
	•	Create a .streamlit/secrets.toml file in the root directory.
	•	Copy and paste your Firebase credentials into this file:

[FIREBASE_CREDENTIALS]
type = "service_account"
project_id = "the-sack"
private_key_id = "your-private-key-id"
private_key = "your-private-key"
client_email = "your-client-email"
client_id = "your-client-id"

5. Run the Application

streamlit run app.py

How to Contribute

We welcome contributions! Here’s how you can help:
	•	Add new features: Submit a pull request with improvements.
	•	Report bugs: Open an issue with a detailed description.
	•	Suggest stories: If you know of historical objects with powerful stories, submit them to the archive.

To Contribute Code
	1.	Fork the repository.
	2.	Create a feature branch (git checkout -b feature-name).
	3.	Commit your changes (git commit -m "Add new feature").
	4.	Push to your branch (git push origin feature-name).
	5.	Open a pull request.

License

The Sack is an open-source project licensed under the MIT License.

Why This Matters

This project is not just about objects—it’s about the people, histories, and emotions tied to them. The Sack aims to preserve and share these voices, making history personal and tangible. We believe that by telling these stories, we honor those who carried them before us.

Join us in building this archive. Share a story. Explore the past. Preserve the future.
