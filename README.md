# PDF_Bear_Tools

---

## 🇵🇱 Opis projektu
Zestaw prostych narzędzi do pracy z plikami **PDF**, napisany w języku **Python**. Projekt jest na etapie rozwoju.

---

## 🇵🇱 Funkcjonalności
- Podział pliku PDF na części
- Wyodrębnianie określonych stron z pliku PDF

---

## 🇵🇱 Technologie
- **Python 3.10+**
- **PyPDF2**
- **ReportLab**
- **argparse / os / sys**

## 🇵🇱 Uruchomienie
1. Sklonuj repozytorium:  
   ```bash
   git clone https://github.com/squirrel4life/PDF_Bear_Tools.git
   cd PDF_Bear_Tools
   ```
2. Zainstaluj zależności:  
   ```bash
   pip install PyPDF2 reportlab
   ```
3. Uruchom jedno z narzędzi, jak w [przykładzie poniżej](#-przykład-działania). 

---

## 🇵🇱 Przykład działania

|Narzędzie|Komenda|Zrzut ekranu|
|:-------------|:-----:|------------|
|Podział na części|`py PDF_Bear_Tools.py split sample.pdf --pages_per_part 10`|<img width="597" height="123" alt="image" src="https://github.com/user-attachments/assets/319e8319-ecc1-4438-9b4b-c527f8d97048" />|
|Wyodrębnianie stron|`PDF_Bear_Tools.py excerpt sample.pdf 5 8`|<img width="598" height="87" alt="image" src="https://github.com/user-attachments/assets/9c53c24b-fe29-4764-8441-e0bb5247eec4" />|

---

## 🇬🇧 Opis projektu
 A set of simple tools for working with PDFs based on Python. This is an ongoing project.

---

## 🇬🇧 Functionalities
- Split PDF into parts
- Extract a range of pages from PDF

---

## 🇬🇧 Tech stack
- **Python 3.10+**
- **PyPDF2**
- **ReportLab**
- **argparse / os / sys**

## 🇬🇧 How to run
1. Clone the repo:  
   ```bash
   git clone https://github.com/squirrel4life/PDF_Bear_Tools.git
   cd PDF_Bear_Tools
   ```
2. Install dependencies:  
   ```bash
   pip install PyPDF2 reportlab
   ```
3.Run one of the tools as shown [below](#-example-of-work). 

---

## 🇬🇧 Example of work
|Tool|Command|Screenshot|
|:-------------|:-----:|------------|
|Split PDF into parts|`py PDF_Bear_Tools.py split sample.pdf --pages_per_part 10`|<img width="597" height="123" alt="image" src="https://github.com/user-attachments/assets/319e8319-ecc1-4438-9b4b-c527f8d97048" />|
|Extract a range of pages from PDF|`PDF_Bear_Tools.py excerpt sample.pdf 5 8`|<img width="598" height="87" alt="image" src="https://github.com/user-attachments/assets/9c53c24b-fe29-4764-8441-e0bb5247eec4" />|
