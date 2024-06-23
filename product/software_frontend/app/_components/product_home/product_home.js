import React from 'react'
import styles from './product_home.module.css'
import SearchBar from '../search_bar/search_bar'
import ProductList from '../product_list/product_list'
import FeaturedProduct from '../featured_products/feature_product'

const ProdcutHome = () => {
  return (
    <div className={styles.productHomeMain}>
        <SearchBar/>
        <h1>Find the top tools from <span>20000</span> products to boost your productivity by 10x in our platform. </h1>
        <div className={styles.productHomeList}>
          <ProductList/>
          <FeaturedProduct/>
        </div>
    </div>
  )
}

export default ProdcutHome