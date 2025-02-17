def services(binder):
    from app.Services.Books.ListAllBooksService import ListAllBooksService
    from app.Services.Books.FindBookByIdService import FindBookByIdService
    from app.Services.Books.CreateBookService import CreateBookService
    binder.bind(ListAllBooksService, to=ListAllBooksService)
    binder.bind(FindBookByIdService, to=FindBookByIdService)
    binder.bind(CreateBookService, to=CreateBookService)
