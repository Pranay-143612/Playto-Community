import { useState } from 'react';
import { useAuth } from '@/contexts/AuthContext';
import { createPost } from '@/lib/localStorage';
import { Loader2 } from 'lucide-react';
import './CreatePost.css';

export const CreatePost = ({ onPostCreated }) => {
  const { session } = useAuth();
  const [content, setContent] = useState('');
  const [isExpanded, setIsExpanded] = useState(false);
  const [isPosting, setIsPosting] = useState(false);

  const getInitials = (name) => {
    return name
      .split(' ')
      .map(n => n[0])
      .join('')
      .toUpperCase()
      .slice(0, 2);
  };

  const handlePost = async () => {
    if (!content.trim() || !session) return;

    setIsPosting(true);
    await new Promise(resolve => setTimeout(resolve, 300));

    createPost({
      userId: session.userId,
      userName: session.name,
      userHeadline: session.headline,
      content: content.trim(),
    });

    setContent('');
    setIsExpanded(false);
    setIsPosting(false);
    onPostCreated();
  };

  return (
    <div className="card">
      <div className="card-content">
        <div className="post-header">
          <div className="avatar">
            <span className="avatar-fallback">
              {session ? getInitials(session.name) : 'U'}
            </span>
          </div>
          <div className="post-body">
            {!isExpanded ? (
              <button
                onClick={() => setIsExpanded(true)}
                className="start-post-btn"
              >
                Start a post...
              </button>
            ) : (
              <div className="expanded-post">
                <textarea
                  placeholder="What do you want to talk about?"
                  value={content}
                  onChange={(e) => setContent(e.target.value)}
                  className="post-textarea"
                  autoFocus
                />
                <div className="post-footer">
                  <p className="char-count">{content.length} / 3000 characters</p>
                  <div className="post-actions">
                    <button
                      className="btn-ghost"
                      onClick={() => {
                        setIsExpanded(false);
                        setContent('');
                      }}
                      disabled={isPosting}
                    >
                      Cancel
                    </button>
                    <button
                      className="btn-post"
                      onClick={handlePost}
                      disabled={!content.trim() || isPosting}
                    >
                      {isPosting ? (
                        <>
                          <Loader2 className="loader" />
                          Posting...
                        </>
                      ) : (
                        'Post'
                      )}
                    </button>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
