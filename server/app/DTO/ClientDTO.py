class ClientDTO:
    def __init__(
        self,
        id: int,
        firstname: str,
        lastname: str,
        phone: str,
        email: str,
        created_at: str,
        updated_at: str
    ):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'phone': self.phone,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    def __repr__(self):
        return f"ClientDTO(id={self.id}, name='{self.firstname}'')"
