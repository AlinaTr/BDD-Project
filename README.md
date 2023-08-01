# BDD-Project_Swag Labs
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/AlinaTr/BDD-Project/main?style=flat&logo=github&color=%2300FFFF)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/m/Alinatr/BDD-Project?logo=github&color=%239400D3)
![GitHub language count](https://img.shields.io/github/languages/count/AlinaTr/BDD-Project?style=flat-square&logo=github&labelColor=black&color=seagreen)
![GitHub top language](https://img.shields.io/github/languages/top/AlinaTr/BDD-Project?style=flat-square&logo=html&logoColor=%23E34F26)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/AlinaTr/BDD-Project?style=flat-square&labelColor=black)

## 🔶 Description

Welcome to my project! I have used <span style="color:#EA4444"> **BDD (Behaviour Driven Development)**</span> framework to run test scenarios.

## 🔶 How to Install and Run the Project
1. Install Google Chrome
2. Install Pycharm Community Edition: https://www.jetbrains.com/pycharm/download/
3. Install Python https://www.python.org/downloads/

## 🔶 Setup BDD Project
1. Pycharm -> New Project
2. pip install selenium
3. pip install webdriver-manager
4. pip install behave (a Python library to implement BDD tests in Gherkin)
5. pip install behave-html-formatter (to generate BDD reports from terminal)

## 🔶 BDD Project Structure
1.  <span style="color:#8044EA">**folder features**</span> = contains all feature files
2.  <span style="color:#8044EA">**folder steps**</span>= contains technical implementation of the feature files
3.  <span style="color:#8044EA">**folder pages**</span> = contains classes to access the web pages
4.  <span style="color:#8044EA">**browser file (py)**</span> = contains the browser implementation
5.   <span style="color:#8044EA">**environment file (py)**</span> = define hooks that will be called before or after each step, scenario, feature or even entire test run
6.   <span style="color:#8044EA">**base_page file (py)**</span> =  methods that are used in multiple files, to be imported and re-used

