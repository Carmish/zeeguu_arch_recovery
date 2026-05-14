tools/crawler/crawl_roundrobin.py [150:214]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    feeds_by_language = {}
    total_feeds = 0

    for lang_code in languages_to_crawl:
        language = Language.find(lang_code)
        feeds = Feed.query.filter_by(language_id=language.id).filter_by(deactivated=False).all()
        feeds_by_language[lang_code] = feeds
        total_feeds += len(feeds)
        log(f"{lang_code.upper()}: {len(feeds)} feeds")

    log(f"\nTotal feeds across all languages: {total_feeds}")
    log(f"Processing {articles_per_feed} article(s) per feed before switching")

    # If recent_days is set, temporarily override last_crawled_time for all feeds
    if recent_days:
        min_date = datetime.now() - timedelta(days=recent_days)
        log(f"*** Filtering articles: Only processing from last {recent_days} days (since {min_date.strftime('%Y-%m-%d %H:%M')})")
        for lang_code in languages_to_crawl:
            for feed in feeds_by_language[lang_code]:
                if feed.last_crawled_time and feed.last_crawled_time < min_date:
                    log(f"    Overriding {feed.title}: {feed.last_crawled_time} -> {min_date}")
                    feed.last_crawled_time = min_date
    log("")

    # Track which feed index we're at for each language
    feed_indices = {lang: 0 for lang in languages_to_crawl}
    feeds_completed = 0

    # Round-robin through languages until all feeds are processed
    while feeds_completed < total_feeds:
        made_progress = False

        for lang_code in languages_to_crawl:
            feeds = feeds_by_language[lang_code]
            idx = feed_indices[lang_code]

            # Skip if this language has no more feeds
            if idx >= len(feeds):
                continue

            made_progress = True
            feed = feeds[idx]
            crawl_report = crawl_reports[lang_code]

            # Add feed to report
            crawl_report.add_feed(feed)

            if feed.deactivated:
                feed_indices[lang_code] += 1
                feeds_completed += 1
                continue

            # Process this feed
            try:
                log("")
                log(f"[{lang_code.upper()}] >>>>> {feed.title} ({idx+1}/{len(feeds)}) <<<<<")

                feed_start_time = time()

                # Download from feed (this already handles article limits internally)
                download_from_feed(
                    feed,
                    db_session,
                    crawl_report,
                    limit=max_articles_per_feed,
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



zeeguu/operations/crawler/crawl.py [201:265]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    feeds_by_language = {}
    total_feeds = 0

    for lang_code in languages_to_crawl:
        language = Language.find(lang_code)
        feeds = Feed.query.filter_by(language_id=language.id).filter_by(deactivated=False).all()
        feeds_by_language[lang_code] = feeds
        total_feeds += len(feeds)
        log(f"{lang_code.upper()}: {len(feeds)} feeds")

    log(f"\nTotal feeds across all languages: {total_feeds}")
    log(f"Processing {articles_per_feed} article(s) per feed before switching")

    # If recent_days is set, temporarily override last_crawled_time for all feeds
    if recent_days:
        min_date = datetime.now() - timedelta(days=recent_days)
        log(f"*** Filtering articles: Only processing from last {recent_days} days (since {min_date.strftime('%Y-%m-%d %H:%M')})")
        for lang_code in languages_to_crawl:
            for feed in feeds_by_language[lang_code]:
                if feed.last_crawled_time and feed.last_crawled_time < min_date:
                    log(f"    Overriding {feed.title}: {feed.last_crawled_time} -> {min_date}")
                    feed.last_crawled_time = min_date
    log("")

    # Track which feed index we're at for each language
    feed_indices = {lang: 0 for lang in languages_to_crawl}
    feeds_completed = 0

    # Round-robin through languages until all feeds are processed
    while feeds_completed < total_feeds:
        made_progress = False

        for lang_code in languages_to_crawl:
            feeds = feeds_by_language[lang_code]
            idx = feed_indices[lang_code]

            # Skip if this language has no more feeds
            if idx >= len(feeds):
                continue

            made_progress = True
            feed = feeds[idx]
            crawl_report = crawl_reports[lang_code]

            # Add feed to report
            crawl_report.add_feed(feed)

            if feed.deactivated:
                feed_indices[lang_code] += 1
                feeds_completed += 1
                continue

            # Process this feed
            try:
                log("")
                log(f"[{lang_code.upper()}] >>>>> {feed.title} ({idx+1}/{len(feeds)}) <<<<<")

                feed_start_time = time()

                # Download from feed (this already handles article limits internally)
                download_from_feed(
                    feed,
                    db_session,
                    crawl_report,
                    limit=max_articles_per_feed,
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



