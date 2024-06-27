import React from 'react'
import Image from 'next/image'
import Link from 'next/link'
import styles from './product_list.module.css'
import ProductCardBig from '../product_card_big/product_card_big'

const ProductList = async ({page_number}) => {
  const res = await fetch('http://127.0.0.1:8000/softwareguru/get_products?page=1');
    if (!res.ok) {
      console.error('Failed to fetch data:', res.statusText);
      return <div>Error: Failed to fetch data</div>;
    }
    const products_data = await res.json();
  return (
    <div className={styles.productListMain}>
      {products_data.map((product_data) => (
          <ProductCardBig product_data={product_data} key={product_data["product_unique_id"]}/>
        ))}
        <div className={styles.pageChange}>
          <div className={styles.previous}> &lt; Previous</div>    
          <div className={styles.next } >Next &gt;</div>    
          
          </div>    
    </div>
  )
}
export default ProductList