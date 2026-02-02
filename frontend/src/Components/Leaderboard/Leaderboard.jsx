import React from 'react';
import './Leaderboard.css';

function Leaderboard({ users }) {
    return (
        <div className="leaderboard">
            <h2>Top 5 Users (24h)</h2>
            <ul>
                {users.map((u, idx) => (
                    <li key={u.user__id}>
                        {idx + 1}. {u.user__username} — {u.total_karma} Karma
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Leaderboard;
