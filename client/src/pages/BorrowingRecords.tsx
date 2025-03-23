import { useState, useEffect } from "react";
import {
  AppBar, Toolbar, Typography, Button, Table, TableBody, TableCell,
  TableContainer, TableHead, TableRow, Paper
} from "@mui/material";
import "../App.css";

interface BorrowedBook {
  id: number;
  book_id: number;
  client_id: number;
  lent_date: string;
  due_date: string;
  return_date?: string;
  book_name?: string;
  borrower_name?: string;
  borrower_jamaat?: string;
  borrower_phone?: string;
}

const BorrowedBooks = () => {
  const [borrowedBooks, setBorrowedBooks] = useState<BorrowedBook[]>([]);
  const baseURL = "http://localhost:8080";

  useEffect(() => {
    const fetchLendingsAndClients = async () => {
      try {
        const [lendingsRes, clientsRes] = await Promise.all([
          fetch(`${baseURL}/api/v1/lendings`),
          fetch(`${baseURL}/api/v1/clients`)
        ]);

        const [lendingsRaw, clientsRaw] = await Promise.all([
          lendingsRes.json(),
          clientsRes.json()
        ]);

        const lendings = Array.isArray(lendingsRaw) ? lendingsRaw : lendingsRaw.lendings || [];
        const clients = Array.isArray(clientsRaw) ? clientsRaw : clientsRaw.clients || [];

        console.log("Parsed lendings:", lendings);
        console.log("Parsed clients:", clients);

        const combined = lendings.map((lending: any) => {
          const client = clients.find((c: any) => Number(c.id) === Number(lending.client_id));
          console.log("Lending ID:", lending.id, "Client match:", client);

          return {
            ...lending,
            borrower_name: client ? `${client.firstname} ${client.lastname}` : "Unknown",
            borrower_phone: client?.phone || "N/A"
          };
        });

        console.log("Final merged list:", combined);
        setBorrowedBooks(combined);
      } catch (error) {
        console.error("Error fetching lendings/clients:", error);
      }
    };

    fetchLendingsAndClients();
  }, []);

  return (
    <div>
      <AppBar position="static" sx={{ backgroundColor: "#ffffff", color: "black" }}>
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>Borrowed Books</Typography>
        </Toolbar>
      </AppBar>

      <TableContainer component={Paper} sx={{ marginTop: 2, padding: 2 }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell><b>Book Name</b></TableCell>
              <TableCell><b>Borrower Name</b></TableCell>
              <TableCell><b>Borrower Jama'at</b></TableCell>
              <TableCell><b>Borrower Phone</b></TableCell>
              <TableCell><b>Quantities Borrowed</b></TableCell>
              <TableCell><b>Issue Date</b></TableCell>
              <TableCell><b>Due Date</b></TableCell>
              <TableCell><b>Return Date</b></TableCell>
              <TableCell><b>Actions</b></TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {borrowedBooks.length > 0 ? (
              borrowedBooks.map((book) => (
                <TableRow key={book.id}>
                <TableCell>{book.book?.name || "Unknown Book"}</TableCell>
                <TableCell>{book.client ? `${book.client.firstname} ${book.client.lastname}` : "Unknown"}</TableCell>
                <TableCell>{book.borrower_jamaat || "..."}</TableCell>
                <TableCell>{book.client?.phone || "N/A"}</TableCell>
                <TableCell>{1}</TableCell>
                <TableCell>{book.lent_date}</TableCell>
                <TableCell>{book.due_date}</TableCell>
                <TableCell>{book.return_date || "Not Returned"}</TableCell>
                <TableCell>
                  <Button
                    variant="contained"
                    sx={{ backgroundColor: "#FFEB3B", color: "black" }}
                  >
                    Return Book
                  </Button>
                </TableCell>
              </TableRow>

              ))
            ) : (
              <TableRow>
                <TableCell colSpan={9} align="center">No borrowed books available</TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
};

export default BorrowedBooks;
