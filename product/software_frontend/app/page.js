import React from "react";
import styles from "./home.module.css";
import SearchBar from "./_components/search_bar/search_bar";
import ProductList from "./_components/product_list/product_list";
import FeaturedProduct from "./_components/featured_products/feature_product";
import Header from "./_components/header/header";
import Footer from "./_components/footer/footer";

const ProdcutHome = () => {
  return (
    <div className={styles.homeMain}>
      <Header />
      <div className={styles.productHomeMain}>
        <SearchBar />
        <h1>
          Find the AI tools you need from <span>20000</span> products to boost
          your productivity by 10x.
        </h1>
        <div className={styles.productHomeList}>
          <ProductList categories_list={[]} page_number={1}/>
          <FeaturedProduct />
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default ProdcutHome;
