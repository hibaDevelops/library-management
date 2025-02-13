def services(binder):
    from app.Services.Books.ListAllBooksService import ListAllBooksService
    from app.Services.Books.FindBookByIdService import FindBookByIdService
    binder.bind(ListAllBooksService, to=ListAllBooksService)
    binder.bind(FindBookByIdService, to=FindBookByIdService)
