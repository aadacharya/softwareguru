"use client"
import React from 'react'
import styles from './product_home.module.css'
import SearchBar from '../_components/search_bar/search_bar'
import ProductList from '../_components/product_list/product_list'
import FeaturedProduct from '../_components/featured_products/feature_product'
import Header from '../_components/header/header'
import Footer from '../_components/footer/footer'
import { useSearchParams } from 'next/navigation'

const ProdcutHome = () => {
  const params = useSearchParams()
  const categories_list = params.get("categories_list")
  console.log("------> ",categories_list)

  return (
    <div className={styles.homeMain}>
      <Header/>
      <div className={styles.productHomeMain}>
          <SearchBar/>
          <h1>Find the AI tools you need from <span>20000</span> products to boost your productivity by 10x. </h1>
          <div className={styles.productHomeList}>
          <ProductList categories_list={[categories_list]}/>
            <FeaturedProduct/>
          </div>
      </div>
      <Footer/>
    </div>
  )
}

export default ProdcutHome