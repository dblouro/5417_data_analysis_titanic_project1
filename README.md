# **Titanic Survival Data Analysis**
**Lab Project**
Developed by **Diogo Louro, Ricardo Conceição, and João Pedro Silva**

---

## ** Project Description**
This project involves **exploratory analysis and preprocessing** of the Titanic dataset using Python, Pandas, Seaborn, and SQLite. The goal is to explore survival patterns among passengers, clean and transform the data, and visualize key insights.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-2E8B57?style=for-the-badge&logo=seaborn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![Statsmodels](https://img.shields.io/badge/Statsmodels-4B8BBE?style=for-the-badge&logoColor=white)

![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-005A9C?style=for-the-badge&logoColor=white)

## ** Project Structure**
- **`titanic.csv`**: Original dataset.
- **`titanic_tratado.csv`**: Cleaned and preprocessed dataset.
- **`titanic_tratado_com_idade.csv`**: Dataset with the `Idade_Milissegundos` column.
- **`titanic_tratado_com_idade_final.csv`**: Final dataset with all transformations.
- **`dados.db`**: SQLite database containing the `passageiros` table.

---

## ** Technologies Used**
- **Python** (Pandas, NumPy, Seaborn, Matplotlib, Statsmodels)
- **SQLite** (data storage)
- **Excel/OpenPyXL** (file manipulation)

---

## ** Activities Performed**

### **1. Data Reading and Exploration**
- Loaded the `titanic.csv` dataset.
- Viewed the first and last records.
- Conducted statistical analysis of numeric and non-numeric columns.

### **2. Data Cleaning and Preprocessing**
- **Handling missing values**:
  - `Age` and `Fare`: Filled with the median.
  - `Cabin`: Filled with "Unknown".
- Saved the cleaned dataset as `titanic_tratado.csv`.

### **3. Data Transformation**
- **Calculated age in milliseconds** since the Unix Epoch (1970).
- Created the `Idade_Milissegundos` column.

### **4. Survival Analysis**
- **Mortality and survival rates by gender**.
- **Survival rates by class and gender**.
- **Average age by survival status**.
- **Visualizations**:
  - Age distribution by survival.
  - Correlation between `Age`, `Fare`, and `Survived`.

### **5. Additional Analysis**
- **Family size and survival**:
  - Created the `Tamanho_Familia` column (SibSp + Parch + 1).
  - Survival rate by family size.
- **Embarkation port and survival**:
  - Mapped ports (`C`, `Q`, `S`).
  - Survival rate by embarkation port.

### **6. Export and Storage**
- Exported the final dataset to `titanic_tratado_com_idade_final.csv`.
- Stored the data in an **SQLite database** (`dados.db`).

---

## ** Results and Insights**
- **Women had a significantly higher survival rate** than men.
- **First-class passengers** were more likely to survive.
- **Children and young adults** (especially in 2nd and 3rd class) had higher survival rates.
- **Embarkation port**: Passengers who embarked at **Cherbourg** had a higher survival rate.

---

## ** Visualizations**
### **Age Distribution by Survival**
<p align="center">
  <img src="images/age_distribution_by_survival.png" width="30%" alt="Distribuição da Idade por Sobrevivência">
</p>

### **Survival Rate by Class and Gender**
<p align="center">
  <img src="images/survival_rate_by_class_and_gender.png" width="30%" alt="Distribuição por Classe e Genero">
</p>

### **Family Size vs. Survival**
<p align="center">
  <img src="images/familysize_vs_survival.png" width="30%" alt="Relação entre Familia e Sobrevivencia">
</p>

### **Additional Analysis - Comparison by Port of Shipment**
<p align="center">
  <img src="images/comparison_by_port_of_shipment.png" width="30%" alt="Análise Adicional - Comparação por Porto de Embarque">
</p>

---

## **🛠 How to Reproduce the Analysis**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/ProjectoFinal.git
   
2. **Install dependencies**:
    ```bash
   pip install pandas openpyxl seaborn matplotlib statsmodels sqlite3

3. **Run the script**:
    ```bash   
    python titanic_analysis.py

---

## ** Conclusions**

Social class and gender were decisive factors in survival.
Larger families (especially with children) had an advantage.
Embarkation port may indicate socioeconomic differences among passengers.

📧 Contact: diogolouro@outlook.com
