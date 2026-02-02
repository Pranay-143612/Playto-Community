import React from 'react';
import './postcard.css';

function PostCard({ post }) {
    return (
        <div className="post">
            <div className="author">{post.author.username}</div>
            <div className="meta">
                {new Date(post.created_at).toLocaleString()}
            </div>
            <div className="content">{post.content}</div>
            <div className="post-stats">
                <span>Likes: {post.like_count}</span> |{' '}
                <span>Comments: {post.comment_count}</span>
            </div>
        </div>
    );
}

export default PostCard;
