from ddgs import DDGS

def web_search(query: str, max_results: int = 5):
    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            url = r.get("href") or r.get("link")
            if not url:
                continue

            results.append(
                {
                    "title": r.get("title", ""),
                    "body": r.get("body", ""),
                    "url": url,
                }
            )

    return results