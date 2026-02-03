# 🛡️ Cyberbullying Detection System

A machine learning-powered web application that detects potential cyberbullying in text using Natural Language Processing.

## 🎯 Features

- Real-time text analysis
- ML-based classification (Logistic Regression + TF-IDF)
- Confidence scoring
- Clean, responsive UI
- Simple REST API

## 🛠️ Tech Stack

**Backend:**
- Python 3.9+
- Flask
- scikit-learn
- NLTK

**Frontend:**
- HTML5
- CSS3
- Vanilla JavaScript

## 📦 Installation

1. Clone the repository
```bash
git clone https://github.com/verahjd/cyberbullying-detection.git
cd cyberbullying-detection
```

2. Install Python dependencies
```bash
cd backend
pip install -r requirements.txt
```

3. Train the model
```bash
python model.py
```

4. Run the backend
```bash
python app.py
```

5. Open frontend
```bash
cd ../frontend
# Open index.html in your browser
# Or run: python -m http.server 3000
```

## 🚀 Usage

1. Enter text in the textarea
2. Click "Analyze Text"
3. View the results with confidence score

## 📊 Model Performance

- Accuracy: ~85%
- Training Data: 50,000 labeled tweets
- Algorithm: Logistic Regression with TF-IDF features

## 🔮 Future Improvements

- [ ] Multi-class classification (types of cyberbullying)
- [ ] Deep learning models (BERT)
- [ ] Real-time social media monitoring
- [ ] Browser extension
- [ ] User authentication and history

## 📝 License

MIT License

## 🤝 Contributing

Contributions welcome! Please open an issue first.

## 👤 Author

Your Name
- GitHub: [@verahjd](https://github.com/verahjd)
- LinkedIn: [Verah Dulay](https://linkedin.com/in/verah-dulay)
