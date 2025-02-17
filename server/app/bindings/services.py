def services(binder):
    from app.Services.Books.ListAllBooksService import ListAllBooksService
    from app.Services.Books.FindBookByIdService import FindBookByIdService
    from app.Services.Books.CreateBookService import CreateBookService
    from app.Services.Lendings.ListLendingsService import ListLendingsService
    from app.Services.Lendings.FindLendingByIDService import FindLendingByIDService
    from app.Services.Lendings.CreateLendingService import CreateLendingService
    binder.bind(ListAllBooksService, to=ListAllBooksService)
    binder.bind(FindBookByIdService, to=FindBookByIdService)
    binder.bind(CreateBookService, to=CreateBookService)
    binder.bind(ListLendingsService, to=ListLendingsService)
    binder.bind(FindLendingByIDService, to=FindLendingByIDService)
    binder.bind(CreateLendingService, to=CreateLendingService)
