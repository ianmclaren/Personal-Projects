from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Go to the golf booking page
        page.goto("https://www.tee-on.com/PubGolf/servlet/com.teeon.teesheet.servlets.trail.TrailSearch?CourseGroupID=11810&InFrame=true&InFrameCourseCode=CHIG")

        # Finding the correct date (current + 5 days) from the date scroller
        page.wait_for_selector("#search-results-date-select-scroller a")
        date_links = page.query_selector_all("#search-results-date-select-scroller a")
        last_date_link = date_links[-2] #CHANGED FOR TESTING
        last_date_link.click()

        #Ensure the 18 Holes filter is selected
        hole_selector = "#hole-filter-18" #TODO: Make this customizable
        page.wait_for_selector(hole_selector)

        hole_button = page.query_selector(hole_selector)
        if hole_button:
            classes = hole_button.get_attribute("class") or ""
            if "primary" not in classes:
                hole_button.click()

        #Search for the timeslot, ensure sufficient players, and book it
        page.wait_for_selector(".search-results-tee-times-box")
        rows = page.query_selector_all(".search-results-tee-times-box")
        target_time = "5:07pm" #TODO: Make this customizable
        desired_players = "4" #TODO: Make this customizable

        for row in rows:
            time_elem = row.query_selector(".time")
            players_elem = row.query_selector(".players-allowed")

            if not time_elem or not players_elem:
                continue

            time_text = time_elem.inner_text().strip().lower()
            players_text = players_elem.inner_text().strip()
            print(f"time_text: {time_text}, players: {players_text}")

            if time_text == target_time and desired_players in players_text:
                row.click()
                print(f"Selected the {time_text} slot for {players_text}")
                break
        else:
            print("No matching 5:07 pm slot for 4 players found")

        page.wait_for_timeout(15000)
        browser.close()

if __name__ == "__main__":
    run()