zeeguu/api/endpoints/user_stats.py [1879:1917]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    for i in range(months):
        # Calculate month boundaries
        if i == 0:
            month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            month_end = now
        else:
            # Go back i months
            year = now.year
            month = now.month - i
            while month <= 0:
                month += 12
                year -= 1
            month_start = datetime(year, month, 1)
            # End is start of next month
            next_month = month + 1
            next_year = year
            if next_month > 12:
                next_month = 1
                next_year += 1
            month_end = datetime(next_year, next_month, 1)

        year_month = month_start.strftime("%Y-%m")
        is_current_month = (year_month == current_year_month)

        # Check cache
        cached = cache.get(year_month)
        use_cache = False

        if cached:
            if is_current_month:
                # For current month, use cache if less than 6 hours old
                cache_age = now - cached.computed_at
                if cache_age.total_seconds() < 6 * 3600:
                    use_cache = True
            else:
                # Historical months: always use cache
                use_cache = True

        if use_cache:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



zeeguu/api/endpoints/user_stats.py [2301:2335]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    for i in range(months):
        # Calculate month boundaries
        if i == 0:
            month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            month_end = now
        else:
            year = now.year
            month = now.month - i
            while month <= 0:
                month += 12
                year -= 1
            month_start = datetime(year, month, 1)
            next_month = month + 1
            next_year = year
            if next_month > 12:
                next_month = 1
                next_year += 1
            month_end = datetime(next_year, next_month, 1)

        year_month = month_start.strftime("%Y-%m")
        is_current_month = (year_month == current_year_month)

        # Check cache
        cached = cache.get(year_month)
        use_cache = False

        if cached:
            if is_current_month:
                cache_age = now - cached.computed_at
                if cache_age.total_seconds() < 6 * 3600:
                    use_cache = True
            else:
                use_cache = True

        if use_cache:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



