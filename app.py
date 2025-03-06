


import streamlit as st
import re
import random
import string
from time import sleep

# Common weak passwords to blacklist
WEAK_PASSWORDS = ["password", "123456", "password123", "qwerty", "admin", "letmein"]

# Function to generate a strong password
def generate_strong_password(length=12):
    # Ensure at least one character from each category
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    # Fill the rest with random characters
    remaining_length = length - 4
    characters = string.ascii_letters + string.digits + string.punctuation
    remaining = ''.join(random.choice(characters) for _ in range(remaining_length))

    # Combine all parts and shuffle
    password = lowercase + uppercase + digit + special + remaining
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

# Function to check if password is blacklisted
def is_password_blacklisted(password):
    return password.lower() in WEAK_PASSWORDS

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        strength = "Strong Password!"
    elif score == 3:
        strength = "Moderate Password - Consider adding more security features."
    else:
        strength = "Weak Password - Improve it using the suggestions above."

    return strength, feedback, score

# Custom CSS styles
st.markdown("""
<style>
    /* Style for weak password feedback points */
    .feedback-item {
        margin: 10px 0;
        padding: 12px;
        border-radius: 8px;
        background-color: #fff3f3;
        border-left: 4px solid #ff4b4b;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        font-size: 14px;
        color: #333;
    }
    
    /* Style for the password generator button */
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        border: none;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s ease;
        width: 100%;
    }
              .sub-heading {
        font-size: 20px;
        color: #3498db;
        margin-top: -10px;
        margin-bottom: 20px;
    }
            
    
    .stButton > button:hover {
        background-color: #45a049;
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div {
        background-color: #4CAF50;
    }
    .weak-password > div > div > div {
        background-color: #ff4b4b;
    }
</style>
""", unsafe_allow_html=True)

# Streamlit App
def main():
    # Sidebar for additional information (kept as it is)
    st.sidebar.title("🔒 Password Strength Meter")

    st.sidebar.markdown("---")


    # About This Project
    with st.sidebar.expander("🌟 **About This Project**", expanded=True):
        st.write("This project is a **Password Strength Meter** that evaluates the strength of a user's password based on security rules. It also includes a **Password Generator** to create strong passwords and a **Blacklist Feature** to reject common weak passwords.")
        st.markdown("**Key Features:**")
        st.write("- 🛠️ Password Strength Check")
        st.write("- 🎲 Password Generator")
        st.write("- 🚫 Blacklist Common Passwords")
        st.write("- 🎨 User-Friendly Interface")

    # Password Strength Criteria
    with st.sidebar.expander("📝 **Password Strength Criteria**", expanded=False):
        st.write("A strong password must meet the following criteria:")
        st.write("- ✅ Be at least 8 characters long")
        st.write("- ✅ Contain both uppercase and lowercase letters")
        st.write("- ✅ Include at least one digit (0-9)")
        st.write("- ✅ Have one special character (!@#$%^&*)")

    # Scoring System
    with st.sidebar.expander("📊 **Scoring System**", expanded=False):
        st.write("Passwords are scored based on the following rules:")
        st.write("- 🟢 **Strong (Score: 4)**: Meets all criteria")
        st.write("- 🟡 **Moderate (Score: 3)**: Good but missing some security features")
        st.write("- 🔴 **Weak (Score: 0-2)**: Short or missing key elements")

    # Feedback System
    with st.sidebar.expander("💡 **Feedback System**", expanded=False):
        st.write("The app provides feedback to help users improve their passwords:")
        st.write("- If the password is **weak**, it suggests improvements.")
        st.write("- If the password is **strong**, it displays a success message.")

    # Main UI
    st.title("🔐 Password Strength Meter")
    st.markdown('<div class="sub-heading">Your Knowledgeable Guide to Creating Strong and Secure Passwords</div>', unsafe_allow_html=True)
    st.write("Welcome to the **Password Strength Meter**! Enter your password below to check its strength or generate a strong password.")

    # Password input
    password = st.text_input("Enter Password", type="password", key="password_input", value="")

    # Check password strength when input is provided
    if password:
        # Check if password is blacklisted
        if is_password_blacklisted(password):
            st.error("🚫 This password is too common and weak. Please choose a stronger password.")
            st.progress(0)
        else:
            # Check password strength
            strength, feedback, score = check_password_strength(password)
            
            # Progress bar with color based on strength
            progress_value = score / 4
            progress_bar = st.progress(progress_value)
            if score == 4:
                progress_bar.progress(1.0)
                st.success(f"**Password Strength:** {strength}")
                st.balloons()
            elif score == 3:
                progress_bar.progress(0.75)
                st.warning(f"**Password Strength:** {strength}")
            else:
                progress_bar.progress(0.5)
                st.error(f"**Password Strength:** {strength}")
                # Add custom class for weak password progress bar
                st.markdown("<style>.stProgress > div > div > div {background-color: #ff4b4b !important;}</style>", unsafe_allow_html=True)

            # Display feedback with styled bullet points
            if feedback:
                st.markdown("📝 **Consider the following improvements:**")
                for item in feedback:
                    st.markdown(f"""
                    <div class="feedback-item">
                        • {item}
                    </div>
                    """, unsafe_allow_html=True)

    # Password Generator with styled button
    st.markdown("### 🛠️ Generate Strong Password")
    if st.button("✨ Generate Strong Password"):
        strong_password = generate_strong_password()
        st.success(f"**Generated Strong Password:** `{strong_password}`")
        st.balloons()

# Run the app
if __name__ == "__main__":
    main()





# import streamlit as st
# import re
# import random
# import string

# # Common weak passwords to blacklist
# WEAK_PASSWORDS = ["password", "123456", "password123", "qwerty", "admin", "letmein"]

# # Function to generate a strong password
# def generate_strong_password(length=12):
#     # Ensure at least one character from each category
#     lowercase = random.choice(string.ascii_lowercase)  # one lowercase letter
#     uppercase = random.choice(string.ascii_uppercase)  # one uppercase letter
#     digit = random.choice(string.digits)               # one digit
#     special = random.choice(string.punctuation)        # one special character

#     # Fill the rest with random characters
#     remaining_length = length - 4
#     characters = string.ascii_letters + string.digits + string.punctuation
#     remaining = ''.join(random.choice(characters) for _ in range(remaining_length))

#     # Combine all parts and shuffle to ensure randomness
#     password = lowercase + uppercase + digit + special + remaining
#     password_list = list(password)
#     random.shuffle(password_list)
#     return ''.join(password_list)

# # Function to check if password is blacklisted
# def is_password_blacklisted(password):
#     return password.lower() in WEAK_PASSWORDS

# # Function to check password strength
# def check_password_strength(password):
#     score = 0
#     feedback = []

#     # Length Check
#     if len(password) >= 8:
#         score += 1
#     else:
#         feedback.append("❌ Password should be at least 8 characters long.")

#     # Upper & Lowercase Check
#     if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
#         score += 1
#     else:
#         feedback.append("❌ Include both uppercase and lowercase letters.")

#     # Digit Check
#     if re.search(r"\d", password):
#         score += 1
#     else:
#         feedback.append("❌ Add at least one number (0-9).")

#     # Special Character Check
#     if re.search(r"[!@#$%^&*]", password):
#         score += 1
#     else:
#         feedback.append("❌ Include at least one special character (!@#$%^&*).")

#     # Strength Rating
#     if score == 4:
#         strength = "✅ Strong Password!"
#     elif score == 3:
#         strength = "⚠️ Moderate Password - Consider adding more security features."
#     else:
#         strength = "❌ Weak Password - Improve it using the suggestions above."

#     return strength, feedback

# # Streamlit App
# def main():
#     # Sidebar for additional information
#     st.sidebar.title("🔒 Password Strength Meter")
#     st.sidebar.markdown("---")

#     # About This Project
#     with st.sidebar.expander("🌟 **About This Project**", expanded=True):
#         st.write("This project is a **Password Strength Meter** that evaluates the strength of a user's password based on security rules. It also includes a **Password Generator** to create strong passwords and a **Blacklist Feature** to reject common weak passwords.")
#         st.markdown("**Key Features:**")
#         st.write("- 🛠️ Password Strength Check")
#         st.write("- 🎲 Password Generator")
#         st.write("- 🚫 Blacklist Common Passwords")
#         st.write("- 🎨 User-Friendly Interface")

#     # Password Strength Criteria
#     with st.sidebar.expander("📝 **Password Strength Criteria**", expanded=False):
#         st.write("A strong password must meet the following criteria:")
#         st.write("- ✅ Be at least 8 characters long")
#         st.write("- ✅ Contain both uppercase and lowercase letters")
#         st.write("- ✅ Include at least one digit (0-9)")
#         st.write("- ✅ Have one special character (!@#$%^&*)")

#     # Scoring System
#     with st.sidebar.expander("📊 **Scoring System**", expanded=False):
#         st.write("Passwords are scored based on the following rules:")
#         st.write("- 🟢 **Strong (Score: 4)**: Meets all criteria")
#         st.write("- 🟡 **Moderate (Score: 3)**: Good but missing some security features")
#         st.write("- 🔴 **Weak (Score: 0-2)**: Short or missing key elements")

#     # Feedback System
#     with st.sidebar.expander("💡 **Feedback System**", expanded=False):
#         st.write("The app provides feedback to help users improve their passwords:")
#         st.write("- If the password is **weak**, it suggests improvements.")
#         st.write("- If the password is **strong**, it displays a success message.")

#     # Main UI
#     st.title("🔐 Password Strength Meter")
#     st.write("Welcome to the **Password Strength Meter**! Enter your password below to check its strength or generate a strong password.")

#     # Initialize session state for input field
#     if "clear_input" not in st.session_state:
#         st.session_state.clear_input = False

#     # Password input
#     password = st.text_input("Enter Password", type="password", key="password_input", value="")

#     # Clear input field if flag is set
#     if st.session_state.clear_input:
#         st.session_state.clear_input = False
#         st.rerun()  # Use st.rerun() to refresh the app

#     # Check password strength when input is provided
#     if password:
#         # Check if password is blacklisted
#         if is_password_blacklisted(password):
#             st.error("🚫 This password is too common and weak. Please choose a stronger password.")
#         else:
#             # Check password strength
#             strength, feedback = check_password_strength(password)

#             # Display strength
#             st.write(f"**Password Strength:** {strength}")

#             # Display feedback
#             if feedback:
#                 st.warning("📝 Consider the following improvements:")
#                 for item in feedback:
#                     st.write(item)

#         # Set flag to clear input field
#         st.session_state.clear_input = True

#     # Password Generator
#     st.markdown("### 🛠️ Generate Strong Password")
#     if st.button("✨ Generate Strong Password", help="Click to generate a strong password"):
#         strong_password = generate_strong_password()
#         st.write(f"**Generated Strong Password:** `{strong_password}`")

# # Run the app
# if __name__ == "__main__":
#     main()



