# ANY PROBLEMS FIX YOURSELF

# AdvancedCTFChallenge

## Overview

Welcome to the AdvancedCTFChallenge! This is a multi-step web application Capture The Flag (CTF) challenge designed to test your cybersecurity skills. Your objective is to find the final flag by completing the following steps:

1. Find an exposed file.
2. Decode the hidden message.
3. Exploit a vulnerability to gain access to the restricted area.
4. Solve a cryptographic puzzle to retrieve the final flag.

## Instructions

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```sh
git clone https://github.com/yourusername/AdvancedCTFChallenge.git
cd AdvancedCTFChallenge

Step 2: Install Dependencies
Ensure you have Python installed, then install the necessary dependencies:

pip install -r requirements.txt

Step 3: Run the Web Application
Run the web application:

python app.py

Open your browser and go to http://127.0.0.1:5000.

Step 4: Find the Final Flag
Follow the steps outlined in the overview to find the final flag.

Project Structure

AdvancedCTFChallenge/
├── app.py
├── templates/
│   ├── index.html
│   ├── admin.html
│   ├── secret.html
├── static/
│   ├── style.css
├── hidden/
│   ├── hidden_message.txt
├── utils/
│   ├── cipher.py
├── flag.txt
├── README.md
├── requirements.txt

Hints
Step 1: Check for exposed files using directory brute-forcing tools.
Step 2: Decode the hidden message using the provided decode function.
Step 3: Look for vulnerabilities in the admin login form.
Step 4: Combine clues and use cryptographic methods to solve the puzzle.

Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.


### Example Usage

1. **Find the exposed file:**
   - Visit the `/admin` page.
   - Use a directory brute-forcing tool (like `dirb` or `gobuster`) to discover the `/hidden/hidden_message.txt` file.

2. **Decode the hidden message:**
   - The content of the `hidden_message.txt` is encrypted with a Fernet key.
   - The key is generated within the `utils/cipher.py` file. Extract the key and use it to decode the message using the provided decode function.

3. **Exploit the vulnerability:**
   - Use a simple SQL injection or brute-force attack on the admin login form to get access to the `/secret` page.

4. **Solve the cryptographic puzzle:**
   - The decoded message from the `hidden_message.txt` provides a clue or a partial flag. Combine it with the contents of the `secret.html` to retrieve the final flag: `CTF{multi_step_web_exploitation_flag}`.

Feel free to expand this challenge further with additional layers of complexity and security concepts!
