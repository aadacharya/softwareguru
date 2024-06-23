import React from 'react'
import Link from 'next/link'
import Image from 'next/image'
import styles from './featured_product.module.css'
import ProductCardSmall from '../product_card_small/product_card_small'

const FeaturedProduct = async () => {
  const res = await fetch('http://127.0.0.1:8000/softwareguru/get_products?page=1');
    if (!res.ok) {
      console.error('Failed to fetch data:', res.statusText);
      return <div>Error: Failed to fetch data</div>;
    }
    const products_data = await res.json();
  return (
    <div className={styles.featuredProductMain}>
      <h1>Featured Products</h1>
      {products_data.map((product_data) => (
          <Link key={product_data["product_unique_id"]}href={product_data["product_url"]}>
            <ProductCardSmall product_data={product_data} key={product_data["product_unique_id"]}/>
          </Link>
        ))}    
    </div>
  )
}

export default FeaturedProduct