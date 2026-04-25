# 📸 SnapClass - Making Attendance Faster using AI

SnapClass is an AI-powered attendance management system built with Streamlit. It modernizes the traditional classroom attendance process by utilizing advanced **Facial Recognition** and **Voice Biometrics**. Teachers can instantly take attendance by uploading classroom photos or recording audio, while students can log in and register using their FaceID.

## ✨ Features

### 👨‍🏫 For Teachers
* **Secure Login/Registration**: Password-protected dashboard with hashed passwords.
* **Manage Subjects**: Create and manage different classes/sections easily.
* **Easy Sharing & Enrollment**: Generate QR codes and sharing links for instant student enrollment.
* **AI Face Attendance**: Upload single or multiple classroom photos. The AI deeply scans the photos, matches faces with enrolled students, and automatically marks them present.
* **AI Voice Attendance**: Upload or record a classroom audio clip. The system identifies students by their unique voice profiles to mark attendance.
* **Detailed Records**: View auto-generated attendance reports, including total students present and historical attendance data.

### 🎓 For Students
* **FaceID Login**: Frictionless login using just the webcam—no passwords required!
* **Biometric Registration**: Seamlessly register by capturing your facial structure and recording a short voice phrase.
* **Subject Dashboard**: Track total classes and your personal attendance stats.
* **Quick Enroll**: Join classes instantly using a subject code or scanning a teacher's QR link.

## 🛠️ Tech Stack

* **Frontend/Framework**: [Streamlit](https://streamlit.io/)
* **Database**: [Supabase](https://supabase.com/) (PostgreSQL)
* **Face Recognition**: `dlib`, `face_recognition`, `scikit-learn` (SVM Classifier)
* **Voice Recognition**: `resemblyzer`, `librosa`
* **Styling**: Custom CSS injected via Streamlit
* **Security**: `bcrypt` (for teacher passwords)
* **Utilities**: `pandas`, `numpy`, `pillow`, `segno` (for QR codes)

## ⚙️ Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.10+ installed.
* A [Supabase](https://supabase.com/) account and a newly created project.
* Basic understanding of Streamlit and Python virtual environments.

## 🚀 Installation & Setup

**1. Clone the repository**
```bash
git clone [https://github.com/yourusername/SnapClass.git](https://github.com/yourusername/SnapClass.git)
cd SnapClass
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Setup Environment Variables**
SnapClass uses Supabase for database management. You need to provide your Supabase URL and API Key.

Create a .streamlit folder in the root directory and add a secrets.toml file:

```bash
mkdir .streamlit
touch .streamlit/secrets.toml
```
Add your Supabase credentials to secrets.toml:

Ini, TOML
```bash
SUPABASE_URL = "your-supabase-project-url"
SUPABASE_KEY = "your-supabase-anon-key"
```

## 🗄️ Database Schema Setup (Supabase)
To run this app, your Supabase database will need the following tables (based on the queries in src/database/db.py):

* `teachers`: `teacher_id` (UUID/Int), `username`, `password`, `name`.

* `students`: `student_id` (UUID/Int), `name`, `face_embedding` (array/json), `voice_embedding` (array/json).

* `subjects`: `subject_id` (UUID/Int), `subject_code`, `name`, `section`, `teacher_id` (Foreign Key).

* `subject_students`: `student_id` (Foreign Key), `subject_id` (Foreign Key) - Junction table for enrollments.

* `attendance_logs`: `log_id`, `student_id` (Foreign Key), `subject_id` (Foreign Key), `timestamp`, `is_present` (Boolean).

## 🏃‍♂️ Running the Application
Once your dependencies are installed and secrets are configured, launch the app:

```bash
streamlit run app.py
```
The application will be available in your browser at http://localhost:8501.

## 📁 Project Structure

```text
SnapClass/
│
├── .streamlit/                 # Streamlit configuration & secrets (ignored in git)
├── src/
│   ├── components/             # Reusable UI components and modal dialogs
│   ├── database/               # Supabase configuration and DB wrapper functions
│   ├── pipelines/              # AI pipelines (Face & Voice detection/embeddings)
│   ├── screens/                # Main application screens (Home, Teacher, Student)
│   └── ui/                     # CSS and UI layout styling files
│
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
└── .gitignore                  # Git ignore rules


