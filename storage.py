import os
import pandas as pd

#set the path
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
DATA_DIR=os.path.join(BASE_DIR,"data")
UPLOAD_DIR=os.path.join(BASE_DIR,"uploads")
CSV_PATH=os.path.join(DATA_DIR,"complaints.csv")

COLUMNS=[
    "complaint_id", "submitted_at", "student_name", "department", "sender",
    "incident_date", "category", "message", "screenshot_path", "description",
    "risk_score", "risk_level", "indicators", "status", "admin_notes", "last_updated"
    ]

def ensure_upload_dir():
    os.makedirs(UPLOAD_DIR,exist_ok=True)

def initialize_data():
    os.makedirs(DATA_DIR, exist_ok=True)
    ensure_upload_dir()
    if not os.path.exists(CSV_PATH):
        pd.DataFrame(columns=COLUMNS).to_csv(CSV_PATH,index=False)

def load_complaints():
    initialize_data()
    try:
        df=pd.read_csv(CSV_PATH, dtype=str, keep_default_na=False)
    except (pd.errors.EmptyDataError, FileNotFoundError):
        df=pd.DataFrame(columns=COLUMNS)

    for col in COLUMNS:
        if col not in df.columns:
            df[col]=""

    return df[COLUMNS].fillna("")

def _next_id(df):
    return f"CS-{len(df)+1:04d}"  #length =>4    CS-0005

def save_complaint(record):
    df = load_complaints()
    complaint_id = _next_id(df)
    row = {col: str(record.get(col, "")) for col in COLUMNS}
    row["complaint_id"] = complaint_id
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df.to_csv(CSV_PATH, index=False, encoding="utf-8")
    return complaint_id

def get_complaint(complaint_id):
    if not complaint_id:
        return None
    df = load_complaints()
    matches = df[df["complaint_id"] == str(complaint_id)]
    if matches.empty:
        return None
    return matches.iloc[0].to_dict()

def update_complaint(complaint_id, updates):
    df = load_complaints()
    mask = df["complaint_id"] == str(complaint_id)
    if not mask.any():
        return False
    for key, value in updates.items():
        if key in COLUMNS:
            df.loc[mask, key] = str(value)
    df.to_csv(CSV_PATH, index=False, encoding="utf-8")
    return True
