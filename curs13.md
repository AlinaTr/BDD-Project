# Sesiunea 13: BDD - Partea 3

## 📝 Obiective
- Rularea scenariilor de test
- Generare raport HTML scenarii de test
- Scenario steps: Given, When, Then, And, But
- Parametrizare scenario steps
- Tag-uri scenarii
- Scenario outline
- Background

## 🔶 Rulare scenarii de test

- Pentru a rula testele folosim comanda **behave**:

```commandline
behave
```

## 🔶 Generare raport HTML

- Pentru a genera un raport HTML cu rezultatele testelor,
rulam comanda:

```commandline
behave -f html -o behave-report.html
```

- Inainte de a rula comanda, trebuie sa cream (la nivelul)
proiectului, un fisier "behave.ini", cu urmatorul continut
```
[behave.formatters]
html = behave_html_formatter:HTMLFormatter 
```

## 🔶 Scenario steps: Given, When, Then, And, But

### 🐾 Given
- Crearea contextului scenariului de testare
- Punerea sistemului intr-un context cunoscut inainte
ca utilizatorul sa inceapa sa interactioneze cu sistemul
- Exemple: navigarea catre o pagina, logarea utilizatorului etc

### 🐾 When
- Cuprinde actiuni ale utilizatorului
- Descrie interactiunea cu sistemul (ce vrem sa testam)
- Exemple: click pe elemente de pe pagina, completare valori pe pagina


### 🐾 Then
- Verificarea rezultatelor observabile de catre utilizator
- Ce se intampla daca utilizatorul a urmat tot scenariul

### 🐾 And si But

```
Scenario: Multiple Givens
  Given one thing
  Given an other thing
  Given yet an other thing
   When I open my eyes
   Then I see something
   Then I don't see something else
```

```
Scenario: Multiple Givens
  Given one thing
    And an other thing
    And yet an other thing
   When I open my eyes
   Then I see something
    But I don't see something else
```

## 🔶 Parametrizare scenario steps
- Atunci cand avem pasi asemanatori in diferite scenarii si doar valorile introduse/testate difera,
putem sa parametrizam pasul respectiv.

1. In feature file:
```
Scenario: look up a book
  Given I search for a valid book
   Then the result page will include "success"

Scenario: look up an invalid book
  Given I search for a invalid book
   Then the result page will include "failure"
```

2. In implementarea scenario step:

```
@then('the result page will include "{text}"')
def step_impl(context, text):
    if text not in context.response:
        fail('%r not in %r' % (text, context.response))
```

## 🔶 Tag-uri scenarii
- Putem adauga tag-uri pentru scenariile testate in feature files.

```
Feature: Fight or flight
  In order to increase the ninja survival rate,
  As a ninja commander
  I want my ninjas to decide whether to take on an
  opponent based on their skill levels

  @slow
  Scenario: Weaker opponent
    Given the ninja has a third level black-belt
    When attacked by a samurai
    Then the ninja should engage the opponent

  Scenario: Stronger opponent
    Given the ninja has a third level black-belt
    When attacked by Chuck Norris
    Then the ninja should run for his life
```

- Folosind tag-uri, putem sa personalizam rularea testelor astfel:
1. Rularea scenariilor de test cu un anumit tag:
```commandline
behave --tags=slow
```
2. Rularea scenariilor de test, cu exceptia celor care au un anumit tag:
```commandline
behave --tags=-slow
```
- Use case: definirea unui tag @wip si rularea doar
acelui scenariu de test

## 🔶 Scenario Outline
- Cand avem scenarii de testare asemanatoare,
in care difera doar parametrii din pasi si rezultatul,
ne putem folosi de Scenario Outline pentru a rula
acelasi scenariu cu mai multe seturi de parametri.

```
Scenario Outline: Blenders
   Given I put "<thing>" in a blender,
    when I switch the blender on
    then it should transform into "<other thing>"

 Examples: Amphibians
   | thing         | other thing |
   | Red Tree Frog | mush        |

 Examples: Consumer Electronics
   | thing         | other thing |
   | iPhone        | toxic waste |
   | Galaxy Nexus  | toxic waste |
```

## 🔶 Background
- Daca consider ca un pas given (contextul actiunii)
este valabil pentru mai multe scenarii/pentru toate scenariile,
atunci, pentru a economisi cod voi putea trece
acel pas la inceputul unui feature file sub keyword-ul
Background.
```
Scenario: Check that you can login into the application when providing correct credentials
    Given I am on the saucedemo login page
    When I insert username "standard_user" and password "secret_sauce"
    When I click the login button
    Then I can login into the application and see the list of products
```

```
Feature: Check the functionality of the login page

    Background:
        Given I am on the saucedemo login page
        
    Scenario: Check that you can login into the application when providing correct credentials
        When I insert username "standard_user" and password "secret_sauce"
        When I click the login button
        Then I can login into the application and see the list of products
```