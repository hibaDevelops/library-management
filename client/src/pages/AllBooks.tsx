import { useState, useEffect } from "react";
import {
  AppBar, Toolbar, Typography, Button, Menu, MenuItem, Table, TableBody, TableCell,
  TableContainer, TableHead, TableRow, Paper, Checkbox
} from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import AddIcon from "@mui/icons-material/Add";
import SellIcon from "@mui/icons-material/ShoppingCart";
import IssueIcon from "@mui/icons-material/AssignmentTurnedIn";
import "../App.css";
import AddBook from "../components/AddBook";
import SellBook from "../components/SellBook";
import IssueBook from "../components/IssueBook";

interface Author {
  id: number;
  name: string;
}

interface Publisher {
  id: number;
  name: string;
}

interface Book {
  id: number;
  name: string;
  author: Author | null;
  location: string;
  available_copies_in_library: number;
  available_copies_for_sale: number;
  price: number;
  publisher: Publisher | null;
  image_url?: string;
}

const AllBooks = () => {
  const [openAddModal, setOpenAddModal] = useState(false);
  const [openSellModal, setOpenSellModal] = useState(false);
  const [openIssueModal, setOpenIssueModal] = useState(false);
  const [books, setBooks] = useState<Book[]>([]);
  const [selectedBooks, setSelectedBooks] = useState<Book[]>([]);
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const baseURL = "http://localhost:8080";

  useEffect(() => {
    fetchBooks();
  }, []);

  // ✅ Fetch books from API
  const fetchBooks = async () => {
    try {
      const response = await fetch(`${baseURL}/api/v1/books`);
      const data = await response.json();
      setBooks(data.books || []);
    } catch (error) {
      console.error("Error fetching books:", error);
    }
  };

  const handleMenuClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  // ✅ Handle book selection (Checkbox logic)
  const handleBookSelect = (book: Book) => {
    setSelectedBooks((prevSelected) =>
      prevSelected.some((b) => b.id === book.id)
        ? prevSelected.filter((b) => b.id !== book.id)
        : [...prevSelected, book]
    );
  };

  return (
    <div>
      <AppBar position="static" sx={{ backgroundColor: "#ffffff", color: "black" }}>
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>All Books</Typography>

          <Button
            aria-controls="simple-menu"
            aria-haspopup="true"
            onClick={handleMenuClick}
            startIcon={<MenuIcon />}
            sx={{ color: "black" }}
          >
            Collections
          </Button>
          <Menu anchorEl={anchorEl} open={Boolean(anchorEl)} onClose={handleMenuClose}>
            <MenuItem onClick={handleMenuClose}>Search By Author</MenuItem>
            <MenuItem onClick={handleMenuClose}>All Books</MenuItem>
          </Menu>

          <Button variant="contained" sx={{ bgcolor: "#8BC34A", color: "black", ml: 2 }}
            startIcon={<AddIcon />} onClick={() => setOpenAddModal(true)}>
            Add Book
          </Button>

          <Button variant="contained" sx={{ bgcolor: "#2196F3", color: "black", ml: 2 }}
            startIcon={<IssueIcon />} disabled={selectedBooks.length === 0}
            onClick={() => setOpenIssueModal(true)}>
            Issue Book
          </Button>

          <Button variant="contained" sx={{ bgcolor: "#FF9800", color: "black", ml: 2 }}
            startIcon={<SellIcon />} disabled={selectedBooks.length === 0}
            onClick={() => setOpenSellModal(true)}>
            Sell Book
          </Button>

          <AddBook open={openAddModal} onClose={() => setOpenAddModal(false)} onBookAdded={fetchBooks} />
          <SellBook open={openSellModal} onClose={() => setOpenSellModal(false)} books={selectedBooks} onBookSold={fetchBooks} />
          <IssueBook open={openIssueModal} onClose={() => setOpenIssueModal(false)} books={selectedBooks} onBookIssued={fetchBooks} />
        </Toolbar>
      </AppBar>

      <TableContainer component={Paper} sx={{ mt: 2, p: 2 }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell><b>Select</b></TableCell>
              <TableCell><b>Name</b></TableCell>
              <TableCell><b>Author</b></TableCell>
              <TableCell><b>Location</b></TableCell>
              <TableCell><b>Available Copies</b></TableCell>
              <TableCell><b>Available Copies in Shop</b></TableCell>
              <TableCell><b>Price</b></TableCell>
              <TableCell><b>Publisher</b></TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {books.map((book) => (
              <TableRow key={book.id}>
                <TableCell>
                  <Checkbox checked={selectedBooks.includes(book)} onChange={() => handleBookSelect(book)} />
                </TableCell>
                <TableCell>{book.name}</TableCell>
                <TableCell>{book.author ? book.author.name : "Unknown Author"}</TableCell>
                <TableCell>{book.location}</TableCell>
                <TableCell>{book.available_copies_in_library}</TableCell>
                <TableCell>{book.available_copies_for_sale}</TableCell>
                <TableCell>${book.price.toFixed(2)}</TableCell>
                <TableCell>{book.publisher ? book.publisher.name : "Unknown Publisher"}</TableCell>
              </TableRow>
            ))}
            {books.length === 0 && (
              <TableRow>
                <TableCell colSpan={8} align="center">No books available</TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
};

export default AllBooks;
