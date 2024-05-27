from playwright.sync_api import sync_playwright

def test_index_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Set to False to see the browser
        page = browser.new_page()

        # Navigate to the local server's URL (adjust the port if different)
        page.goto('http://localhost:8000/')
        
        # Check if the index page loads successfully
        assert page.title() == "Weather App"  # Adjust title according to your HTML

        browser.close()

def test_weather_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Set to False to see the browser
        page = browser.new_page()

        # Navigate to the weather route
        page.goto('http://localhost:8000/weather?city=Kansas%20City')
        
        # Check if the correct data is displayed
        assert "Kansas City" in page.text_content('h1')  # Check if city name is displayed
        assert "°F" in page.text_content('.temperature')  # Example, adjust according to your actual classes/ids

        # Test for a city not found
        page.goto('http://localhost:8000/weather?city=UnknownCityXYZ')
        assert "City not found" in page.text_content('body')  # Adjust according to your error handling

        browser.close()

if __name__ == "__main__":
    test_index_page()
    test_weather_page()
