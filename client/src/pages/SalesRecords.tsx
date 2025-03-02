import { useState, useEffect } from "react";
import {
  AppBar, Toolbar, Typography, Button, Table, TableBody, TableCell,
  TableContainer, TableHead, TableRow, Paper
} from "@mui/material";
import "../App.css";

interface SaleRecord {
  id: number;
  receipt_number: string;
  book_name: string;
  client_name: string;
  client_jamaat: string;
  client_phone: string;
  quantity_sold: number;
  sale_date: string;
  amount_paid: number;
}

const SalesRecords = () => {
  const [sales, setSales] = useState<SaleRecord[]>([]);
  const baseURL = "http://localhost:8080"; // API base URL

  const fetchSalesRecords = async () => {
    try {
      console.log("Fetching sales records...");
      const response = await fetch(`${baseURL}/api/v1/sales`);
      const data = await response.json();

      console.log("Fetched sales records:", data);

      if (Array.isArray(data)) {
        setSales(data);
      } else {
        console.warn("Unexpected response format.");
      }
    } catch (error) {
      console.error("Error fetching sales records:", error);
    }
  };

  useEffect(() => {
    fetchSalesRecords();
  }, []);

  return (
    <div>
      {/* Navbar */}
      <AppBar position="static" sx={{ backgroundColor: "#ffffff", color: "black" }}>
        <Toolbar>
          
          <Typography variant="h6" sx={{ flexGrow: 1 }}>Sales Records</Typography>
        </Toolbar>
      </AppBar>

      {/* Sales Records Table */}
      <TableContainer component={Paper} sx={{ marginTop: 2, padding: 2 }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell><b>Receipt Number</b></TableCell>
              <TableCell><b>Book Name</b></TableCell>
              <TableCell><b>Client Name</b></TableCell>
              <TableCell><b>Client Jama'at</b></TableCell>
              <TableCell><b>Client Phone</b></TableCell>
              <TableCell><b>Quantities Sold</b></TableCell>
              <TableCell><b>Sale Date</b></TableCell>
              <TableCell><b>Amount Paid</b></TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {sales.length > 0 ? (
              sales.map((sale) => (
                <TableRow key={sale.id}>
                  <TableCell>{sale.receipt_number}</TableCell>
                  <TableCell>{sale.book_name}</TableCell>
                  <TableCell>{sale.client_name}</TableCell>
                  <TableCell>{sale.client_jamaat}</TableCell>
                  <TableCell>{sale.client_phone}</TableCell>
                  <TableCell>{sale.quantity_sold}</TableCell>
                  <TableCell>{sale.sale_date}</TableCell>
                  <TableCell>${sale.amount_paid.toFixed(2)}</TableCell>
                </TableRow>
              ))
            ) : (
              <TableRow>
                <TableCell colSpan={8} align="center">No sales records available</TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
};

export default SalesRecords;
