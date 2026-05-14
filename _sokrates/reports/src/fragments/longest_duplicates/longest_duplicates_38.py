zeeguu/core/model/article_summary_context.py [32:62]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @classmethod
    def find_by_bookmark(cls, bookmark):
        try:
            return cls.query.filter(cls.bookmark == bookmark).one()
        except sqlalchemy.orm.exc.NoResultFound:
            return None

    @classmethod
    def find_or_create(
        cls,
        session,
        bookmark,
        article,
        commit=True,
    ):
        try:
            return cls.query.filter(
                cls.bookmark == bookmark,
                cls.article == article,
            ).one()
        except sqlalchemy.orm.exc.NoResultFound or sqlalchemy.exc.InterfaceError:
            new = cls(
                bookmark,
                article,
            )
            session.add(new)
            if commit:
                session.commit()
            return new

    @classmethod
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



zeeguu/core/model/article_title_context.py [32:62]:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @classmethod
    def find_by_bookmark(cls, bookmark):
        try:
            return cls.query.filter(cls.bookmark == bookmark).one()
        except sqlalchemy.orm.exc.NoResultFound:
            return None

    @classmethod
    def find_or_create(
        cls,
        session,
        bookmark,
        article,
        commit=True,
    ):
        try:
            return cls.query.filter(
                cls.bookmark == bookmark,
                cls.article == article,
            ).one()
        except sqlalchemy.orm.exc.NoResultFound or sqlalchemy.exc.InterfaceError:
            new = cls(
                bookmark,
                article,
            )
            session.add(new)
            if commit:
                session.commit()
            return new

    @classmethod
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



