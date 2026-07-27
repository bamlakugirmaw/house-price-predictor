## 🌐 Live Demo

https://house-price-predictor-irzgddmdehd8lsg4tgw2ob.streamlit.app/

# 🏡 EstateValuate – AI Real Estate Engine

An intelligent machine learning web application that predicts residential property prices in Ethiopia based on property characteristics, location, and infrastructure proximity.

Built with **Streamlit** and **Scikit-learn**, EstateValuate provides instant property valuation through an elegant, modern interface.

---

## 📸 Preview

> Add a screenshot of your application here after deployment.

---

## ✨ Features

- Predicts Ethiopian house prices instantly
- Clean, modern Streamlit interface
- Machine Learning powered predictions
- Interactive sliders and input fields
- Fast real-time valuation
- Responsive dark-themed UI

---

## 🧠 Machine Learning

The prediction model was trained using property-related features including:

- Number of Rooms
- Built Area
- Site Area
- Property Age
- Distance to CBD
- Distance to Bus Station
- Distance to School
- Building Material
- Property Typology
- Land Grading
- Road Access

The trained model is serialized using **Joblib** and loaded efficiently using Streamlit caching.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## 📂 Project Structure

```
house-price-predictor/
│
├── app.py
├── best_house_price_model.pkl
├── houses_improved.csv
├── house-price-predictor.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/bamlakugirmaw/house-price-predictor.git
```

Move into the project directory

```bash
cd house-price-predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

- Interactive property maps
- Image-based house analysis
- Model comparison dashboard
- Price trend visualization
- Cloud database integration

---

## 👨‍💻 Author

**Bamlaku Girmaw**

Computer Science Student

GitHub:
https://github.com/bamlakugirmaw

---

## 📜 License

This project is intended for educational and portfolio purposes.
