import React from 'react';
import Header from '../../components/Header';
import SearchBar from '../../components/SearchBar';
import './styles.css';

const HomePage = () => {
    return (
        <div className="home-page">
            <Header />
            <div className="home-content">
                <h2 className="home-tagline">Find your next signature scent!</h2>
                <p className="home-description">Enter a fragrance you love, and we'll recommend similar scents you might enjoy.</p>
                <SearchBar />
            </div>
        </div>
    );
};

export default HomePage;