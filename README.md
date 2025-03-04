# Password Strength Meter 🔒

Welcome to the **Password Strength Meter** project! This is a Python-based application built with **Streamlit** that evaluates the strength of a user's password based on predefined security rules. It also includes a **Password Generator** to create strong passwords and a **Blacklist Feature** to reject common weak passwords.

---

## 🌟 Features

- **Password Strength Check**: Evaluates your password based on length, character types, and patterns.
- **Password Generator**: Creates a strong password that meets all security criteria.
- **Blacklist Common Passwords**: Rejects weak passwords like `password123`, `qwerty`, etc.
- **User-Friendly Interface**: Clean and intuitive design for easy use.

---

## 📝 Requirements

A strong password must meet the following criteria:
- ✅ Be at least **8 characters long**.
- ✅ Contain both **uppercase and lowercase letters**.
- ✅ Include at least **one digit (0-9)**.
- ✅ Have **one special character** (`!@#$%^&*`).

---

## 📊 Scoring System

Passwords are scored based on the following rules:
- 🟢 **Strong (Score: 4)**: Meets all criteria.
- 🟡 **Moderate (Score: 3)**: Good but missing some security features.
- 🔴 **Weak (Score: 0-2)**: Short or missing key elements.

---

## 💡 Feedback System

The app provides feedback to help users improve their passwords:
- If the password is **weak**, it suggests improvements.
- If the password is **strong**, it displays a success message.

---

## 🚀 How to Use

1. **Enter Password**:
   - Type a password in the input field and press Enter.
   - The app will evaluate the password and display its strength along with feedback.

2. **Generate Strong Password**:
   - Click the **✨ Generate Strong Password** button to get a strong password suggestion.
   - Copy the generated password and use it for your accounts.

3. **Check Password Strength**:
   - If the password is weak or moderate, the app will suggest improvements.
   - If the password is strong, the app will display a success message.

---

## 🛠️ Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Asia-parveen/password-strength-meter.git
   cd password-strength-meter
