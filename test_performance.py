from playwright.sync_api import sync_playwright
import time

def test_performance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Start measuring time
        start_time = time.time()

        # Navigate to the website
        page.goto('https://automationbookstore.dev')

        # Wait for the page to load
        page.wait_for_load_state('load')

        # Calculate the time taken
        load_time = time.time() - start_time
        print(f"Time taken to load the page: {load_time:.2f} seconds")

        # Save the result in a text file
        with open('performance_results.txt', 'w') as file:
            file.write(f"Time taken to load the page: {load_time:.2f} seconds\n")

        # Close the browser
        browser.close()

if __name__ == '__main__':
    test_performance()
