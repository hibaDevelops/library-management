import React, { useState, useEffect } from "react";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  Button,
  FormControl,
  InputLabel,
  MenuItem,
  Box,
  Select,
  IconButton,
  List,
  ListItem,
  ListItemText,
  Typography
} from "@mui/material";
import { Add, Remove } from "@mui/icons-material";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { LocalizationProvider, DatePicker } from "@mui/x-date-pickers";
import dayjs, { Dayjs } from "dayjs";

interface Borrower {
  id: number;
  name: string;
  phone: string;
  jamaat?: string;
}

interface Book {
  id: number;
  name: string;
}

interface IssueBookProps {
  open: boolean;
  onClose: () => void;
  books: Book[];
  onBookIssued: () => void;
}

const IssueBook = ({ open, onClose, books, onBookIssued }: IssueBookProps) => {
  const [borrowers, setBorrowers] = useState<Borrower[]>([]);
  const [selectedBorrowerId, setSelectedBorrowerId] = useState<string>("");
  const [borrowerJamaat, setBorrowerJamaat] = useState<string>("");
  const [borrowerPhone, setBorrowerPhone] = useState<string>("");
  const [issueDate, setIssueDate] = useState<Dayjs | null>(dayjs());
  const [returnDate, setReturnDate] = useState<Dayjs | null>(dayjs().add(7, "day"));
  const [selectedBooks, setSelectedBooks] = useState<{ id: number; name: string; quantity: number }[]>([]);
  const [searchTerm, setSearchTerm] = useState<string>("");
  const [searchResults, setSearchResults] = useState<Book[]>([]);
  const baseURL = "http://localhost:8080";

  useEffect(() => {
    if (open) {
      fetch(`${baseURL}/api/v1/borrowers`)
        .then((res) => res.json())
        .then((data) => setBorrowers(data.borrowers || []))
        .catch((error) => console.error("Error fetching borrowers:", error));

      setSelectedBooks(books.map((book) => ({ id: book.id, name: book.name, quantity: 1 })));
    }
  }, [open]);

  // ✅ Improved Search: Fetch books and sort by closest match
  useEffect(() => {
    if (searchTerm.length > 1) {
      fetch(`${baseURL}/api/v1/books?search=${searchTerm}`)
        .then((res) => res.json())
        .then((data) => {
          const sortedBooks = (data.books || [])
            .filter((book: Book) => book.name.toLowerCase().includes(searchTerm.toLowerCase()))
            .sort((a, b) => a.name.toLowerCase().indexOf(searchTerm.toLowerCase()) - b.name.toLowerCase().indexOf(searchTerm.toLowerCase())); // Sort by relevance

          setSearchResults(sortedBooks);
        })
        .catch((error) => console.error("Error fetching books:", error));
    } else {
      setSearchResults([]);
    }
  }, [searchTerm]);

  // ✅ Auto-fill Borrower Jama’at & Phone when selected
  const handleBorrowerChange = (borrowerId: string) => {
    setSelectedBorrowerId(borrowerId);
    const selectedBorrower = borrowers.find((b) => b.id.toString() === borrowerId);
    setBorrowerJamaat(selectedBorrower?.jamaat || "");
    setBorrowerPhone(selectedBorrower?.phone || "");
  };

  // ✅ Handle Book Issue Submission
  const handleIssueBook = async () => {
    const selectedBorrower = borrowers.find((b) => b.id.toString() === selectedBorrowerId);

    if (!selectedBorrower || selectedBooks.length === 0 || !issueDate || !returnDate) {
      alert("Please fill in all required fields.");
      return;
    }

    const newIssue = {
      books: selectedBooks,
      borrower_name: selectedBorrower.name,
      borrower_phone: selectedBorrower.phone,
      borrower_jamaat: borrowerJamaat,
      issue_date: issueDate.toISOString(),
      expected_return_date: returnDate.toISOString(),
    };

    try {
      const response = await fetch(`${baseURL}/api/v1/issue`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newIssue),
      });

      if (response.ok) {
        alert("Book(s) issued successfully!");
        onBookIssued();
        onClose();
      } else {
        alert("Failed to issue book.");
      }
    } catch (error) {
      console.error("Error issuing book:", error);
    }
  };

  // ✅ Handle book quantity increase/decrease
  const handleQuantityChange = (bookId: number, change: number) => {
    setSelectedBooks((prevBooks) =>
      prevBooks.map((book) =>
        book.id === bookId ? { ...book, quantity: Math.max(1, book.quantity + change) } : book
      )
    );
  };

  // ✅ Handle removing a book from the list
  const handleRemoveBook = (bookId: number) => {
    setSelectedBooks(selectedBooks.filter((book) => book.id !== bookId));
  };

  // ✅ Handle Book Selection
  const handleAddBook = (book: Book) => {
    if (!selectedBooks.some((b) => b.id === book.id)) {
      setSelectedBooks([...selectedBooks, { id: book.id, name: book.name, quantity: 1 }]);
    }
    setSearchTerm(""); // Clear search box
    setSearchResults([]);
  };

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>Issue Book(s)</DialogTitle>
      <DialogContent>
        <Box display="flex" flexDirection="column" gap={2}>
          <LocalizationProvider dateAdapter={AdapterDayjs}>

            {/* ✅ Search Box for Books */}
            <TextField
              label="Search for a book"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              fullWidth
            />

            {/* ✅ Display matching book suggestions from API */}
            {searchTerm && searchResults.length > 0 && (
              <Box sx={{ border: "1px solid #ddd", borderRadius: 1, padding: 1, marginTop: 1 }}>
                {searchResults.map((book) => (
                  <Button key={book.id} fullWidth onClick={() => handleAddBook(book)}>
                    {book.name}
                  </Button>
                ))}
              </Box>
            )}

            {/* ✅ Selected Books with Quantity Controls */}
            <List>
              {selectedBooks.map((book) => (
                <ListItem key={book.id} sx={{ display: "flex", justifyContent: "space-between" }}>
                  <ListItemText primary={book.name} secondary={`Quantity: ${book.quantity}`} />
                  <Box display="flex" alignItems="center">
                    <IconButton onClick={() => handleQuantityChange(book.id, -1)} disabled={book.quantity === 1}>
                      <Remove />
                    </IconButton>
                    <Typography>{book.quantity}</Typography>
                    <IconButton onClick={() => handleQuantityChange(book.id, 1)}>
                      <Add />
                    </IconButton>
                    <Button onClick={() => handleRemoveBook(book.id)} variant="outlined" color="error">
                      Remove
                    </Button>
                  </Box>
                </ListItem>
              ))}
            </List>

            {/* ✅ Borrower Selection */}
            <FormControl fullWidth>
              <InputLabel>Borrower Name</InputLabel>
              <Select value={selectedBorrowerId} onChange={(e) => handleBorrowerChange(e.target.value)}>
                {borrowers.map((borrower) => (
                  <MenuItem key={borrower.id} value={borrower.id.toString()}>
                    {borrower.name}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>

            {/* ✅ Auto-Filled Borrower Details */}
            <TextField label="Borrower Jama'at" value={borrowerJamaat} disabled fullWidth />
            <TextField label="Borrower Phone" value={borrowerPhone} disabled fullWidth />
               {/* ✅ Issue & Return Dates */}
               <DatePicker label="Issue Date" value={issueDate} onChange={(date) => setIssueDate(date)} />
            <DatePicker label="Expected Return Date" value={returnDate} onChange={(date) => setReturnDate(date)} />
          </LocalizationProvider>
        </Box>
      </DialogContent>

      <DialogActions>
        <Button onClick={onClose} variant="outlined">Cancel</Button>
        <Button onClick={handleIssueBook} variant="contained" sx={{ bgcolor: "lightgreen" }}>Issue</Button>
      </DialogActions>
    </Dialog>
  );
};

export default IssueBook;
