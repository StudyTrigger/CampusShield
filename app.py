import os
import streamlit as st
from datetime import datetime, date
from analyser import analyse_message
from storage import (
    initialize_data, load_complaints, save_complaint, update_complaint,
    get_complaint, ensure_upload_dir, DATA_DIR
)
#www.getemoji.com for icons
st.set_page_config(
    page_title="CampusShield | Student Safety",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

initialize_data()
ensure_upload_dir()

def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "styles.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

#session define
if "page" not in st.session_state:
    st.session_state.page="Student"
if "admin_authenticated" not in st.session_state:
    st.session_state.admin_authenticated = False
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None
if "analysis_text" not in st.session_state:
    st.session_state.analysis_text = ""
if "selected_complaint" not in st.session_state:
    st.session_state.selected_complaint = None
if "admin_login_error" not in st.session_state:
    st.session_state.admin_login_error = False
if "nav_choice" not in st.session_state:
    st.session_state.nav_choice = "🎓 Student"
if "complaint_message" not in st.session_state:
    st.session_state["complaint_message"] = ""

def change_page():
    st.session_state.page=st.session_state.nav_choice  #student, admin

def logout_admin():
    st.session_state.admin_authenticated=False
    st.session_state.page="Student"
    st.session_state.nav_choice="Student"
    st.session_state.selected_complaint=None

def header():
    left, navigation, logout_col = st.columns([4.5, 3.2, 1],vertical_alignment="center")

    with left:
        st.markdown("""
        <div class="brand-wrap">
            <div class="brand-shield">🛡️</div>
            <div>
                <div class="brand-name">Campus<span>Shield</span></div>
                <div class="brand-subtitle">
                    Sextortion &amp; Online Blackmail Analyzer
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with navigation:
        selected_page = st.segmented_control(
            "Main navigation",
            options=["🎓 Student", "🔒 Admin"],
            key="nav_choice",
            label_visibility="collapsed",
            width="stretch",
        )

        if selected_page is not None:
            new_page = (
                "Student"
                if selected_page == "🎓 Student"
                else "Admin"
            )

            if st.session_state.page != new_page:
                st.session_state.page = new_page
                st.rerun()

    with logout_col:
        if st.session_state.admin_authenticated:
            st.button(
                "Logout",
                use_container_width=True,
                on_click=logout_admin
            )

    st.markdown(
        '<div class="header-rule"></div>',
        unsafe_allow_html=True
    )

def risk_badge(risk):
    return {"High": "🔴 High", "Medium": "🟠 Medium", "Low": "🟢 Low"}.get(risk, risk)

def render_analysis(result):
    risk = result["risk_level"]
    st.markdown('<div class="section-title">📊 Analysis Result</div>', unsafe_allow_html=True)

    if risk == "High":
        st.error(f"**HIGH RISK INDICATORS FOUND** · Score: {result['score']}/100")
    elif risk == "Medium":
        st.warning(f"**SUSPICIOUS INDICATORS FOUND** · Score: {result['score']}/100")
    else:
        st.success(f"**FEWER RISK INDICATORS FOUND** · Score: {result['score']}/100")

    st.progress(result["score"] / 100)

    st.caption("This is a preliminary text-based assessment, not proof of a crime or a determination of the sender's identity.")
    if result["indicators"]:
        st.markdown("**Detected indicators**")
        st.markdown(" ".join([f"`{x}`" for x in result["indicators"]]))
    else:
        st.info("No configured warning indicators were detected. A low score does not mean a message is safe.")
    
    st.markdown("**Why was it flagged?**")
    
    for reason in result["reasons"]:
        st.markdown(f"- {reason}")
    st.markdown("**Suggested next steps**")
    
    for tip in result["guidance"]:
        st.markdown(f"- {tip}")

def message_box(title, subtitle, eyebrow="STUDENT SAFETY"):
    st.markdown(f"""
    <div class="hero">
      <div class="hero-copy">
        <div class="eyebrow">{eyebrow}</div>
        <h1>{title}</h1>
        <p>{subtitle}</p>
      </div>
      <div class="hero-note"><div class="hero-note-icon">💡</div>
        <div><b>You are not alone</b><p>If someone is threatening to share private images or is blackmailing you, preserve the evidence and seek help.</p></div>
      </div>
    </div>""", unsafe_allow_html=True)

def student_page():
    message_box(
        "Student Portal",
        "Analyze a suspicious message and, if you choose, register a confidential college complaint.",
        "SEXTORTION & ONLINE BLACKMAIL SUPPORT"
    )
    st.markdown('<div class="section-heading">'
    '<span class="step-number">1</span>'
    '<div><h2>Message Analyzer</h2><p>Paste the message to check for common sextortion and blackmail indicators.</p></div>'
    '</div>', unsafe_allow_html=True)

    analyzer_left, analyzer_right = st.columns([1.08, 0.92], gap="large")

    with analyzer_left:
        
        message = st.text_area(
            "Suspicious message",
            key="analyzer_message",
            height=160,
            placeholder="Paste the suspicious message here…",
            help="Use fictional text for demos. Avoid sharing unnecessary sensitive information."
        )

        if st.button("🔍 Analyze Message", type="primary", use_container_width=True):
            if not message.strip():
                st.warning("Please enter a message to analyze.")
            else:
                st.session_state.analysis_result = analyse_message(message)
                st.session_state.analysis_text = message
        
        if st.session_state.analysis_result and st.session_state.analysis_text:
            if st.button("↘ Use this message in complaint form", use_container_width=True):
                st.session_state["complaint_message"] = st.session_state.analysis_text
                st.rerun()

    with analyzer_right:
        if st.session_state.analysis_result:
            render_analysis(st.session_state.analysis_result)
        else:
            st.markdown("""
            <div class="empty-analysis">
              <div class="empty-icon">🔎</div><h3>Your analysis will appear here</h3>
              <p>The analyzer checks for patterns such as threats to expose private content, 
              payment demands, coercion, and time pressure.</p>
              <div class="mini-pill">Private content threats</div>
              <div class="mini-pill">Payment demands</div><div class="mini-pill">Intimidation</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown('<div class="section-heading"><span class="step-number">2</span>'
    '<div><h2>Register a Complaint</h2>'
    '<p>You can submit a complaint even if you did not analyze the message first.</p></div></div>', unsafe_allow_html=True)
    
    with st.form("complaint_form", clear_on_submit=False):
        form_left, form_right = st.columns([1.15, 0.85], gap="large")
        
        with form_left:
            c1, c2 = st.columns(2)
            with c1:
                student_name = st.text_input("Your name (optional)", placeholder="Name or preferred name")
                sender = st.text_input("Sender phone / username / account *", placeholder="Phone number, username, or account")
            with c2:
                department = st.selectbox("Department / course (optional)", 
                                          ["Prefer not to say", "BCA", "B.Tech", "B.Sc.", "B.Com.", "BA", "MCA", "Other"])
                incident_date = st.date_input("Incident date", value=date.today(), max_value=date.today())
            
            complaint_message = st.text_area(
                "Message content *",
                key="complaint_message",
                height=120,
                placeholder="Paste or summarize the message…"
            )

            category = st.selectbox("Complaint category", [
                "Sextortion / threat to share private content",
                "Online blackmail / extortion",
                "Threats or harassment",
                "Fake profile / impersonation",
                "Suspicious link or scam",
                "Other related concern",
            ])

            screenshot = st.file_uploader(
                "Screenshot (optional)",
                type=["png", "jpg", "jpeg"],
                help="PNG/JPG/JPEG, up to 5 MB. Avoid uploading unrelated private information."
            )

            description = st.text_area("Additional details (optional)", height=90, 
                                       placeholder="When did it happen? Has the sender contacted you repeatedly?")
        with form_right:
            st.markdown("""
            <div class="info-card next-card">
              <h3>🧭 What happens next?</h3>
              <ol><li>Your complaint receives a unique ID.</li>
              <li>The college admin reviews the information.</li>
              <li>Admin may record follow-up actions or request more details.</li>
              <li>You can keep the complaint ID for your records.</li></ol>
            </div>
            <div class="info-card caution-card">
              <h3>⚠ Important information</h3>
              <ul><li>Keep the original messages and screenshots if safe to do so.</li>
              <li>Do not pay or send more private content in response to threats.</li>
              <li>This demo does not file a police or cybercrime complaint.</li>
              <li>If you are in immediate danger, contact local emergency services or a trusted person.</li></ul>
            </div>""", unsafe_allow_html=True)
            
            st.caption("Your complaint details are stored locally by this demo. Do not enter real sensitive data in a publicly deployed demo.")
        
        submitted = st.form_submit_button("📨 Submit Complaint", type="primary", use_container_width=True)
        if submitted:
            errors = []
            if not sender.strip():
                errors.append("Enter the sender's phone number, username, or account.")
            if not complaint_message.strip():
                errors.append("Enter the message content or a description of the message.")
            if screenshot is not None and screenshot.size > 5 * 1024 * 1024:
                errors.append("Screenshot must be 5 MB or smaller.")
            if errors:
                for e in errors:
                    st.error(e)
            else:
                result = analyse_message(complaint_message)
                saved_path = ""
                if screenshot is not None:
                    # Keep the upload name generated by the app, not a user-controlled path.
                    import uuid
                    ext = os.path.splitext(screenshot.name)[1].lower()
                    saved_path = os.path.join("uploads", f"{uuid.uuid4().hex}{ext}")
                    with open(os.path.join(os.path.dirname(__file__), saved_path), "wb") as out:
                        out.write(screenshot.getbuffer())

                complaint_id = save_complaint({
                    "submitted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "student_name": student_name.strip(),
                    "department": department,
                    "sender": sender.strip(),
                    "incident_date": incident_date.strftime("%Y-%m-%d"),
                    "category": category,
                    "message": complaint_message.strip(),
                    "screenshot_path": saved_path,
                    "description": description.strip(),
                    "risk_score": result["score"],
                    "risk_level": result["risk_level"],
                    "indicators": " | ".join(result["indicators"]),
                    "status": "Open",
                    "admin_notes": "",
                    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                })

                st.session_state["last_submitted_id"] = complaint_id
                st.session_state.analysis_result = None
                st.session_state.analysis_text = ""
                st.success(f"Complaint submitted successfully. Your complaint ID is **{complaint_id}**.")
                st.info("Keep this ID for your records. This is a local demo record, not an official police complaint.")
    if st.session_state.get("last_submitted_id"):
        st.markdown(f'<div class="success-ticket"><b>Last submitted complaint:</b> {st.session_state["last_submitted_id"]}</div>', unsafe_allow_html=True)

def admin_page():
    if not st.session_state.admin_authenticated:

        st.markdown("""
        <div class="login-wrap">
          <div class="login-icon">🔐</div><h1>Admin Access</h1>
          <p>Enter the admin password to review student complaints.</p>
        </div>""", unsafe_allow_html=True)

        with st.form("admin_login"):
            password = st.text_input("Admin password", type="password", placeholder="Enter admin password")
            login = st.form_submit_button("Unlock Admin Dashboard", type="primary", use_container_width=True)
            if login:
                expected = os.getenv("CAMPUSSHIELD_ADMIN_PASSWORD", "")
                try:
                    expected = st.secrets.get("admin_password", expected)
                except Exception:
                    pass
                if not expected:
                    st.error("Admin password is not configured. " \
                    "Set CAMPUSSHIELD_ADMIN_PASSWORD or add admin_password to .streamlit/secrets.toml.")
                
                elif password and password == expected:
                    st.session_state.admin_authenticated = True
                    st.session_state.admin_login_error = False
                    st.rerun()
                else:
                    st.session_state.admin_login_error = True

        if st.session_state.admin_login_error:
            st.error("Incorrect password. Please try again.")
        st.caption("For a local demo, configure a password before running the app. Never commit secrets.toml to a public repository.")
        return

    st.markdown("""
    <div class="hero admin-hero">
      <div class="hero-copy"><div class="eyebrow">CONFIDENTIAL CASE REVIEW</div>
      <h1>Admin Dashboard</h1><p>Review and manage student complaints related to sextortion and online blackmail.</p></div>
      <div class="hero-note"><div class="hero-note-icon">💡</div><div><b>Handle with care</b><p>Limit access to complaint details and treat all reports sensitively. A risk score is not proof.</p></div></div>
    </div>""", unsafe_allow_html=True)

    df = load_complaints()

    total = len(df)
    high = int((df["risk_level"] == "High").sum()) if total else 0
    review = int((df["status"] == "Under Review").sum()) if total else 0
    resolved = int((df["status"] == "Resolved").sum()) if total else 0

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total complaints", total)
    m2.metric("High-risk indicators", high)
    m3.metric("Under review", review)
    m4.metric("Resolved", resolved)

    st.markdown("### 🔎 Filter complaints")
    f1, f2, f3 = st.columns([1.2, 1, 1])
    with f1:
        status_filter = st.selectbox("Status", ["All", "Open", "Under Review", "Resolved"])
    with f2:
        risk_filter = st.selectbox("Risk level", ["All", "High", "Medium", "Low"])
    with f3:
        category_options = ["All"] + sorted(df["category"].dropna().unique().tolist()) if total else ["All"]
        category_filter = st.selectbox("Category", category_options)

    filtered = df.copy()

    if status_filter != "All":
        filtered = filtered[filtered["status"] == status_filter]
    if risk_filter != "All":
        filtered = filtered[filtered["risk_level"] == risk_filter]
    if category_filter != "All":
        filtered = filtered[filtered["category"] == category_filter]

    left, right = st.columns([1.15, 1], gap="large")
    
    with left:
        st.markdown("### 📋 Student Complaints")
        if filtered.empty:
            st.info("No complaints match these filters.")
        else:
            display = filtered[["complaint_id", "incident_date", "student_name", "sender", "category", "risk_level", "status"]].copy()
            display.columns = ["ID", "Incident date", "Student", "Sender / Account", "Category", "Risk", "Status"]
            st.dataframe(display, use_container_width=True, hide_index=True, height=390)
            choices = filtered["complaint_id"].tolist()
            current = st.session_state.selected_complaint
            if current not in choices:
                current = choices[0]
            selected = st.selectbox("Select complaint to review", choices, index=choices.index(current), key="selected_complaint_selector")
            st.session_state.selected_complaint = selected

    with right:
        st.markdown("### 🧾 Complaint Details")
        selected_id = st.session_state.selected_complaint
        selected_row = get_complaint(selected_id) if selected_id else None
        if selected_row is None:
            st.info("Select a complaint to view its details.")
        else:
            st.markdown(f'<div class="case-id">Complaint ID · <b>{selected_row["complaint_id"]}</b></div>', unsafe_allow_html=True)
            d1, d2 = st.columns(2)
            d1.markdown(f"**Student**  \n{selected_row.get('student_name') or 'Not provided'}")
            d2.markdown(f"**Sender / account**  \n{selected_row.get('sender') or 'Not provided'}")
            d1.markdown(f"**Department**  \n{selected_row.get('department') or 'Not provided'}")
            d2.markdown(f"**Incident date**  \n{selected_row.get('incident_date') or 'Not provided'}")
            d1.markdown(f"**Category**  \n{selected_row.get('category') or 'Not provided'}")
            d2.markdown(f"**Risk indicator score**  \n{selected_row.get('risk_score', '0')}/100 · {selected_row.get('risk_level', 'Unknown')}")
            st.markdown("**Message provided by student**")
            st.text_area("Message", value=selected_row.get("message", ""), height=105, disabled=True, key=f"msg_{selected_id}")
            indicators = selected_row.get("indicators", "")
            st.markdown("**Detected indicators**")
            st.write(indicators if indicators else "No configured indicators recorded.")
            desc = selected_row.get("description", "")
            if desc:
                st.markdown("**Additional details**")
                st.write(desc)
            shot = selected_row.get("screenshot_path", "")

            if shot:
                full_path = os.path.join(os.path.dirname(__file__), shot)
                if os.path.isfile(full_path):
                    st.markdown("**Screenshot provided by student**")
                    st.image(full_path, use_container_width=True)
                else:
                    st.caption("Screenshot file is not available in this local demo folder.")
            st.markdown("---")

            with st.form(f"admin_update_{selected_id}"):
                new_status = st.selectbox(
                    "Update status",
                    ["Open", "Under Review", "Resolved"],
                    index=["Open", "Under Review", "Resolved"].index(selected_row.get("status", "Open") if selected_row.get("status", "Open") in ["Open", "Under Review", "Resolved"] else "Open")
                )
                notes = st.text_area("Admin notes / actions taken", value=selected_row.get("admin_notes", ""), height=110)
                save = st.form_submit_button("💾 Save updates", type="primary", use_container_width=True)
                
                if save:
                    update_complaint(selected_id, {
                        "status": new_status,
                        "admin_notes": notes.strip(),
                        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    st.success("Complaint updated.")
                    st.rerun()
    st.caption("Demo limitation: the app stores local CSV records and files. It does not send notifications or submit complaints to police/cybercrime authorities.")



header()
if st.session_state.page == "Student":
    student_page()
else:
    admin_page()

st.markdown('<div class="footer">CampusShield · Educational demo · Protect privacy, preserve evidence, seek trusted support.</div>', unsafe_allow_html=True)
