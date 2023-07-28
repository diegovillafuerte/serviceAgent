import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import 'tailwindcss/tailwind.css';
import Layout from '../components/Layout'


export default function User_Hub() {
  const [userMessage, setUserMessage] = useState('');
  const [conversation, setConversation] = useState([]);
  const [loading, setLoading] = useState(false);
  const router = useRouter(); // Add this line

  // Add this useEffect
  useEffect(() => {
    const email = localStorage.getItem('email');
    if (!email) {
      router.push('/welcome');
    }
  }, []);


  const handleInputChange = (e) => {
    setUserMessage(e.target.value);
  };

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      event.preventDefault();
      document.getElementById('send-button').click();
    }
  };

  const handleSendMessage = () => {
    if (userMessage.trim() !== '') {
      const companyUserId = 7;  // Hard coded for now
      const email = localStorage.getItem('email');  // Retrieve the token from local storage
      setLoading(true);

  
      fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/chat/`, {  // Update with your actual API endpoint
        method: 'POST',
        body: JSON.stringify({ message: userMessage, email: email, companyUser_id: companyUserId }),
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then((response) => response.json())
        .then((data) => {
          // Update the conversation with the received response
          setConversation((prevConversation) => [
            ...prevConversation,
            { sender: 'user', message: userMessage },
            { sender: 'bot', message: data.result },
          ]);
        setLoading(false);

        })
        .catch((error) => {
          console.error('Error:', error);
          setLoading(false);

        });
  
      setUserMessage('');
    }
  };
  

  return (
    <Layout>
      <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
        <div className="max-w-md w-full space-y-8">
          <div className="flex items-center justify-center">
            <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
              Hi! How can I help?
            </h2>
          </div>
          <div className="mt-8 space-y-2">
            {conversation.map((message, index) => (
              <div
                key={index}
                className={`flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}
              >
                <span
                  className={`${
                    message.sender === 'user'
                      ? 'bg-blue-500 text-white'
                      : 'bg-gray-300 text-black'
                  } px-4 py-2 rounded-lg inline-block`}
                >
                  {message.message}
                </span>
              </div>
            ))}
          </div>
          <div className="flex items-center justify-center mt-4">
            <input
              type="text"
              value={userMessage}
              onChange={handleInputChange}
              onKeyDown={handleKeyDown}
              placeholder="Type your message..."
              className="border border-gray-300 rounded-lg py-2 px-4 w-full"
            />
            <button
              id="send-button"
              onClick={handleSendMessage}
              className="ml-2 px-4 py-2 border border-transparent text-base font-medium rounded-md text-white bg-blue-500 hover:bg-blue-600"
            >
              {loading ? (
                // This is a simple spinner using Tailwind CSS classes. You can customize it to your liking.
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
              ) : (
                'Send'
              )}
            </button>
          </div>
        </div>
      </div>
    </Layout>
  );
  
  }
