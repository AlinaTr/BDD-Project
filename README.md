# BDD-Project_Swag Labs
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/AlinaTr/BDD-Project/main?style=flat&logo=github&color=%2300FFFF)

## 🔶 Description

Welcome to my project! I have used <span style="color:#EA4444"> **BDD (Behaviour Driven Development)**</span> framework to run test scenarios.

## 🔶 How to Install and Run the Project
1. Install Google Chrome
2. Install Pycharm Community Edition: https://www.jetbrains.com/pycharm/download/
3. Install Python https://www.python.org/downloads/

## 🔶 Setup BDD Project
1. Pycharm -> New Project
2. pip install selenium
3. pip install behave (a Python library to implement BDD tests in Gherkin)
4. pip install behave-html-formatter (to generate BDD reports)
5. pip install webdriver-manager

## 🔶 BDD Project Structure
1.  <span style="color:#8044EA">**folder features**</span> = contains all feature files
2.  <span style="color:#8044EA">**folder steps**</span>= contains technical implementation of the feature files
3.  <span style="color:#8044EA">**folder pages**</span> = contains classes to access the web pages
4.  <span style="color:#8044EA">**browser file (py)**</span> = contains the browser implementation
5.   <span style="color:#8044EA">**environment file (py)**</span> = define hooks that will be called before or after each step, scenario, feature or even entire test run
6.   <span style="color:#8044EA">**base_page file (py)**</span> =  methods that are used in multiple files, to be imported and re-used

###  <span style="color:#EA4444"> This is the link to see the report:
* https://github.com/AlinaTr/BDD-Project/commit/d7db69794bd308c7b21df7f45edf0fe287529886