import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api'; 

const api = {
    searchFragrances: async (query) => {
        try {
            const response = await axios.get(`${API_BASE_URL}/search`, {
                params: {q: query}
            });
            return response.data;
          } catch (error) {
            console.error('Error searching fragrances:', error);
            throw error;
        }
    },

    getFragrance: async (id) => {
        try {
            const response = await axios.get(`${API_BASE_URL}/fragrance/${id}`);
            return response.data;
          } catch (error) {
            console.error('Error getting fragrance details:', error);
            throw error;
        }
    },

    getSimilarFragrances: async (id) => {
        try {
            const response = await axios.get(`${API_BASE_URL}/fragrance/${id}/similar`);
            return response.data;
          } catch (error) {
            console.error('Error getting similar fragrances:', error);
            throw error;
        }
    }
};

export default api;