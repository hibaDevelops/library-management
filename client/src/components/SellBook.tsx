import React, { useState, useEffect } from "react";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  Button,
  Box,
  FormControl,
  InputLabel,
  Select,
  MenuItem
} from "@mui/material";
import { DatePicker, LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import dayjs, { Dayjs } from "dayjs";

interface Client {
  id: number;
  name: string;
  phone: string;
}

interface SellBookProps {
  open: boolean;
  onClose: () => void;
  books: { name: string; price: number }[];
  onBookSold: () => void;
}

const SellBook = ({ open, onClose, books, onBookSold }: SellBookProps) => {
  const [clients, setClients] = useState<Client[]>([]);
  const [selectedClient, setSelectedClient] = useState<Client | null>(null);
  const [selectedBook, setSelectedBook] = useState<{ name: string; price: number } | null>(null);
  const [copiesToSell, setCopiesToSell] = useState<number>(1);
  const [purchaseDate, setPurchaseDate] = useState<Dayjs | null>(dayjs());
  const [discount, setDiscount] = useState<number>(0);

  useEffect(() => {
    // ✅ Fetch clients from API
    const fetchClients = async () => {
      try {
        const response = await fetch("http://localhost:8080/api/v1/clients");
        const data = await response.json();
        setClients(data.clients || []);
      } catch (error) {
        console.error("Error fetching clients:", error);
      }
    };

    if (open) {
      fetchClients();
    }
  }, [open]);

  const handleSellBook = async () => {
    if (!selectedClient || !selectedBook || !purchaseDate || copiesToSell <= 0) {
      alert("Please fill in all required fields!");
      return;
    }

    const sellData = {
      book_name: selectedBook.name,
      client_id: selectedClient.id,
      copies_sold: copiesToSell,
      purchase_date: purchaseDate.toISOString(),
      price: selectedBook.price,
      discount: discount,
    };

    try {
      const response = await fetch("http://localhost:8080/api/v1/sales", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(sellData),
      });

      if (response.ok) {
        alert("Book sold successfully!");
        onBookSold(); // Refresh book data
        onClose(); // Close modal
      } else {
        alert("Failed to sell book.");
      }
    } catch (error) {
      console.error("Error selling book:", error);
    }
  };

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>Sell Book</DialogTitle>
      <DialogContent>
        <Box display="grid" gap={2} mt={2}>
          {/* Book Select Dropdown */}
          <FormControl fullWidth>
            <InputLabel>Book Name</InputLabel>
            <Select
              value={selectedBook ? selectedBook.name : ""}
              onChange={(e) => {
                const book = books.find((b) => b.name === e.target.value) || null;
                setSelectedBook(book);
              }}
            >
              {books.map((book, index) => (
                <MenuItem key={index} value={book.name}>
                  {book.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          {/* Client Select Dropdown */}
          <FormControl fullWidth>
            <InputLabel>Client Name</InputLabel>
            <Select
              value={selectedClient ? selectedClient.id : ""}
              onChange={(e) => {
                const clientId = Number(e.target.value); // Convert to number
                const client = clients.find((c) => c.id === clientId) || null;
                setSelectedClient(client);
              }}
            >
              {clients.map((client) => (
                <MenuItem key={client.id} value={client.id}>
                  {client.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          {/* Auto-filled Client Phone */}
          <TextField label="Client Phone" value={selectedClient?.phone || ""} disabled fullWidth />

          {/* Copies to Sell */}
          <TextField
            label="Copies to Sell"
            type="number"
            value={copiesToSell}
            onChange={(e) => setCopiesToSell(Math.max(1, Number(e.target.value)))} // Prevent negative numbers
            fullWidth
          />

          {/* Purchase Date */}
          <LocalizationProvider dateAdapter={AdapterDayjs}>
            <DatePicker
              label="Purchase Date"
              value={purchaseDate}
              onChange={(date) => setPurchaseDate(date)}
            />
          </LocalizationProvider>

          {/* Auto-filled Price */}
          <TextField label="Price" type="number" value={selectedBook?.price || ""} disabled fullWidth />

          {/* Discount */}
          <TextField
            label="Discount"
            type="number"
            value={discount}
            onChange={(e) => setDiscount(Math.max(0, Number(e.target.value)))} // Prevent negative discounts
            fullWidth
          />
        </Box>
      </DialogContent>

      {/* Action Buttons */}
      <DialogActions>
        <Button onClick={onClose} variant="outlined">Cancel</Button>
        <Button onClick={handleSellBook} variant="contained" sx={{ bgcolor: "lightgreen" }}>
          Sell
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default SellBook;
