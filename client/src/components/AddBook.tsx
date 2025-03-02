import React, { useState } from "react";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  Button,
  MenuItem,
  Select,
  InputLabel,
  FormControl,
  Box,
} from "@mui/material";

const AddBookModal = ({ open, onClose, onBookAdded }: { open: boolean; onClose: () => void; onBookAdded: () => void }) => {
  const [bookName, setBookName] = useState("");
  const [author, setAuthor] = useState("");
  const [publisher, setPublisher] = useState("");
  const [price, setPrice] = useState("");
  const [libraryCopies, setLibraryCopies] = useState("");
  const [shopCopies, setShopCopies] = useState("");
  const [location, setLocation] = useState("");
  const [imageUrl, setImageUrl] = useState("");

  // ✅ Handle book submission
  const handleAddBook = async () => {
    // ✅ Fix: Convert author and publisher to objects
    const newBook = {
      name: bookName,
      author: author ? { name: author } : null, // Fix null issue
      publisher: publisher ? { name: publisher } : null,
      price: parseFloat(price) || 0, // Default to 0 if empty
      available_copies_in_library: parseInt(libraryCopies) || 0,
      available_copies_for_sale: parseInt(shopCopies) || 0,
      location: location || "Unknown", // Default location if empty
      image_url: imageUrl || "", // Allow empty image URL
    };

    try {
      const response = await fetch("http://localhost:8080/api/v1/books", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newBook),
      });

      if (response.ok) {
        alert("Book added successfully!");

        // ✅ Clear form fields after successful submission
        setBookName("");
        setAuthor("");
        setPublisher("");
        setPrice("");
        setLibraryCopies("");
        setShopCopies("");
        setLocation("");
        setImageUrl("");

        onClose(); // Close modal FIRST
        setTimeout(onBookAdded, 500); // Delay book fetching for state update
      } else {
        alert("Failed to add book");
      }
    } catch (error) {
      console.error("Error adding book:", error);
    }
  };

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>Add New Book</DialogTitle>
      <DialogContent>
        <Box display="grid" gap={2} gridTemplateColumns="1fr 1fr">
          <TextField label="Book Name" value={bookName} onChange={(e) => setBookName(e.target.value)} fullWidth />
          {/* Dropdown for Author */}
          <FormControl fullWidth>
            <InputLabel>Author</InputLabel>
            <Select value={author} onChange={(e) => setAuthor(e.target.value)}>
              <MenuItem value="talha">Talha</MenuItem>
              <MenuItem value="Author2">Author 2</MenuItem>
            </Select>
          </FormControl>

          {/* Dropdown for Publisher */}
          <FormControl fullWidth>
            <InputLabel>Publisher</InputLabel>
            <Select value={publisher} onChange={(e) => setPublisher(e.target.value)}>
              <MenuItem value="Rabwah Test">Rabwah Test</MenuItem>
              <MenuItem value="Publisher2">Publisher 2</MenuItem>
            </Select>
          </FormControl>
          
          <TextField label="Price" type="number" value={price} onChange={(e) => setPrice(e.target.value)} fullWidth />
          <TextField label="Available Copies in Library" type="number" value={libraryCopies} onChange={(e) => setLibraryCopies(e.target.value)} fullWidth />
          <TextField label="Available Copies in Shop" type="number" value={shopCopies} onChange={(e) => setShopCopies(e.target.value)} fullWidth />
          <TextField label="Location" value={location} onChange={(e) => setLocation(e.target.value)} fullWidth />
          <TextField label="Image URL" value={imageUrl} onChange={(e) => setImageUrl(e.target.value)} fullWidth />
        </Box>
      </DialogContent>

      {/* Action Buttons */}
      <DialogActions>
        <Button onClick={onClose} variant="outlined">Cancel</Button>
        <Button onClick={handleAddBook} variant="contained" sx={{ bgcolor: "lightgreen" }}>Add Book</Button>
      </DialogActions>
    </Dialog>
  );
};

export default AddBookModal;
