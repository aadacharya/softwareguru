import React from 'react'
import styles from './product_page.module.css'
import SearchBar from '../search_bar/search_bar'
import ProductPageCard from '../product_page_card/prodcut_page_card'
import FeaturedProduct from '../featured_products/feature_product'
import SimilarProduct from '../similar_products/similar_products'


const ProductPage = ({product_unique_id}) => {
    return (
    <div className={styles.productPageMain}>
        <SearchBar/>
          <div className={styles["productPageList"]}>
            <ProductPageCard product_unique_id={product_unique_id} key={product_unique_id}/>
            <FeaturedProduct/>
          </div>
          <SimilarProduct/>
        </div>
  )
}

export default ProductPage