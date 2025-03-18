def repositories(binder):
    from app.Repositories.AuthorRepository import AuthorRepository
    from app.Repositories.BookRepository import BookRepository
    from app.Repositories.ClientRepository import ClientRepository
    from app.Repositories.LendingRepository import LendingRepository
    from app.Repositories.PublisherRepository import PublisherRepository
    from app.Repositories.SaleRepository import SaleRepository
    binder.bind(AuthorRepository, to=AuthorRepository)
    binder.bind(BookRepository, to=BookRepository)
    binder.bind(ClientRepository, to=ClientRepository)
    binder.bind(LendingRepository, to=LendingRepository)
    binder.bind(PublisherRepository, to=PublisherRepository)
    binder.bind(SaleRepository, to=SaleRepository)
