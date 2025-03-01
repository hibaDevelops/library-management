// src/routes.tsx
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Books from './pages/AllBooks';
import Authors from './pages/BorrowingRecords';
import Publishers from './pages/SalesRecords';

const AppRoutes = () => {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/books" element={<Books />} />
            <Route path="/authors" element={<Authors />} />
            <Route path="/publishers" element={<Publishers />} />
        </Routes>
    );
};

export default AppRoutes;
