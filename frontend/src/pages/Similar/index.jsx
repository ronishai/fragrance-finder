import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Header from '../../components/Header';
import FragranceCard from '../../components/FragranceCard';
import SimilarityList from '../../components/SimilarityList';
import api from '../../services/api';
import './styles.css';

const SimilarPage = () => {
    const { id } = useParams();
    const [data, setData] = useState({
        fragrance: null,
        similar: []
    });
    const [loading, setLoading] = useState(true); // Fixed function name
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchSimilarFragrances = async () => {
            try {
                setLoading(true);
                const result = await api.getSimilarFragrances(id);
                setData(result);
                setError(null);
            } catch (err) {
                setError('Failed to load similar fragrances. Please try again.');
                setData({ fragrance: null, similar: [] });
            } finally {
                setLoading(false);
            }
        };

        if (id) {
            fetchSimilarFragrances();
        }
    }, [id]);

    const { fragrance, similar } = data;

    return ( 
        <div className="similar-page">
            <Header />
            <div className="similar-container">
                <Link to="/" className="back-link">← New Search</Link>

                {loading ? (
                    <div className="loading-message">Loading fragrances...</div>
                ) : error ? (
                    <div className="error-message">{error}</div>
                ) : fragrance ? (
                    <>
                        <div className="source-fragrance">
                            <h2 className="similar-title">Similar to</h2>
                            <div className="fragrance-detail-card">
                                <div className="fragrance-detail-brand">{fragrance.brand}</div>
                                <div className="fragrance-detail-content">
                                    <h1 className="fragrance-detail-name">{fragrance.name}</h1>
                                    <h3 className="fragrance-detail-subtitle">{fragrance.brand}</h3>
                                    
                                    {fragrance.notes && (
                                        <div className="fragrance-detail-section">
                                            <h4>Notes</h4>
                                            <p className="fragrance-notes-list">
                                                {fragrance.notes.join(', ')}
                                            </p>
                                        </div>
                                    )}
                                    
                                    {fragrance.types && (
                                        <div className="fragrance-detail-section">
                                            <h4>Fragrance Types</h4>
                                            <div className="type-tags">
                                                {fragrance.types.map((type) => (
                                                    <span key={type} className="type-tag">{type}</span>
                                                ))}
                                            </div>
                                        </div>
                                    )}
                                </div>
                            </div>
                        </div>

                        <div className="similar-fragrances">
                            <h2 className="similar-title">
                                {similar.length > 0
                                ? 'You might also like these'
                                : 'No similar fragrances found'}
                            </h2>
                            <SimilarityList fragrances={similar} />
                        </div>
                    </>
                ) : (
                    <div className="not-found">
                        <h2>Fragrance not found</h2>
                        <p>The fragrance you're looking for doesn't exist or was removed.</p>
                    </div>
                )}
            </div>
        </div>
    );
};

export default SimilarPage;