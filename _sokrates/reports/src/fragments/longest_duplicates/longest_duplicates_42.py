zeeguu/core/elastic/elastic_query_builder.py [82:138]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
):
    """
    Builds an elastic search query for article recommendations.

    Filters articles by:
    - Language
    - User's CEFR level (via available_cefr_levels field)
    - Topic preferences
    - Disturbing content (if enabled)

    Scores/ranks by recency (preferring recent articles).

    Args:
        user_cefr_level: User's CEFR level string (e.g., "A1", "B2")
                        Articles must have this level in available_cefr_levels.
                        Also matches compound levels (e.g., A2 matches "A1/A2").
    """

    # must = mandatory, has to occur
    # must not = has to not occur
    # should = nice to have (extra points if it matches)
    must = []

    must_not = []
    should = []

    bool_query_body = {"query": {"bool": {}}}  # initial empty bool query

    if language:
        must.append(match("language", language.name))

    if not user_topics:
        user_topics = ""

    topics_to_filter_out = array_of_topics(topics_to_exclude)
    if len(topics_to_exclude) > 0:
        should_remove_topics = []
        for t in topics_to_filter_out:
            should_remove_topics.append({"match": {"topics": t}})
            should_remove_topics.append({"match": {"topics_inferred": t}})
        must_not.append({"bool": {"should": should_remove_topics}})

    if unwanted_user_topics:
        must_not.append(match("content", unwanted_user_topics))
        must_not.append(match("title", unwanted_user_topics))

    # Exclude sources that user has repeatedly scrolled past (behavioral filtering)
    # Note: Each Article has a source_id that links to a Source record, which is an
    # abstraction for all content types (Article, Video, etc.). This filters based on
    # user behavior - sources they've scrolled past multiple times without engaging.
    if user_ignored_sources:
        must_not.append(
            terms(
                "source_id",
                user_ignored_sources,
            )
        )
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



zeeguu/core/elastic/elastic_query_builder.py [216:252]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
):
    """
    Builds video search query with CEFR level filtering.
    Similar to article recommender but with less emphasis on recency.
    """

    must = []
    must_not = []
    should = []

    bool_query_body = {"query": {"bool": {}}}  # initial empty bool query

    if language:
        must.append(match("language", language.name))

    if not user_topics:
        user_topics = ""

    topics_to_filter_out = array_of_topics(topics_to_exclude)
    if len(topics_to_exclude) > 0:
        should_remove_topics = []
        for t in topics_to_filter_out:
            should_remove_topics.append({"match": {"topics": t}})
            should_remove_topics.append({"match": {"topics_inferred": t}})
        must_not.append({"bool": {"should": should_remove_topics}})

    if unwanted_user_topics:
        must_not.append(match("content", unwanted_user_topics))
        must_not.append(match("title", unwanted_user_topics))

    if user_ignored_sources:
        must_not.append(
            terms(
                "source_id",
                user_ignored_sources,
            )
        )
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



