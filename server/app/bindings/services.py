def services(binder):
    from app.Services.Books.ListAllBooksService import ListAllBooksService
    binder.bind(ListAllBooksService, to=ListAllBooksService)
