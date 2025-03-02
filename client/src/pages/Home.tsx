import React from 'react';
import libraryImage from '../assets/IMG_1231.jpg'; 

const Home = () => {
    return (
        <div style={{ textAlign: "center" }}>
            <h1>Welcome to Library Management</h1>
            <img 
                src={libraryImage} 
                alt="Library" 
                style={{
                    width: "80%", 
                    maxWidth: "600px", 
                    borderRadius: "10px", 
                    boxShadow: "0px 4px 8px rgba(0,0,0,0.2)" 
                }}
            />
        </div>
    );
};

export default Home;
