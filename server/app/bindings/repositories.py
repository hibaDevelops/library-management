def repositories(binder):
    from app.Repositories.AuthorRepository import AuthorRepository
    from app.Repositories.BookRepository import BookRepository
    from app.Repositories.PublisherRepository import PublisherRepository
    binder.bind(AuthorRepository, to=AuthorRepository)
    binder.bind(BookRepository, to=BookRepository)
    binder.bind(PublisherRepository, to=PublisherRepository)
