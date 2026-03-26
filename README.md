 Fake Website Detector (Machine Learning)
 
 Overview
The Fake Website Detector is a machine learning-based project that analyzes URLs and determines whether a website is SAFE or FAKE (phishing/suspicious).
This project is designed to promote digital literacy and cybersecurity awareness by helping users identify potentially harmful websites.
________________________________________

Features
•	Detects fake and safe websites using Machine Learning
•	Uses URL-based feature extraction
•	Provides prediction with confidence score
•	Simple command-line interface
•	Beginner-friendly and easy to run
________________________________________

How It Works
1.	Feature Extraction
o	Checks HTTPS usage
o	URL length
o	Presence of @, -, and multiple dots
o	Detects IP-based URLs
o	Identifies suspicious keywords (login, verify, free, etc.)
2.	Model Training
o	Uses Random Forest Classifier
o	Trained on a dataset of safe and fake URLs
3.	Prediction
o	User inputs a URL
o	Model analyzes features
o	Outputs:
	 SAFE
	 FAKE
o	Also shows confidence percentage
________________________________________

Technologies Used
•	Python
•	Pandas
•	Scikit-learn
•	Regular Expressions (re)
________________________________________

Installation
1.	Clone the repository or download the code
2.	Install dependencies:
pip install pandas scikit-learn
3.	Run the program:
python fake_website_detector.py
________________________________________

Usage
After running the program:
Enter URL (or exit): http://free-money-login.com  
Result: FAKE (92.5%)
________________________________________

Example
URL	Result
https://www.google.com
SAFE
http://win-free-prize.com
FAKE
________________________________________

Advantages
•	Fast and automated detection
•	Easy to understand and implement
•	Useful for cybersecurity awareness
•	Can be extended into real-world applications
________________________________________

Limitations
•	Uses a small dataset (limited accuracy)
•	Does not check real-time website data
•	Cannot detect advanced phishing techniques
________________________________________

Future Improvements
•	Use large real-world datasets (Kaggle)
•	Add domain age and SSL certificate checks
•	Build a web app using Streamlit
•	Integrate real-time URL scanning
•	Improve accuracy with advanced models
________________________________________

Project Structure
fake-website-detector/
│── fake_website_detector.py
│── README.md
________________________________________

Author
Munmun Ghosh
25BET10009



