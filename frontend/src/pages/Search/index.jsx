import React, { useState, useEffect } from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import Header from '../../components/Header';
import FragranceCard from '../../components/FragranceCard';
import api from '../../services/api';
import './styles.css';

const SearchPage = () => {
    const [searchParams] = useSearchParams();
    const query = searchParams.get('q');
    const [results, setResults] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchResults = async () => {
            try {
                setLoading(true);
                const data = await api.searchFragrances(query);
                setResults(data.results || []);
                setError(null);
            } catch (err) {
                setError('Failed to search fragrances. Please try again.');
                setResults([]);
            } finally {
                setLoading(false);
            }
        };

        if (query && query.length >= 3) {
            fetchResults();
        } else {
            setLoading(false);
            setError('Please enter at least 3 characters.');
        }
            }, [query]);

        return (
            <div className="search-page">
                <Header />
                <div className="search-container">
                    <div className="search-header">
                        <h2 className="search-title">Search Results</h2>
                        <p className="search-query">Showing results for: <strong>{query}</strong></p>
                        <Link to="/" className="back-link">New Search</Link>
                    </div>

                    {loading ? (
                        <div className="loading-message">Searching fragrances...</div>
                    ) : error ? (
                        <div className="error-message">{error}</div>
                    ) : results.length === 0 ? (
                        <div className="no-results">
                            <p>No fragrances found matching "{query}".</p>
                        </div>
                    ) : (
                        <div className="results-grid">
                            {results.map((fragrance) => (
                                <FragranceCard key={fragrance.id} fragrance={fragrance} />
                            ))}
                        </div>
                    )}
                </div>
            </div>
        );
    };        
        
export default SearchPage;