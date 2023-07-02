from behave import *


@given('I am on the saucedemo login page')
def step_impl(context):
    """
    CONTEXT este in primul rand un parametru pe care toate functiile/
    implementarile de scenario steps il vor avea.
    El reprezinta o cutiuta in care pot sa stochez toate obiectele
    instantiate in fisierul environment.py
    """

    #Voi avea nevoie de: o instanta/un obiect al clasei LoginPage
    #si sa apelez metoda navigate_to_login_page

    context.login_page_object.navigate_to_login_page()


@when('I insert username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page_object.insert_username(username)
    context.login_page_object.insert_password(password)

@when('I do not insert username and only insert password "{password}"')
def step_impl(context, password):
    context.login_page_object.insert_password(password)


@when('I click the login button')
def step_impl(context):
    context.login_page_object.click_login_button()


@then('I can login into the application and see the list of products')
def step_impl(context):
    context.inventory_page_object.check_current_url()


@then('I cannot login into the application and I receive "{error_message}" error')
def step_impl(context, error_message):
    context.login_page_object.check_login_error_message(error_message)
