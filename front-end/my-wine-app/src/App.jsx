import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AboutPage from "./components/AboutPage";
import Home from "./components/Home";
import Footer from "./components/Footer";
import Navbar from "./components/Navbar";
import Wines from "./components/Wines";
import Login from './components/Login';
import { AuthProvider } from './components/AuthContext'; // Import the AuthProvider
import Reviews from './components/Reviews';

function App() {
  return (
    <Router>
      <AuthProvider> {/* Place AuthProvider as a parent of Routes */}
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/wines" element={<Wines />} />
          <Route path="/navbar" element={<Navbar />} />
          <Route path="/footer" element={<Footer />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/reviews" element={<Reviews />} />
          <Route path="/login" element={<Login />} />
        </Routes>
        <Footer />
      </AuthProvider> {/* Close AuthProvider */}
    </Router>
  );
}

export default App;