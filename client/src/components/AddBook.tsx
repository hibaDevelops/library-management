import React, { useState, useEffect } from "react";
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
  
  const [authors, setAuthors] = useState<{ id: number; name: string }[]>([]);
  const [publishers, setPublishers] = useState<{ id: number; name: string }[]>([]);

  // ✅ Fetch authors and publishers when modal opens
  useEffect(() => {
    if (open) {
      fetchAuthors();
      fetchPublishers();
    }
  }, [open]);

  const fetchAuthors = async () => {
    try {
      const response = await fetch("http://localhost:8080/api/v1/authors");
      if (response.ok) {
        const data = await response.json();
        setAuthors(data);
      }
    } catch (error) {
      console.error("Error fetching authors:", error);
    }
  };

  const fetchPublishers = async () => {
    try {
      const response = await fetch("http://localhost:8080/api/v1/publishers");
      if (response.ok) {
        const data = await response.json();
        setPublishers(data);
      }
    } catch (error) {
      console.error("Error fetching publishers:", error);
    }
  };

  // ✅ Handle book submission
  const handleAddBook = async () => {
    const newBook = {
      name: bookName,
      author_id: author || null, // Send author ID instead of object
      publisher_id: publisher || null, // Send publisher ID instead of object
      price: parseFloat(price) || 0,
      available_copies_in_library: parseInt(libraryCopies) || 0,
      available_copies_for_sale: parseInt(shopCopies) || 0,
      location: location || "Unknown",
      image_url: imageUrl || "",
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

        onClose();
        setTimeout(onBookAdded, 500);
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
              {authors.map((auth) => (
                <MenuItem key={auth.id} value={auth.id}>
                  {auth.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          {/* Dropdown for Publisher */}
          <FormControl fullWidth>
            <InputLabel>Publisher</InputLabel>
            <Select value={publisher} onChange={(e) => setPublisher(e.target.value)}>
              {publishers.map((pub) => (
                <MenuItem key={pub.id} value={pub.id}>
                  {pub.name}
                </MenuItem>
              ))}
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
