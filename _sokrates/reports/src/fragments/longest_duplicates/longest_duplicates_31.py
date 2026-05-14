tools/report_generator/data_extractor.py [4:116]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def ms_to_mins(ms_time):
    return ms_time / 1000 / 60


class DataExtractor:
    def __init__(self, db_connection, DAYS_FOR_REPORT=7) -> None:
        self.DAYS_FOR_REPORT = DAYS_FOR_REPORT
        self.db_connection = db_connection

    def __add_feed_name(self, df, feed_df, column_with_id="feed_id"):
        df["Feed Name"] = df[column_with_id].apply(
            lambda x: (
                "No Feed"
                if pd.isna(x)
                else str(x) + " " + feed_df.loc[feed_df.id == x, "title"].values[0][:15]
            )
        )

    def run_query(self, query):
        df = pd.read_sql(query, con=self.db_connection)
        return df

    def get_article_topics_df(self, feed_df):
        print("Getting Article Topics...")
        query = f"""SELECT a.id, l.name Language, a.feed_id, t.title Topic, atm.origin_type
        FROM article a 
        INNER JOIN article_topic_map atm on a.id = atm.article_id 
        INNER JOIN topic t ON atm.topic_id = t.id
        INNER JOIN language l ON l.id = a.language_id
        WHERE a.published_time >= DATE_SUB(CURDATE(), INTERVAL {self.DAYS_FOR_REPORT} DAY)
        AND a.broken = 0"""
        df = pd.read_sql(query, con=self.db_connection)
        self.__add_feed_name(df, feed_df)
        return df

    def get_days_since_last_crawl(self):
        print("Getting Feeds Last Crawl Time...")
        query = f"""
            SELECT
                feed_id,
                f.title,
                DATEDIFF(CURDATE(), MAX(published_time)) days_since_last_article,
                DATEDIFF(CURDATE(), f.last_crawled_time) days_since_last_feed_crawl
            FROM
                article a
                JOIN feed f ON a.feed_id = f.id
            WHERE
                f.deactivated = 0
            GROUP by
                feed_id
            HAVING
                days_since_last_feed_crawl <= {self.DAYS_FOR_REPORT}
            ORDER BY
                days_since_last_article DESC;
        """
        df = pd.read_sql(query, con=self.db_connection)
        return df

    def get_article_df(self, feed_df):
        print("Getting Articles...")
        query = f"""SELECT a.*, l.name Language
        FROM article a     
        INNER JOIN language l ON l.id = a.language_id
        WHERE published_time >= DATE_SUB(CURDATE(), INTERVAL {self.DAYS_FOR_REPORT} DAY)
        AND a.broken = 0"""
        df = pd.read_sql(query, con=self.db_connection)
        self.__add_feed_name(df, feed_df)
        return df

    def get_url_keyword_counts(self, min_count=100):
        print("Getting URL keyword counts...")
        # Update with values from the code.
        query = f"""SELECT uk.id, l.name, keyword, count
                    FROM url_keyword uk
                    JOIN (SELECT url_keyword_id, count(*) count
                          FROM article_url_keyword_map
                          GROUP BY url_keyword_id) as keyword_count
                    ON uk.id = keyword_count.url_keyword_id
                    JOIN language l ON l.id = language_id
                    WHERE count > {min_count}
                    AND topic_id is NULL
                    AND keyword not in (
                                        "news",
                                        "i",
                                        "nyheter",
                                        "article",
                                        "nieuws",
                                        "aktuell",
                                        "artikel",
                                        "wiadomosci",
                                        "actualites",
                                        "cronaca",
                                        "nyheder",
                                        "jan",
                                        "feb",
                                        "mar",
                                        "apr",
                                        "may",
                                        "jun",
                                        "jul",
                                        "aug",
                                        "sep",
                                        "oct",
                                        "nov",
                                        "dec"
                                        )
                    ORDER BY count DESC;
                """
        df = pd.read_sql(query, con=self.db_connection)
        return df

    def get_article_df_with_ids(self, feed_df, id_to_fetch: list[int]):
        print("Getting Articles with Ids...")
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



zeeguu/operations/report_generator/data_extractor.py [4:116]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def ms_to_mins(ms_time):
    return ms_time / 1000 / 60


class DataExtractor:
    def __init__(self, db_connection, DAYS_FOR_REPORT=7) -> None:
        self.DAYS_FOR_REPORT = DAYS_FOR_REPORT
        self.db_connection = db_connection

    def __add_feed_name(self, df, feed_df, column_with_id="feed_id"):
        df["Feed Name"] = df[column_with_id].apply(
            lambda x: (
                "No Feed"
                if pd.isna(x)
                else str(x) + " " + feed_df.loc[feed_df.id == x, "title"].values[0][:15]
            )
        )

    def run_query(self, query):
        df = pd.read_sql(query, con=self.db_connection)
        return df

    def get_article_topics_df(self, feed_df):
        print("Getting Article Topics...")
        query = f"""SELECT a.id, l.name Language, a.feed_id, t.title Topic, atm.origin_type
        FROM article a 
        INNER JOIN article_topic_map atm on a.id = atm.article_id 
        INNER JOIN topic t ON atm.topic_id = t.id
        INNER JOIN language l ON l.id = a.language_id
        WHERE a.published_time >= DATE_SUB(CURDATE(), INTERVAL {self.DAYS_FOR_REPORT} DAY)
        AND a.broken = 0"""
        df = pd.read_sql(query, con=self.db_connection)
        self.__add_feed_name(df, feed_df)
        return df

    def get_days_since_last_crawl(self):
        print("Getting Feeds Last Crawl Time...")
        query = f"""
            SELECT
                feed_id,
                f.title,
                DATEDIFF(CURDATE(), MAX(published_time)) days_since_last_article,
                DATEDIFF(CURDATE(), f.last_crawled_time) days_since_last_feed_crawl
            FROM
                article a
                JOIN feed f ON a.feed_id = f.id
            WHERE
                f.deactivated = 0
            GROUP by
                feed_id
            HAVING
                days_since_last_feed_crawl <= {self.DAYS_FOR_REPORT}
            ORDER BY
                days_since_last_article DESC;
        """
        df = pd.read_sql(query, con=self.db_connection)
        return df

    def get_article_df(self, feed_df):
        print("Getting Articles...")
        query = f"""SELECT a.*, l.name Language
        FROM article a     
        INNER JOIN language l ON l.id = a.language_id
        WHERE published_time >= DATE_SUB(CURDATE(), INTERVAL {self.DAYS_FOR_REPORT} DAY)
        AND a.broken = 0"""
        df = pd.read_sql(query, con=self.db_connection)
        self.__add_feed_name(df, feed_df)
        return df

    def get_url_keyword_counts(self, min_count=100):
        print("Getting URL keyword counts...")
        # Update with values from the code.
        query = f"""SELECT uk.id, l.name, keyword, count
                    FROM url_keyword uk
                    JOIN (SELECT url_keyword_id, count(*) count
                          FROM article_url_keyword_map
                          GROUP BY url_keyword_id) as keyword_count
                    ON uk.id = keyword_count.url_keyword_id
                    JOIN language l ON l.id = language_id
                    WHERE count > {min_count}
                    AND topic_id is NULL
                    AND keyword not in (
                                        "news",
                                        "i",
                                        "nyheter",
                                        "article",
                                        "nieuws",
                                        "aktuell",
                                        "artikel",
                                        "wiadomosci",
                                        "actualites",
                                        "cronaca",
                                        "nyheder",
                                        "jan",
                                        "feb",
                                        "mar",
                                        "apr",
                                        "may",
                                        "jun",
                                        "jul",
                                        "aug",
                                        "sep",
                                        "oct",
                                        "nov",
                                        "dec"
                                        )
                    ORDER BY count DESC;
                """
        df = pd.read_sql(query, con=self.db_connection)
        return df

    def get_article_df_with_ids(self, feed_df, id_to_fetch: list[int]):
        print("Getting Articles with Ids...")
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



