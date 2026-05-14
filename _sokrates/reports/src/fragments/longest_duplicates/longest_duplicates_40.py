tools/old/remove_unreferenced_articles.py [41:76]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    reading_session_info = UserReadingSession.query.filter_by(
        article_id=article.id
    ).all()
    belongs_to_a_cohort = CohortArticleMap.query.filter_by(article_id=article.id).all()

    referenced = info or interaction_data or reading_session_info or belongs_to_a_cohort

    if print_reference_info and referenced:
        print(f"WON'T DELETE ID:{article.id} -- {article.title}")

        for ainfo in info:
            print(ainfo.user_info_as_string())

        if interaction_data:
            print("interaction data: (e.g. " + str(interaction_data[0]))

        if reading_session_info:
            print("reading session info: (e.g. " + str(reading_session_info[0]))

        if belongs_to_a_cohort:
            print("referenced by a cohort: (e.g. " + str(belongs_to_a_cohort[0]))

    return referenced


def delete_articles_older_than(
    DAYS, print_progress_for_every_article=False, delete_from_ES=True
):
    print(f"Finding articles older than {DAYS} days...")
    all_articles = Article.all_older_than(days=DAYS)
    print(f" ... article count: {len(all_articles)}")

    i = 0
    referenced_in_this_batch = 0
    deleted = []
    deleted_from_es = 0
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



tools/remove_unreferenced_articles.py [49:84]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    reading_session_info = UserReadingSession.query.filter_by(
        article_id=article.id
    ).all()
    belongs_to_a_cohort = CohortArticleMap.query.filter_by(article_id=article.id).all()

    referenced = info or interaction_data or reading_session_info or belongs_to_a_cohort

    if print_reference_info and referenced:
        print(f"WON'T DELETE ID:{article.id} -- {article.title}")

        for ainfo in info:
            print(ainfo.user_info_as_string())

        if interaction_data:
            print("interaction data: (e.g. " + str(interaction_data[0]))

        if reading_session_info:
            print("reading session info: (e.g. " + str(reading_session_info[0]))

        if belongs_to_a_cohort:
            print("referenced by a cohort: (e.g. " + str(belongs_to_a_cohort[0]))

    return referenced


def delete_articles_older_than(
    DAYS, print_progress_for_every_article=False, delete_from_ES=True
):
    print(f"Finding articles older than {DAYS} days...")
    all_articles = Article.all_older_than(days=DAYS)
    print(f" ... article count: {len(all_articles)}")

    i = 0
    referenced_in_this_batch = 0
    deleted = []
    deleted_from_es = 0
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



