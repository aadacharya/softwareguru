'use client';

import React, { useEffect, useState } from 'react';
import Image from 'next/image';
import styles from './search_bar.module.css';
import { useRouter } from 'next/navigation';
import Spinner from '../spinner/spinner';

const SearchBar = () => {
  const router = useRouter();
  const [isSticky, setIsSticky] = useState(false);
  const [searchText, setSearchText] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsSticky(window.scrollY > 0);
    };

    window.addEventListener('scroll', handleScroll);
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);
  const handleInputChange = (e) => {
    setSearchText(e.target.value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };
  const handleSearch = async () => {
    try {
      setIsLoading(true);

      const response = await fetch(
        `http://127.0.0.1:8000/softwareguru/get_categories?prompt=${searchText}`
      );
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const categories = await response.json();
      console.log('Search results:', categories['categories'].join(','));
      router.push(`/${categories['categories'].join(',')}/1`); // Ensure to await router.push
      setIsLoading(false);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleImageClick = () => {
    console.log('Image clicked');
    handleSearch();
  };

  return (
    <div
      className={isSticky ? styles.searchBarSticky : styles.searchBarNonSticky}
    >
      <div
        className={isSticky ? styles.searchBarMainSticky : styles.searchBarMain}
      >
        <div className={styles.searchIcon} onClick={handleSearch}></div>
        <input
          type="text"
          placeholder="Enter your prompt or search for products/categories"
          value={searchText}
          onChange={handleInputChange}
          onKeyDown={handleKeyPress}
        />
        {isLoading && <Spinner className={styles.spinner} />}
      </div>
    </div>
  );
};

export default SearchBar;
