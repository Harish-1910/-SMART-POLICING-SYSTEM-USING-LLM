# SMART-POLICING-SYSTEM-USING-LLM
# 🚔 IntelCop – LLM-Powered Crime Insight Dashboard

**IntelCop** is an AI-powered crime data analysis tool built using **Streamlit** and **Flask**, and powered by **DeepSeek LLM**. This interactive dashboard allows users to ask questions in natural language, visualize trends, and gain insights from Indian crime datasets.

---

## 🧠 Key Technologies

- **DeepSeek LLM** – for understanding and answering crime-related queries
- **Streamlit** – for the interactive web UI
- **Flask** – API backend to process and serve model responses
- **LangChain** – framework for building LLM-driven pipelines
- **Pandas** – for data handling and filtering
- **Unstructured** – for text extraction and processing
- **ChromaDB** – for vector storage and similarity search

---

## 🎯 Features

- 💬 Ask natural questions about crime statistics
- 📊 View visual insights and data summaries
- 📁 Preview crime datasets
- ⚙️ Clean architecture with separate API and UI layers
- 🧠 LLM-powered logic handled using LangChain + DeepSeek

---

## 📁 Folder Structure

```
intelcop/
├── hello.py               # Flask API (backend)
├── streamlit_app.py       # Streamlit frontend (user interface)
├── crime_data_india.csv   # Dataset used for analysis
├── requirements.txt       # Python dependencies
├── .gitignore             # Ignore rules for Git
└── README.md              # You're reading this file
```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/intelcop.git
cd intelcop
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate       # For Windows
# source venv/bin/activate  # For Mac/Linux
```

### 3️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Flask Backend API

```bash
python hello.py
```

This starts the backend server at `http://127.0.0.1:5000`.

---

### 5️⃣ Run the Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

Make sure `streamlit_app.py` is sending requests to `http://localhost:5000`.

---

## 💡 Example Queries to Try

- "Show top 5 states with highest crime rates"
- "Plot theft crimes by year"
- "Visualize crimes in Tamil Nadu from 2015 to 2020"
- "What are the most reported crimes in Delhi?"

---

## 📊 Dataset

We use `crime_data_india.csv`, a structured dataset representing various crime statistics categorized by region, year, and type.

---

## 🧪 Dependencies

From `requirements.txt`:

```text
langchain==0.2.14
langchain-community==0.2.12
langchain-groq==0.1.9
unstructured==0.14.6
selenium==4.21.0
chromadb==0.5.0
streamlit==1.35.0
pandas==2.0.2
python-dotenv==1.0.0
```

---


## 📸 Screenshots

### 🏠 Home Page
![Home Page](Screenshots/Home%20page.png)

### 🤖 LLM Response Page
![LLM Response Page](Screenshots/LLM%20Response%20page.png)

### 🔐 Login Page
![Login Page](Screenshots/Login%20page.png)

### 💬 Prompt Page
![Prompt Page](Screenshots/Prompt%20page.png)

### 📝 Registration Page
![Registration Page](Screenshots/Registration%20page.png)


---

## 🙋‍♂️ Author

**Harish S.**  

- 🔗 [LinkedIn](https://www.linkedin.com/in/harish-s2003)
- 📫 Email: rks.harish2003@gmail.com 

---

## 📜 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute this project for personal or commercial purposes with proper attribution.
