from behave import given, when, then
from playwright.sync_api import sync_playwright

@given('I am on the "{url}" page')
def step_given_i_am_on_the_page(context, url):
    context.page.goto(url)

@when('I click on the "{book_name}" book')
def step_when_i_click_on_the_book(context, book_name):
    # Locate the book by its text and click on it
    context.page.click(f'//h3[text()="{book_name}"]')

@then('I should see the book details page')
def step_then_i_should_see_the_book_details(context):
    # Wait for the book details page to load
    context.page.wait_for_load_state('load')
    assert 'Test Automation in the Real World' in context.page.title()

@then('the result should be saved in a test result file')
def step_then_the_result_should_be_saved_in_file(context):
    # This step is now handled by the `after_scenario` hook in `environment.py`
    pass
