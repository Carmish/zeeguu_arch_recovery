tools/ml/cefr_trainers/train_cefr_classifiers.py [221:267]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    log("=" * 80)

    # Get training data
    X, y, weights = get_training_data(language_code, include_simplified)
    if X is None:
        log(f"Skipping {language_code} - no training data")
        return None

    # Train model
    clf, accuracy = train_classifier(X, y, weights)

    # Save model
    save_model(clf, language_code)

    log(f"\n✓ Training complete for {language_code} (accuracy: {accuracy:.3f})")
    return accuracy


def train_all_languages(include_simplified=True):
    """
    Train classifiers for all languages with sufficient data.

    Args:
        include_simplified: Whether to include simplified articles
    """
    # Get all languages with LLM-assessed articles
    languages_query = (
        db_session.query(Language)
        .join(Article)
        .filter(Article.cefr_level.isnot(None), Article.broken == 0)
        .distinct()
    )

    languages = languages_query.all()

    log(f"Found {len(languages)} languages with CEFR-assessed articles")
    log("")

    results = {}
    for language in languages:
        accuracy = train_language(language.code, include_simplified)
        if accuracy:
            results[language.code] = accuracy
        log("")

    # Summary
    log("=" * 80)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



tools/ml/cefr_trainers/train_cefr_classifiers_with_frequency.py [297:343]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    log("=" * 80)

    # Get training data
    X, y, weights = get_training_data(language_code, include_simplified)
    if X is None:
        log(f"Skipping {language_code} - no training data")
        return None

    # Train model
    clf, accuracy = train_classifier(X, y, weights)

    # Save model
    save_model(clf, language_code)

    log(f"\n✓ Training complete for {language_code} (accuracy: {accuracy:.3f})")
    return accuracy


def train_all_languages(include_simplified=True):
    """
    Train classifiers for all languages with sufficient data.

    Args:
        include_simplified: Whether to include simplified articles
    """
    # Get all languages with LLM-assessed articles
    languages_query = (
        db_session.query(Language)
        .join(Article)
        .filter(Article.cefr_level.isnot(None), Article.broken == 0)
        .distinct()
    )

    languages = languages_query.all()

    log(f"Found {len(languages)} languages with CEFR-assessed articles")
    log("")

    results = {}
    for language in languages:
        accuracy = train_language(language.code, include_simplified)
        if accuracy:
            results[language.code] = accuracy
        log("")

    # Summary
    log("=" * 80)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



