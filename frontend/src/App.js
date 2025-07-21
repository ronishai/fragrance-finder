import logo from './logo.svg';
import './App.css';
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import HomePage from './pages/Home';
import SearchPage from './pages/Search';
import SimilarPage from './pages/Similar';
import './App.css';  

function App() {
  return (
    <BrowserRouter>
      <div className="App">
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/search" element={<SearchPage />} />
        <Route path="/similar/:id" element={<SimilarPage />} />
      </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
