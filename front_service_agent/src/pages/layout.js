import React, { useContext, useState, useEffect } from 'react'
import { useRouter } from 'next/router'
import 'tailwindcss/tailwind.css'

const Layout = ({ children }) => {
  const router = useRouter();
  const [email, setEmail] = useState(null);

  useEffect(() => {
    setEmail(window.localStorage.getItem('email'));
  }, []);

  const handleSignOut = () => {
    try {
      window.localStorage.removeItem('email');
      router.replace('/welcome')
      } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="flex flex-col min-h-screen bg-gray-100">
      <header className="py-6 bg-blue-600 text-white shadow-md">
        <div className="container mx-auto flex justify-between items-center px-6">
          <div className="text-2xl">Agent</div>
          {email && (
            <button
              className="bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
              onClick={handleSignOut}
            >
              Finish conversation
            </button>
          )}        
          </div>
      </header>
      <main className="flex-grow pt-6 pb-8">
        {children}
      </main>
      <footer className="bg-gray-200 text-center py-3 shadow-md">
        <p className="text-sm">© 2023 Diego Villafuerte. All rights reserved.</p>
      </footer>
    </div>
  )
}

export default Layout
