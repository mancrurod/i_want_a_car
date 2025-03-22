# 🚗 "I Want a Car!"

## 🚀 Overview

Help Fer choose the perfect car through data-driven analysis! This project scrapes AutoScout24 data, creating visualizations and insights to support an informed vehicle purchase decision.

---

## 📂 Project Structure

i_want_a_car/
├── data/                 # Raw and processed .csv files
├── images/               # Visualization outputs (.html)
├── src/                  # Source code
│   ├── scraping.py       # Collect car data from AutoScout24
│   ├── transform.py      # Clean and structure the data
│   ├── explore.py        # Analyze car specifications
│   ├── visualize.py      # Generate interactive charts
├── requirements.txt      # Dependencies
├── .gitignore            # Exclude unnecessary files
└── README.md             # Project documentation

---

## ✨ Features

✔ **Web Scraping**: Extract comprehensive car data from AutoScout24.  
✔ **Data Processing**: Clean, normalize, and structure vehicle information.  
✔ **Interactive Analysis**: Explore correlations between price, features, and performance.  
✔ **Visualization Dashboard**: Compare options with dynamic charts and graphs.  
✔ **Vehicle Management**: Register, update, and consult information in the database.

---

## ⚙️ Prerequisites

Ensure you have the following installed:

- **Python**: Version 3.8+
- **Libraries**: pandas, BeautifulSoup4, requests, plotly

---

## 📥 Installation

1. **Clone the repository**:
    
```bash
git clone https://github.com/your_username/i_want_a_car.git
cd i_want_a_car
```

2. **Install dependencies**:
    
```bash
pip install -r requirements.txt
```

---

## 📖 Usage

1. **Run the data collection**:
    
```bash
python src/scraping.py
```

2. **Transform the data**:
    
```bash
python src/transform.py
```

3. **Generate visualizations**:
    
```bash
python src/visualize.py
```

4. **Launch the application**:
    
```bash
python main.py
```

---

## 🔄 Workflow

1. **Web Scraping** → Collect vehicle listings from AutoScout24.
2. **Data Transformation** → Clean and structure the collected data.
3. **Exploratory Analysis** → Identify trends and patterns.
4. **Visualization** → Create interactive charts for comparison.
5. **Decision Support** → Generate insights to help with car selection.

---

## 🛠️ Troubleshooting

🔹 **Scraping Issues** → Check your internet connection and website structure changes.  
🔹 **Missing Data** → Verify data files exist in the data/ directory.  
🔹 **Visualization Errors** → Ensure plotly is properly installed.  
🔹 **Performance Problems** → Consider filtering the dataset for faster processing.

---

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch:
    
```bash
git checkout -b feature/new-feature
```

3. Commit your changes:
    
```bash
git commit -m "Add new feature"
```

4. Push to the branch:
    
```bash
git push origin feature/new-feature
```

5. Open a pull request.

---

## 📜 License

This project is licensed under the **MIT License**. See LICENSE for details.

---

🚀 **Help Fer find his dream car with data science!**