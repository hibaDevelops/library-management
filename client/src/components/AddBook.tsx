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

const AddBookModal = ({ open, onClose }: { open: boolean; onClose: () => void }) => {
  const [author, setAuthor] = useState("");
  const [publisher, setPublisher] = useState("");

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>Add New Book</DialogTitle>
      <DialogContent>
        <Box display="grid" gap={2} gridTemplateColumns="1fr 1fr">
          <TextField label="Book Name" fullWidth />
          {/* Dropdown for Author */}
          <FormControl fullWidth>
            <InputLabel>Author</InputLabel>
            <Select value={author} onChange={(e) => setAuthor(e.target.value)}>
              <MenuItem value="Author1">Author 1</MenuItem>
              <MenuItem value="Author2">Author 2</MenuItem>
            </Select>
          </FormControl>

          {/* Dropdown for Publisher */}
          <FormControl fullWidth>
            <InputLabel>Publisher</InputLabel>
            <Select value={publisher} onChange={(e) => setPublisher(e.target.value)}>
              <MenuItem value="Publisher1">Publisher 1</MenuItem>
              <MenuItem value="Publisher2">Publisher 2</MenuItem>
            </Select>
          </FormControl>
          <TextField label="Price" type="number" fullWidth />

          <TextField label="Available Copies in Library" type="number" fullWidth />
          <TextField label="Available Copies in Shop" type="number" fullWidth />

          <TextField label="Location" fullWidth />
          <TextField label="URL" fullWidth />

          <Button variant="outlined" component="label">
            Upload Image
            <input type="file" hidden />
          </Button>
        </Box>
      </DialogContent>

      {/* Action Buttons */}
      <DialogActions>
        <Button onClick={onClose} variant="outlined">
          Cancel
        </Button>
        <Button onClick={onClose} variant="contained" sx={{ bgcolor: "lightgreen" }}>
          Add Book
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default AddBookModal;
