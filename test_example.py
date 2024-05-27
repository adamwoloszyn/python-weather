from playwright.sync_api import sync_playwright

def test_index_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) 
        page = browser.new_page()

        try:
            page.goto('https://127.0.0.1:8000/')
            assert page.title() == "Get Weather Conditions"
            print("test_index_page: Passed")
        except AssertionError:
            print("test_index_page: Failed")
        finally:
            browser.close()

def test_weather_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) 
        page = browser.new_page()

        try:
            page.goto('https://127.0.0.1:8000/weather?city=Kansas%20City')        
            assert "Kansas City Weather" in page.text_content('h1') 

            page.goto('https://127.0.0.1:8000/weather?city=UnknownCityXYZ')
            assert "City Not Found" in page.text_content('h1') 

            print("test_weather_page: Passed")

        except AssertionError:
            print("test_weather_page: Failed")
        finally:
            browser.close()

if __name__ == "__main__":
    test_index_page()
    test_weather_page()
