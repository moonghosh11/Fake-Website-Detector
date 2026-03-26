import pandas as pd
import re
from urllib.parse import urlparse
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ----------------------------
# 1. Feature Extraction
# ----------------------------
def extract_features(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    features = []

    features.append(1 if url.startswith("https") else 0)
    features.append(len(url))
    features.append(1 if "@" in url else 0)
    features.append(1 if "-" in domain else 0)
    features.append(url.count('.'))

    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    features.append(1 if re.search(ip_pattern, url) else 0)

    suspicious_words = ["login", "verify", "bank", "secure", "account", "free", "win", "update"]
    features.append(sum(word in url.lower() for word in suspicious_words))

    return features


# ----------------------------
# 2. Bigger Dataset (Synthetic)
# ----------------------------
urls = [
    # SAFE
    "https://www.google.com", "https://www.wikipedia.org",
    "https://github.com", "https://stackoverflow.com",
    "https://amazon.in", "https://flipkart.com",

    # FAKE
    "http://free-money.com", "http://login-secure-bank.net",
    "http://verify-account-now.com", "http://win-prize-fast.com",
    "http://192.168.1.1/login", "http://secure-update-account.net",
    "http://paypal-login-free.com", "http://bank-verify-user.net"
]

labels = [0,0,0,0,0,0, 1,1,1,1,1,1,1,1]

df = pd.DataFrame({"url": urls, "label": labels})

# ----------------------------
# 3. Create Features
# ----------------------------
X = df["url"].apply(extract_features).tolist()
y = df["label"]

# ----------------------------
# 4. Train-Test Split
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ----------------------------
# 5. Train Better Model
# ----------------------------
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# ----------------------------
# 6. Accuracy
# ----------------------------
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))


# ----------------------------
# 7. Prediction
# ----------------------------
def predict_url(url):
    features = extract_features(url)
    prediction = model.predict([features])[0]
    prob = model.predict_proba([features])[0]

    confidence = round(max(prob) * 100, 2)

    if prediction == 0:
        return f"SAFE ({confidence}%)"
    else:
        return f"FAKE ({confidence}%)"


# ----------------------------
# 8. Input Loop
# ----------------------------
print("\n Improved Fake Website Detector\n")

while True:
    url = input("Enter URL (or exit): ")

    if url.lower() == "exit":
        break

    print("Result:", predict_url(url))
