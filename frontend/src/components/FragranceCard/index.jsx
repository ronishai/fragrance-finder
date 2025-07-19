import React from 'react';
import { Link } from 'react-router-dom';
import './styles.css';

const FragranceCard = ({ fragrance, similarity }) => {
    return (
        <div className="fragrance-card">
            <div className="fragrance-image">
                {fragrance.brand}
            </div>
            <div className="fragrance-details">
                <h3 className="fragramce-name">{fragrance.name}</h3>
                <p className="fragrance-brand">{fragrance.brand}</p>

                {fragrance.notes && (
                    <p className='fragrance-notes'>
                        <strong>Key Notes:</strong>
                        {fragrance.notes.slice(0, 4).join(', ')}
                        {fragrance.notes.length > 4 ? '...' : ''}
                    </p>
                )}

                {similarity !== undefined && (
                    <div className="similarity-badge">
                        {similarity}% match
                    </div>
                )}
                
                {fragrance.id && (
                    <Link to={`/similar/${fragrance.id}`} className="view-button">
                        View Similar
                    </Link>
                )}
            </div>
        </div>
    );
};

export default FragranceCard;