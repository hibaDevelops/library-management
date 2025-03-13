def services(binder):
    from app.Services.Books.ListAllBooksService import ListAllBooksService
    from app.Services.Books.FindBookByIdService import FindBookByIdService
    from app.Services.Books.CreateBookService import CreateBookService
    from app.Services.Lendings.ListLendingsService import ListLendingsService
    from app.Services.Lendings.FindLendingByIDService import FindLendingByIDService
    from app.Services.Lendings.CreateLendingService import CreateLendingService
    from app.Services.Lendings.RetrieveLendingService import RetrieveLendingService
    from app.Services.Clients.ListClientsService import ListClientsService
    from app.Services.Clients.FindClientByIDService import FindClientByIDService
    from app.Services.Clients.CreateClientService import CreateClientService
    from app.Services.Sales.ListSalesService import ListSalesService
    binder.bind(ListAllBooksService, to=ListAllBooksService)
    binder.bind(FindBookByIdService, to=FindBookByIdService)
    binder.bind(CreateBookService, to=CreateBookService)
    binder.bind(ListLendingsService, to=ListLendingsService)
    binder.bind(FindLendingByIDService, to=FindLendingByIDService)
    binder.bind(CreateLendingService, to=CreateLendingService)
    binder.bind(RetrieveLendingService, to=RetrieveLendingService)
    binder.bind(ListClientsService, to=ListClientsService)
    binder.bind(FindClientByIDService, to=FindClientByIDService)
    binder.bind(CreateClientService, to=CreateClientService)
    binder.bind(ListSalesService, to=ListSalesService)
