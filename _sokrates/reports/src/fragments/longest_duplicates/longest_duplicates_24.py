tools/report_generator/generate_report.py [16:95]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
FOLDER_FOR_REPORT_OUTPUT = os.environ.get(
    "FOLDER_FOR_REPORT_OUTPUT",
    os.path.join(pathlib.Path(__file__).parent.resolve(), "reports"),
)


def set_legend_to_right_side(ax):
    # https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))


def get_color_palette(n_items):
    if n_items <= 10:
        return sns.color_palette("tab10")
    else:
        return sns.color_palette("tab20")


def identify_repeating_patterns(article_df, sents_filtered_set: set):
    def normalize_sent(text: str):
        return text.lower().strip()

    def sent_count(text: str):
        return Counter(
            [
                normalize_sent(sent)
                for paragraph in text.split("\n\n")
                for sent in sent_tokenize(paragraph)
                if len(sent.strip()) > 10
            ]
        )

    def get_total_sent_counts(text_list: list[str]):
        total_counts = Counter()
        for text in tqdm(text_list, total=len(text_list)):
            total_counts += sent_count(text)
        return total_counts

    print("Evaluating new repeating patterns...")
    total_counts = get_total_sent_counts(article_df.content)
    sents_occur_more_than_10 = [
        [sent, count]
        for sent, count in total_counts.items()
        if count > 10 and sent not in sents_filtered_set
    ]
    return pd.DataFrame(sents_occur_more_than_10, columns=["Sent", "Count"])


def save_fig_params(filename):
    if not os.path.exists(FOLDER_FOR_REPORT_OUTPUT):
        os.mkdir(FOLDER_FOR_REPORT_OUTPUT)
    img_folder = os.path.join(FOLDER_FOR_REPORT_OUTPUT, "img")
    if not os.path.exists(img_folder):
        os.mkdir(img_folder)
    path_to_img = os.path.join(img_folder, filename)
    rel_path = os.path.join("img", filename)
    plt.savefig(path_to_img, bbox_inches="tight")
    plt.clf()
    return rel_path


def get_new_repeating_sents_table(pd_repeating_sents):
    return generate_html_table(pd_repeating_sents.sort_values("Count", ascending=False))


def get_url_keywords_table(pd_url_keywords_count):
    return generate_html_table(
        pd_url_keywords_count.sort_values("count", ascending=False)
    )


def get_rejected_sentences_table(total_deleted_sents):
    total_deleted_sents["Total"] = sum(total_deleted_sents.values())
    pd_deleted_sents = pd.DataFrame.from_dict(
        total_deleted_sents, orient="index"
    ).reset_index()
    pd_deleted_sents.columns = ["Reason", "Count"]
    return generate_html_table(pd_deleted_sents.sort_values("Count", ascending=False))
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



zeeguu/operations/report_generator/generate_report.py [16:95]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
FOLDER_FOR_REPORT_OUTPUT = os.environ.get(
    "FOLDER_FOR_REPORT_OUTPUT",
    os.path.join(pathlib.Path(__file__).parent.resolve(), "reports"),
)


def set_legend_to_right_side(ax):
    # https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))


def get_color_palette(n_items):
    if n_items <= 10:
        return sns.color_palette("tab10")
    else:
        return sns.color_palette("tab20")


def identify_repeating_patterns(article_df, sents_filtered_set: set):
    def normalize_sent(text: str):
        return text.lower().strip()

    def sent_count(text: str):
        return Counter(
            [
                normalize_sent(sent)
                for paragraph in text.split("\n\n")
                for sent in sent_tokenize(paragraph)
                if len(sent.strip()) > 10
            ]
        )

    def get_total_sent_counts(text_list: list[str]):
        total_counts = Counter()
        for text in tqdm(text_list, total=len(text_list)):
            total_counts += sent_count(text)
        return total_counts

    print("Evaluating new repeating patterns...")
    total_counts = get_total_sent_counts(article_df.content)
    sents_occur_more_than_10 = [
        [sent, count]
        for sent, count in total_counts.items()
        if count > 10 and sent not in sents_filtered_set
    ]
    return pd.DataFrame(sents_occur_more_than_10, columns=["Sent", "Count"])


def save_fig_params(filename):
    if not os.path.exists(FOLDER_FOR_REPORT_OUTPUT):
        os.mkdir(FOLDER_FOR_REPORT_OUTPUT)
    img_folder = os.path.join(FOLDER_FOR_REPORT_OUTPUT, "img")
    if not os.path.exists(img_folder):
        os.mkdir(img_folder)
    path_to_img = os.path.join(img_folder, filename)
    rel_path = os.path.join("img", filename)
    plt.savefig(path_to_img, bbox_inches="tight")
    plt.clf()
    return rel_path


def get_new_repeating_sents_table(pd_repeating_sents):
    return generate_html_table(pd_repeating_sents.sort_values("Count", ascending=False))


def get_url_keywords_table(pd_url_keywords_count):
    return generate_html_table(
        pd_url_keywords_count.sort_values("count", ascending=False)
    )


def get_rejected_sentences_table(total_deleted_sents):
    total_deleted_sents["Total"] = sum(total_deleted_sents.values())
    pd_deleted_sents = pd.DataFrame.from_dict(
        total_deleted_sents, orient="index"
    ).reset_index()
    pd_deleted_sents.columns = ["Reason", "Count"]
    return generate_html_table(pd_deleted_sents.sort_values("Count", ascending=False))
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



