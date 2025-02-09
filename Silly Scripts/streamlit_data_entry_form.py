# IMPORTANT: Run script from the terminal by pasting this command (remove hash symbol):
# streamlit run streamlit_data_entry_form.py --logger.level warning
# ---
# Script Explained:
# - Streamlit web app with data entry form (text, number, dropdown, checkbox, slider)
# - Saves entries to Excel using pandas - appends to data.xlsx or creates new file
# - Validates required fields and email format before saving
# - Auto-clears form on success with confirmation message

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import streamlit as st
import pandas as pd

def save_to_excel(data):
    """Saves data to Excel file, appending to existing data if available"""
    try:
        existing_df = pd.read_excel("data.xlsx")
        updated_df = pd.concat([existing_df, pd.DataFrame([data])], ignore_index=True)
    except FileNotFoundError:
        updated_df = pd.DataFrame([data])
    
    updated_df.to_excel("data.xlsx", index=False)

# Main form structure
st.set_option('client.showErrorDetails', False)
st.title("📝 Data Entry Form")
st.markdown("*Required fields are marked with an asterisk*")

with st.form("data_form"):
    name = st.text_input("Full Name*", key="name")
    age = st.number_input("Age", min_value=1, max_value=100, value=18, key="age")
    gender = st.selectbox("Gender", ["", "Male", "Female", "Other"], key="gender")
    email = st.text_input("Email*", key="email")
    subscription = st.checkbox("Subscribe to newsletter", key="subscription")
    satisfaction = st.slider("Satisfaction Level (0-100)", 0, 100, 50, key="satisfaction")
    comments = st.text_area("Comments", key="comments")

    # Form submission
    submitted = st.form_submit_button("Submit Entry")
    
    if submitted:
        # Validation
        errors = []
        if not name.strip():
            errors.append("Name is required")
        if not email.strip() or "@" not in email:
            errors.append("Valid email address is required")
        
        # Handle submission
        if errors:
            for error in errors:
                st.error(error)
        else:
            try:
                # Create data entry
                entry = {
                    "Name": name.strip(),
                    "Age": age,
                    "Gender": gender,
                    "Email": email.strip(),
                    "Subscription": int(subscription),  # Convert to 0/1 like Excel format
                    "Satisfaction": satisfaction,
                    "Comments": comments.strip()
                }
                
                save_to_excel(entry)
                st.success("✅ Entry saved successfully!")
                
                # Clear form inputs
                for key in ["name", "email", "comments"]:
                    st.session_state[key] = ""
                st.session_state.age = 18
                st.session_state.gender = ""
                st.session_state.subscription = False
                st.session_state.satisfaction = 50
                
            except Exception as e:
                st.error(f"❌ Error saving data: {str(e)}")