# Sesiunea 12: BDD - Part 2

## 📝 Obiective
- Key Notes BDD - Part 1 (Sesiunea 11)
- POM - Page Object Model Design Pattern
- Setup proiect testare BDD
- Structura proiect testare BDD

- Practica: testare BDD

## 🔑 Key Notes BDD - Partea 1 (Sesiunea 11)

### 🔐 Metodologii de testare software

- Pentru a obtine un **produs software** final **calitativ**, **in buget** si in **timp util**,
desfasurarea proiectului se desfasoara urmand un **set de reguli**, **practici**, **procese** si **tehnici** -> o metodologie de dezvoltare software.
- Cele mai folosite metodologii de dezvoltare software: **Agile**, **Waterfall**.

### 🔐 Agile

- **Framework-ul de testare BDD este cel mai des folosit in metodologia Agile.**
- Pentru a defini <span style="color:#5091E8">**clar cerintele/functionalitatile**</span> pe care un produs software trebuie sa le aiba, trebuie definite <span style="color:#5091E8">**user story-uri.**</span>

#### 📍 <span style="color:#5091E8">Agile - User Story</span>
- Un user story reprezinta o <span style="color:#5091E8">**explicatie end to end a unui feature**</span> facuta din perspectiva utilizatorului final (<span style="color:#5091E8">**rezultatul la care trebuie sa ajungem pentru a duce o functionalitate la bun sfarsit)**</span>.
- User story-urile sunt scrise sub forma:
<span style="color:#5091E8">**"As a (type of user), I want to (perform some action) so that I (can achieve some goal/result/value)."**</span>
- <span style="color:#5091E8">**Scopul**</span> user-story-urilor este de <span style="color:#5091E8">**a explica rolul utilizatorilor intr-un sistem, activitatile lor si sa identificam necesitatile utilizatorilor.**</span>
- Pentru a ne asigura ca user story-urile sunt indeplinite 
si se aliniaza cu cererile din partea clientului,
avem nevoie de una sau mai multe <span style="color:#EA4444">**acceptance criteria (definition of done)**</span>.

#### 📍 <span style="color:#EA4444">Agile - Acceptance Criteria</span>
- Acceptance criteria reprezinta <span style="color:#EA4444">**conditii**</span> care daca sunt urmate, <span style="color:#EA4444">**duc la atingerea obiectivului stabilit in user-story**</span>.
- Acceptance criteria ajuta echipa de dezvoltare sa aiba o intelegere clara si concisa asupra a ceea ce trebuie dezvoltat si ce e cuprins in user story-ul curent, ajuta la divizarea corecta a user story-ului in task-uri dar de asemenea, ajuta si la a furniza o baza pentru testarea automata.
- Acceptance criteria sunt <span style="color:#EA4444">**scrise**</span> folosind <span style="color:#EA4444">**formatul Given/Then/When**</span>.
- <span style="color:#EA4444">**Astfel, putem prelua acceptance criteria in testarea automata a user story-ului 
si sa transpunem criteriile de acceptanta in scenarii de teste.**</span>

### 🔐 BDD
- <span style="color:#8044EA">**BDD = Behaviour Driven Development**</span>.
- BDD-ul (Behaviour Driven Development) este un <span style="color:#8044EA">**framework 
de testare automata**</span> care
presupune <span style="color:#8044EA">**testarea scenariilor
de business**</span> prin folosirea unor 
<span style="color:#8044EA">**fisiere descriptive
(feature files)**</span> - care sunt corelate cu criteriile de acceptanta incluse in user story-uri.

#### 📍 BDD - Features file & Gherkin
- Fisierele descriptive (feature files)
sunt scrise in <span style="color:#8044EA">
**limbajul Gherkin**</span>.
- In general, intr-un feature file de BDD putem gasi urmatoarele <span style="color:#8044EA">**elemente**</span>:
1. <span style="color:#8044EA">**Feature**</span> = o functionalitate mai mare care se doreste a fi testata
2. <span style="color:#8044EA">**Scenario**</span> = o descriere a unei situatii specifice care poate fi intalnita de un utilizator in viata reala
3. <span style="color:#8044EA">**Scenario steps**</span> = instructiuni care trebuie urmarite pas cu pas pentru verificarea unui scenariu (Given, When, Then, And, But)
4. <span style="color:#8044EA">**Background**</span> = context general valabil pentru majoritatea scenariilor de testare.


## 🔶 POM Design Pattern
- **POM Design Pattern** = Page Object Model Design Pattern
- POM este **cel mai folosit design pattern** in testarea web
- **Design Pattern** = o solutie gasita pentru o problema general
intalnita la software -> o structura/un how-to de urmat astfel incat sa avem o solutie/o implementare consistenta, readable si extensibila
- **PAGE OBJECT MODEL** = un design pattern care presupune gruparea
codului de TESTARE AUTOMATA, astfel incat fiecare pagina web sa aiba un corespondent (o clasa intr-un fisier python) de mapare
a elementelor si actiunilor de pe acea pagina


## 🔶 Setup proiect BDD
1. Pycharm -> New Project
2. pip install selenium
3. pip install behave (o librarie BDD care va interpreta si rula testele scrise in Gherkin)
4. pip install behave-html-formatter (ne ajuta sa generam rapoarte BDD)
5. pip install webdriver-manager

## 🔶 Structura unui proiect BDD

1. un folder features = contine toate fisierele de tip feature-files
2. un folder steps = contine implementarea tehnica a fisierelor de tip feature
3. un folder pages (cel care defineste structura BDD) = contine paginile de mapare a paginilor web
4. un fisier browser (py) = contine implementarea browser-ului
5. un fisier environment (py) = contine instantierea tuturor obiectelor din clasele de tip Page
6. un fisier base_page (py) = contine metode ce sunt folosite in mai multe fisiere,
pentru a fi importate si reutilizate

## 🔶 behave

- Documentatie: https://behave.readthedocs.io/en/stable/

## 💻 Practica
- Vom folosi POM pentru a testa feature-uri de pe o pagina web:
https://www.saucedemo.com/



