tools/report_generator/generate_report.py [681:722]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    result += f"""
            <h1 id="new-url-keywords">Newly url keywords without topics:</h1>
            <p>URL Keywords that occur more than 100 times in articles and are not mapped to a topic. They are language unique.<p>
            {get_url_keywords_table(pd_url_keywords) if DAYS_FOR_REPORT <= 7 else "<p>Skipped due to long period.</p>"}
            <br />
            <h1 id="inactive-feeds">Feed activity:</h1>
            {generate_html_table(pd_feed_innactivity_time)}
        </body>
    """

    output_filepath = f"report_zeeguu_{date_str}_d{DAYS_FOR_REPORT}.html"
    with open(
        os.path.join(
            FOLDER_FOR_REPORT_OUTPUT,
            output_filepath,
        ),
        "w",
        encoding="UTF-8",
    ) as f:
        f.write(result)

    print(f"File written to '{output_filepath}'.")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser("generate_plots_report")
    parser.add_argument(
        "number_of_days",
        nargs="?",
        default=7,
        help="Number of days from the current date that will be cnsidered for the report.",
        type=int,
    )
    args = parser.parse_args()
    DAYS_FOR_REPORT = args.number_of_days
    print(
        f"## Reporting for the last {DAYS_FOR_REPORT} days, today is: {datetime.datetime.now()}"
    )
    print(
        "################################################################################"
    )
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



zeeguu/operations/report_generator/generate_report.py [716:762]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    result += f"""
            <h1 id="feed-errors">Feed Errors:</h1>
            <p>Connection timeouts, HTTP errors, and other issues encountered while fetching feeds.</p>
            <p>{warning_crawl_range}</p>
            {get_feed_errors_table(feed_errors, feed_df)}
            <br />
            <h1 id="new-url-keywords">Newly url keywords without topics:</h1>
            <p>URL Keywords that occur more than 100 times in articles and are not mapped to a topic. They are language unique.<p>
            {get_url_keywords_table(pd_url_keywords) if DAYS_FOR_REPORT <= 7 else "<p>Skipped due to long period.</p>"}
            <br />
            <h1 id="inactive-feeds">Feed activity:</h1>
            {generate_html_table(pd_feed_innactivity_time)}
        </body>
    """

    output_filepath = f"report_zeeguu_{date_str}_d{DAYS_FOR_REPORT}.html"
    with open(
        os.path.join(
            FOLDER_FOR_REPORT_OUTPUT,
            output_filepath,
        ),
        "w",
        encoding="UTF-8",
    ) as f:
        f.write(result)

    print(f"File written to '{output_filepath}'.")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser("generate_plots_report")
    parser.add_argument(
        "number_of_days",
        nargs="?",
        default=7,
        help="Number of days from the current date that will be cnsidered for the report.",
        type=int,
    )
    args = parser.parse_args()
    DAYS_FOR_REPORT = args.number_of_days
    print(
        f"## Reporting for the last {DAYS_FOR_REPORT} days, today is: {datetime.datetime.now()}"
    )
    print(
        "################################################################################"
    )
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



