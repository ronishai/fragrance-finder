import React from 'react';
import FragranceCard from '../FragranceCard';
import './styles.css';

const SimilarityList = ({ fragrances }) => {
    if (!fragrances || fragrances.length === 0) {
        return (
            <div className="no-results">
                <p>No similar fragrances found.</p>
            </div>
        );
    }

    return (
        <div className="similarity-list">
            {fragrances.map((fragrance) => (
                <FragranceCard
                    key={fragrance.id}
                    fragrance={fragrance}
                    similarity={fragrance.similarity}
                />
            ))}
        </div>
    );
};

export default SimilarityList;


