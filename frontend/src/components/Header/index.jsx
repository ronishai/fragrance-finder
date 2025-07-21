import React from 'react';
import './styles.css';

const Header = () => {
    return (
        <header className="header">
            <div className="header-container">
                <h1 className="header-title">Fragrance Finder</h1>
                <p className="header-subtitlle">Find similar fragrances based on your favorite fragrances</p>
            </div>
        </header>
    );
};

export default Header;