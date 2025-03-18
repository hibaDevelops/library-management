import { useState, useEffect } from "react";
import {
  AppBar, Toolbar, Typography, Button, Table, TableBody, TableCell,
  TableContainer, TableHead, TableRow, Paper
} from "@mui/material";
import "../App.css";

interface BorrowedBook {
  id: number;
  book_name: string;
  borrower_name: string;
  borrower_jamaat: string;
  borrower_phone: string;
  quantity_borrowed: number;
  issue_date: string;
  due_date: string;
  return_date?: string;
}

const BorrowedBooks = () => {
  const [borrowedBooks, setBorrowedBooks] = useState<BorrowedBook[]>([]);
  const baseURL = "http://localhost:8080"; // API base URL

  const fetchBorrowedBooks = async () => {
    try {
      console.log("Fetching borrowed books...");
      const response = await fetch(`${baseURL}/api/v1/borrowed-books`);
      const data = await response.json();

      console.log("Fetched borrowed books:", data);

      if (Array.isArray(data)) {
        setBorrowedBooks(data);
      } else {
        console.warn("Unexpected response format.");
      }
    } catch (error) {
      console.error("Error fetching borrowed books:", error);
    }
  };

  useEffect(() => {
    fetchBorrowedBooks();
  }, []);

  return (
    <div>
      {/* Navbar */}
      <AppBar position="static" sx={{ backgroundColor: "#ffffff", color: "black" }}>
        <Toolbar>
         
          <Typography variant="h6" sx={{ flexGrow: 1 }}>Borrowed Books</Typography>
        </Toolbar>
      </AppBar>

      {/* Borrowed Books Table */}
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
                  <TableCell>{book.book_name}</TableCell>
                  <TableCell>{book.borrower_name}</TableCell>
                  <TableCell>{book.borrower_jamaat}</TableCell>
                  <TableCell>{book.borrower_phone}</TableCell>
                  <TableCell>{book.quantity_borrowed}</TableCell>
                  <TableCell>{book.issue_date}</TableCell>
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
