import time

# Result file path
result_file = 'test_result.txt'

def after_scenario(context, scenario):
    # Log the result of each scenario (pass or fail)
    with open(result_file, 'a') as file:
        # Capture if the scenario passed or failed
        result = "Passed" if scenario.status == "passed" else "Failed"
        file.write(f"Scenario: {scenario.name}\n")
        file.write(f"Status: {result}\n")
        
        # If the scenario passed, capture the time it took to load the page
        if result == "Passed":
            load_time = context.page.evaluate("performance.timing.loadEventEnd - performance.timing.navigationStart")
            file.write(f"Time taken to load the page: {load_time / 1000:.2f} seconds\n")
        file.write("\n")

def before_scenario(context, scenario):
    # Set up a new browser instance and page before each scenario
    from playwright.sync_api import sync_playwright
    context.start_time = time.time()

    with sync_playwright() as p:
        context.browser = p.chromium.launch(headless=True)
        context.page = context.browser.new_page()
        context.page.goto('https://automationbookstore.dev')

def after_all(context):
    # Close the browser after all scenarios are completed
    context.browser.close()
