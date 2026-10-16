# 🛡️ CampusShield – Cybersecurity Project Using Python

🔐 Build a practical **Cybersecurity Awareness Project using Python and Streamlit** to analyze suspicious messages, identify potential online blackmail indicators, and manage complaints through an admin dashboard!

📌 **Part of: Super Sunday Project Series** 🚀  
* 👉 New AI/ML and Python projects every Sunday  
* 👉 Learn by building practical applications  
* 👉 Beginner Friendly + Industry Relevant Concepts  

[**Watch Full Video**](YOUR_YOUTUBE_VIDEO_LINK)

---

# ⭐ Support & Follow

If this project helps you:

* ⭐ Star this repository
* 👨‍💻 Follow me on GitHub for more Python and AI/ML projects
* 📺 Subscribe to [Study Trigger on YouTube](https://www.youtube.com/)
* 🚀 Share this project with your friends

---

# 🎥 Project Overview

**CampusShield** is a cybersecurity awareness application built using **Python and Streamlit**. It focuses on suspicious messages related to online blackmail, sextortion, threats, and harassment.

The application analyzes message text using predefined patterns and rules to identify potential warning indicators.

For example:

📩 A user receives a message threatening to share private photos unless money is paid.

➡️ CampusShield analyzes the message and highlights configured warning indicators.

➡️ The user can register a complaint with the sender's details, message content, incident date, and an optional screenshot.

➡️ An administrator can review submitted complaints, update their status, and add notes.

The project demonstrates how Python can be used to build a simple cybersecurity awareness and complaint management application.

**Note:** This is an educational prototype. Its analysis is not proof of a crime, does not verify a sender's identity, and does not submit official complaints to police or cybercrime authorities.

---

# ✨ Features

## 🔍 Suspicious Message Analyzer

* Enter or paste a suspicious message
* Analyze text using predefined patterns and rules
* Identify possible threats to expose private content
* Detect configured payment demands and intimidation indicators
* Calculate a preliminary risk score and risk category
* Display detected indicators and suggested safety guidance

## 📝 Complaint Registration

* Register complaints related to online blackmail and sextortion
* Enter sender phone number, username, or account details
* Select the incident date and complaint category
* Add the suspicious message and additional details
* Upload an optional screenshot as supporting evidence
* Generate a unique complaint ID
* Validate required fields and screenshot file size

## 🔐 Admin Dashboard

* Access the dashboard using an administrator password
* View registered complaints
* Review complaint details and uploaded screenshots
* Filter complaints by status, risk level, and category
* Update complaint status:
  * Open
  * Under Review
  * Resolved
* Add administrative notes and record follow-up actions

## 📊 Complaint Management

* Store complaint records in CSV format
* Load and update complaint information
* Maintain complaint status and risk assessment details
* Store uploaded screenshots in a local directory
* Generate basic complaint statistics for the dashboard

## 🎨 Streamlit Interface

* Interactive Student Portal
* Message analysis results
* Complaint registration form
* Admin login and dashboard
* Complaint filters and status management
* Custom styling using CSS
* Session state management for navigation and application interactions

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive web application |
| Pandas | CSV data handling and complaint analysis |
| Regular Expressions | Rule-based message pattern matching |
| CSV | Local complaint record storage |
| HTML & CSS | Custom interface styling |
| UUID | Generate unique identifiers for uploaded screenshot filenames |

---

# 📂 Project Structure

```text
CampusShield/
│
├── app.py
│   └── Main Streamlit application
│       ├── Student Portal
│       ├── Message Analyzer interface
│       ├── Complaint Registration
│       └── Admin Dashboard
│
├── analyzer.py
│   └── Message analysis logic
│       ├── Rule-based pattern matching
│       ├── Warning indicator detection
│       └── Risk score calculation
│
├── storage.py
│   └── Complaint storage and file handling
│       ├── Initialize data files
│       ├── Load and save complaints
│       ├── Update complaint records
│       └── Manage upload directories
│
├── styles.css
│   └── Custom styling for the Streamlit interface
│
├── data/
│   └── complaints.csv
│       └── Complaint records
│
├── uploads/
│   └── Uploaded complaint screenshots
│
├── .streamlit/
│   └── secrets.toml.example
│       └── Example administrator password configuration
│
├── requirements.txt
│   └── Required Python packages
│
├── .gitignore
│   └── Files excluded from Git tracking
│
└── README.md
    └── Project documentation
```

**Note:** The `data/` directory, complaint CSV file, and `uploads/` directory may be initialized or populated automatically when the application runs. Their exact contents depend on the project implementation and submitted complaints.

---

# 🚀 Getting Started

## 📌 Prerequisites

Before running this project, install:

* Python 3.10 or a compatible version supported by your installed dependencies
* pip (Python package manager)
* Git (optional, for cloning the repository)

---

# ⚙️ Installation

## 1️⃣ Clone Repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/CampusShield.git
```

Navigate to the project directory:

```bash
cd CampusShield
```

## 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Configure the Admin Password

Create a file named `secrets.toml` inside the `.streamlit` directory.

Your directory should look like this:

```text
.streamlit/
└── secrets.toml
```

Add the following configuration:

```toml
admin_password = "change-this-to-a-strong-password"
```

Alternatively, configure the `CAMPUSSHIELD_ADMIN_PASSWORD` environment variable.

**Important:** Never commit your actual `secrets.toml` file or administrator password to a public GitHub repository.

## 5️⃣ Run the Application

Execute the following command from the project root directory:

```bash
streamlit run app.py
```

Streamlit will provide a local URL, typically:

```text
http://localhost:8501
```

Open the URL in your browser to use CampusShield.

---

# 🖥️ How to Use the Application

## 1. Analyze a Suspicious Message

* Open the Student Portal.
* Paste a suspicious message into the Message Analyzer.
* Click **Analyze Message**.
* Review the detected indicators, preliminary risk score, and suggested guidance.

## 2. Register a Complaint

* Enter the sender's phone number, username, or account details.
* Add the message content and incident date.
* Select a complaint category.
* Upload a screenshot if needed.
* Submit the complaint.
* Save the generated complaint ID for your records.

## 3. Review Complaints as an Administrator

* Open the Admin section.
* Enter the configured administrator password.
* View and filter complaint records.
* Select a complaint to inspect its details.
* Update its status and add administrative notes.
* Save the changes.

---

# 📁 Data Storage

CampusShield uses local files for this educational project.

* **`data/complaints.csv`** stores complaint records.
* **`uploads/`** stores uploaded screenshot files.
* Complaint records include fields such as complaint ID, submission time, sender details, incident date, message, category, risk indicators, status, and administrative notes.

Because data is stored locally, the application does not automatically provide cloud backups, email notifications, or multi-user synchronization.

Avoid using real sensitive personal information in a publicly deployed demonstration.

---

# 🔒 Cybersecurity & Privacy Disclaimer

CampusShield is designed for **educational purposes and cybersecurity awareness**.

* The message analyzer uses predefined rules and patterns, not a trained machine learning model.
* A high risk score does not establish that a crime occurred.
* A low score does not guarantee that a message is safe.
* The application does not verify sender identity or investigate cybercrime.
* Complaint registration is local to this application and is not an official police or cybercrime report.
* Do not upload real private images or sensitive personal information to a public demonstration.
* Use a strong administrator password and protect access to complaint records.

If someone is experiencing blackmail or sextortion, preserve relevant evidence when safe and seek help from a trusted person or appropriate official support service.

---

# 🔮 Future Enhancements

Possible improvements for future versions include:

* 🤖 NLP-based suspicious message classification
* 📈 Advanced complaint analytics and visualizations
* 🔎 Complaint tracking for students
* 🔔 Notifications when complaint status changes
* 🗄️ Database integration using SQLite or PostgreSQL
* 👥 More robust user authentication and authorization
* ☁️ Secure deployment with appropriate access controls

These are potential future improvements and are not necessarily implemented in the current version.

---

# 🎓 Learning Outcomes

By building this project, students can learn:

* Python application development
* Streamlit UI development
* Regular expressions and rule-based text analysis
* Data handling with Pandas
* CSV file storage and management
* File uploads and directory handling
* Session state management in Streamlit
* Basic complaint management workflows
* Cybersecurity awareness and privacy considerations

---

# 📺 Watch the Project Tutorial

Learn how to build CampusShield step by step using Python and Streamlit.

👉 **YouTube Video:** [Add your video link here](YOUR_YOUTUBE_VIDEO_LINK)

---

# ⭐ Support & Follow

If you found this project useful:

* ⭐ Give this repository a star
* 🍴 Fork the repository and experiment with the code
* 👨‍💻 Follow Study Trigger for more programming projects
* 📺 Subscribe to Study Trigger on YouTube
* 💬 Share your suggestions and improvements

---

**Made for learning by Study Trigger** 🚀

*Learn by building. Build to understand.*
