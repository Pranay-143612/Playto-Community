import axios from 'axios';

const API = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/',
    headers: {
        'Content-Type': 'application/json',
    },
});

// For authenticated requests
export const setAuthToken = (token) => {
    if (token) {
        API.defaults.headers.common['Authorization'] = `Token ${token}`;
    } else {
        delete API.defaults.headers.common['Authorization'];
    }
};

// API calls
export const fetchPosts = () => API.get('posts/');
export const fetchComments = (postId) => API.get(`comments/?post=${postId}`);
export const createLike = (data) => API.post('like/', data);
export const fetchLeaderboard = () => API.get('leaderboard/');
export const createPost = (data) => API.post('posts/', data);

export default API;
