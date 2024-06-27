'use client';
import React, { useEffect, useState }  from 'react';
import Image from 'next/image';
import styles from './search_bar.module.css';

const SearchBar = () => {
  const [isSticky, setIsSticky] = useState(false);
  const [searchText, setSearchText] = useState('');
  useEffect(() => {
    const handleScroll = () => {
      setIsSticky(window.scrollY > 0);
    };

    window.addEventListener('scroll', handleScroll);
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  console.log("SearchBar component rendered"); // To check if the component is rendering

  const handleInputChange = (e) => {
    console.log("Input change detected");
    setSearchText(e.target.value);
    console.log("Current input value:", e.target.value);
  };

  const handleKeyPress = (e) => {
    console.log("Key press detected:", e.key);
    if (e.key === 'Enter') {
      console.log("Enter key pressed");
      handleSearch();
    }
  };

  const handleSearch = () => {
    console.log('Search triggered with text:', searchText);
  };

  const handleImageClick = () => {
    console.log("Image clicked");
    handleSearch();
  };

  return (
    <div className={isSticky ? styles.searchBarSticky : styles.searchBarNonSticky}>
      <div className={isSticky ? styles.searchBarMainSticky : styles.searchBarMain} >
          <Image
            src="/search.svg" // Ensure this path is correct and the image is in the public directory
            width={30}
            height={30}
            alt='Search'
          />
        <input
          type="text"
          placeholder="Enter your prompt or search for products/categories"
          value={searchText}
          onChange={handleInputChange}
          onKeyPress={handleKeyPress}
        />
      </div>
    </div>
  );
};

export default SearchBar;
