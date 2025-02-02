def repositories(binder):
    from app.Repositories.BookRepository import BookRepository
    binder.bind(BookRepository, to=BookRepository)
