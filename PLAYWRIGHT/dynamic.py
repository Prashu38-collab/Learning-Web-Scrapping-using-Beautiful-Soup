from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # navigating to kantipur
    page.goto("https://ekantipur.com", wait_until="domcontentloaded")
    page.wait_for_timeout(3000)

    # navigation to rajniti
    page.get_by_text("राजनीति").first.click()
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)

    # Grab ALL cards
    cards = page.locator(".category-inner-wrapper").all()
    print(f" Total cards found: {len(cards)}")

    # empty list to store all articles
    all_articles = []

    # extracting the data from each card
    for i, card in enumerate(cards):
        try:
            heading = card.locator(".category-description h2 a").inner_text()
            url     = card.locator(".category-description h2 a").get_attribute("href")

            # handling multiple authors
            author_elements = card.locator(".author-name p a").all()  
            author = ", ".join([a.inner_text() for a in author_elements])

            # handling missing image
            image_locator = card.locator(".category-image figure img")
            image = image_locator.get_attribute("src") if image_locator.count() > 0 else None

            # store as dictionary
            article = {
                "id"    : i + 1,
                "title" : heading,
                "author": author,
                "url"   : url,
                "image" : image
            }

            all_articles.append(article)
            

        except Exception as e:
            print(f" Card {i+1} skipped — {e}")

    # save to JSON file
    with open("rajniti_news.json", "w", encoding="utf-8") as f:
        json.dump(all_articles, f, ensure_ascii=False, indent=4)

    print(f"articles is saved rajniti_news.json")
    browser.close()