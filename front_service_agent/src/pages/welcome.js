import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import 'tailwindcss/tailwind.css';
import Layout from './layout';

export default function EmailInput() {
  const [email, setEmail] = useState('');
  const router = useRouter();

  const handleInputChange = (e) => {
    setEmail(e.target.value);
  };

  const handleSubmitEmail = (event) => {
    event.preventDefault();
    if (email.trim() !== '') {
      localStorage.setItem('email', email);
      router.push('/chat_hub');
    }
  };


  return (
    <Layout>
      <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
        <div className="max-w-md w-full space-y-8">
          <div className="flex items-center justify-center">
            <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
              Please provide your email
            </h2>
          </div>
          <form onSubmit={handleSubmitEmail} className="flex items-center justify-center mt-4">
            <input
              type="email"
              value={email}
              onChange={handleInputChange}
              placeholder="Type your email..."
              className="border border-gray-300 rounded-lg py-2 px-4 w-full"
            />
            <button
              type="submit"
              className="ml-2 px-4 py-2 border border-transparent text-base font-medium rounded-md text-white bg-blue-500 hover:bg-blue-600"
            >
              Submit
            </button>
          </form>
        </div>
      </div>
    </Layout>

  );
}
