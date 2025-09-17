from playwright.sync_api import sync_playwright

username = "Enter your username"
password = "Enter your password"

def login(page):
    #Login if needed?
    page.fill("#username", "username")
    page.fill("#password", "password")
    #Click login
    #wait

def run():
    with sync_playwright() as p:
        # Launch browser (set headless=False if you want to watch it)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Open a new page
        page = context.new_page()

        # Go to your golf booking page
        page.goto("https://www.tee-on.com/PubGolf/servlet/com.teeon.teesheet.servlets.trail.TrailSearch?CourseGroupID=11810&InFrame=true&InFrameCourseCode=CHIG")

        # Finding the correct date (current + 5 days) from the date scroller
        page.wait_for_selector("#search-results-date-select-scroller a")
        date_links = page.query_selector_all("#search-results-date-select-scroller a")
        last_date_link = date_links[-1]
        last_date_link.click()

        #Login - should this come after the booking?
        #login(page)


        page.wait_for_timeout(5000)
        browser.close()

if __name__ == "__main__":
    run()