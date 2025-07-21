import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './styles.css';

const SearchBar = () => {
    const [query, setQuery] = useState('');
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        if (query.trim().length >= 3) {
            navigate(`/search?q=${encodeURIComponent(query.trim())}`);
        }
    };

    return (
        <div className="search-container">
            <form onSubmit={handleSubmit} className="search-form">
                <input
                    type="text"
                    className="search-input"
                    placeholder="Enter a fragrance name"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    minLength={3}
                    required
                />
                <button type="submit" className="search-button">
                    Find Similar
                </button>
            </form>
        </div>
    );
};

export default SearchBar;