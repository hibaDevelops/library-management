// src/routes.tsx
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Books from './pages/AllBooks';
import Borrowing from './pages/BorrowingRecords';
import Sales from './pages/SalesRecords';

const AppRoutes = () => {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/books" element={<Books />} />
            <Route path="/borrowing" element={<Borrowing />} />
            <Route path="/sales" element={<Sales />} />
        </Routes>
    );
};

export default AppRoutes;
