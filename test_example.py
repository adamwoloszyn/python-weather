import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://python-weather-dot-adam-workshop.uw.r.appspot.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Get Weather Conditions"))

