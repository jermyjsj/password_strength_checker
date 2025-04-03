# 🔐 Password Strength Checker (Beginner Edition)

This is a simple Python project I made to check how strong a password is. The program looks at different parts of the password (like length, uppercase/lowercase letters, numbers, and special characters) and gives it a score out of 7.

It keeps asking the user to enter a password until it’s considered strong (score of 6 or 7). The script is written in a beginner-friendly way with easy-to-understand logic and comments.

---

## ✅ What It Checks For

- Password length (8+ or 12+ characters)
- At least one uppercase letter (A–Z)
- At least one lowercase letter (a–z)
- At least one number (0–9)
- At least one special character (!@#$ etc)
- Whether it’s a common password (optional check using a file)

---

## 💡 How To Use

1. Clone or download the project folder.
2. (Optional) Add a `common_passwords.txt` file in the same folder.
3. Open the project in [GitHub Codespaces](https://github.com/features/codespaces) or run the script locally.
4. Run the program:

```bash
python password_checker.py
