import React from 'react'
import Image from 'next/image'
import Link from 'next/link'
import styles from './search_bar.module.css'

const SearchBar = () => {
  return (
    <div className={styles.searchBarMain}>
        <Image src="./search.svg" width={100} height={100} alt='Search'></Image>
        <input type="text"  placeholder="Enter you prompt or search for products/categories"/>
    </div>
  )
}

export default SearchBar