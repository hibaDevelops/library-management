import { useState, useEffect } from 'react';
import {
  AppBar, Toolbar, Typography, Button, Menu, MenuItem, Table, TableBody, TableCell,
  TableContainer, TableHead, TableRow, Paper
} from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import AddIcon from '@mui/icons-material/Add';
import '../App.css';
import AddBook from "../components/AddBook"; 

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
  author: Author | null;  // ✅ Fix: Allow `null` values
  location: string;
  available_copies_in_library: number;
  available_copies_for_sale: number;
  price: number;
  publisher: Publisher | null; // ✅ Fix: Allow `null` values
  image_url?: string;
}

const AllBooks = () => {
  const [openModal, setOpenModal] = useState(false);
  const [books, setBooks] = useState<Book[]>([]);
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const baseURL = 'http://localhost:8080';

  // ✅ Fetch books from the backend
  const fetchBooks = async () => {
    try {
      const response = await fetch(`${baseURL}/api/v1/books`);
      const data = await response.json();
      
      // ✅ Fix: Ensure books is always an array
      if (data.books) {
        setBooks(Array.isArray(data.books) ? data.books : [data.books]);
      } else {
        setBooks([]); // Handle case where no books are available
      }
    } catch (error) {
      console.error("Error fetching books:", error);
    }
  };

  useEffect(() => {
    fetchBooks();
  }, []);

  const handleMenuClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  return (
    <div>
      {/* Navbar */}
      <AppBar position="static" sx={{ backgroundColor: "#ffffff", color: "black" }}>
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>All Books</Typography>

          {/* Dropdown Menu */}
          <Button 
            aria-controls="simple-menu" 
            aria-haspopup="true" 
            onClick={handleMenuClick} 
            startIcon={<MenuIcon />}
            sx={{ color: "black" }}
          >
            Collections
          </Button>
          <Menu
            id="simple-menu"
            anchorEl={anchorEl}
            open={Boolean(anchorEl)}
            onClose={handleMenuClose}
          >
            <MenuItem onClick={handleMenuClose}>Search By Author</MenuItem>
            <MenuItem onClick={handleMenuClose}>All Books</MenuItem>
          </Menu>

          {/* Add New Book Button */}
          <Button 
            variant="contained" 
            sx={{ backgroundColor: "#8BC34A", color: "black", marginLeft: 2 }}
            startIcon={<AddIcon />}
            onClick={() => setOpenModal(true)}
          >
            Add New Book
          </Button>
          <AddBook open={openModal} onClose={() => setOpenModal(false)} onBookAdded={fetchBooks} />
        </Toolbar>
      </AppBar>
      
      {/* Books Table */}
      <TableContainer component={Paper} sx={{ marginTop: 2, padding: 2 }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell><b>Image</b></TableCell>
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
            {books.length > 0 ? (
              books.map((book) => (
                <TableRow key={book.id}>
                  {/* Book Image */}
                  <TableCell>
                    <img 
                      src={book.image_url || "https://via.placeholder.com/50"} 
                      alt="Book Cover" 
                      style={{ height: 50 }} 
                    />
                  </TableCell>

                  {/* Book Details */}
                  <TableCell>{book.name}</TableCell>

                  {/* ✅ Fix: Handle `null` authors */}
                  <TableCell>{book.author ? book.author.name : "Unknown Author"}</TableCell>

                  <TableCell>{book.location}</TableCell>
                  <TableCell>{book.available_copies_in_library}</TableCell>
                  <TableCell>{book.available_copies_for_sale}</TableCell>
                  <TableCell>${book.price.toFixed(2)}</TableCell>

                  {/* ✅ Fix: Handle `null` publishers */}
                  <TableCell>{book.publisher ? book.publisher.name : "Unknown Publisher"}</TableCell>
                </TableRow>
              ))
            ) : (
              <TableRow>
                <TableCell colSpan={8} align="center">No books available</TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
}

export default AllBooks;
