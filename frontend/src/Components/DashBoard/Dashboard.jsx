import React, { useEffect, useState } from 'react';
import axios from 'axios';
import PostCard from '../PostCard/PostCard';
import './dashboard.css';

function Dashboard() {
    const [posts, setPosts] = useState([]);
    const [leaderboard, setLeaderboard] = useState([]);

    useEffect(() => {
        // Fetch posts
        const fetchPosts = async () => {
            try {
                const res = await axios.get('http://127.0.0.1:8000/api/posts/', {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('access_token')}`
                    }
                });
                setPosts(res.data);
            } catch (err) {
                console.error('Error fetching posts:', err);
            }
        };

        // Fetch leaderboard
        const fetchLeaderboard = async () => {
            try {
                const res = await axios.get('http://127.0.0.1:8000/api/leaderboard/', {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('access_token')}`
                    }
                });
                setLeaderboard(res.data);
            } catch (err) {
                console.error('Error fetching leaderboard:', err);
            }
        };

        fetchPosts();
        fetchLeaderboard();
    }, []);

    return (
        <div className="Dashboard">
            <h2>Leaderboard (Last 24h)</h2>
            <ul>
                {leaderboard.map(user => (
                    <li key={user.user__id}>
                        {user.user__username} — Karma: {user.total_karma}
                    </li>
                ))}
            </ul>

            <h2>Posts</h2>
            <div className="posts-list">
                {posts.map(post => (
                    <PostCard key={post.id} post={post} />
                ))}
            </div>
        </div>
    );
}

export default Dashboard;
