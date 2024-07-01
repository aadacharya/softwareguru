import React from "react";
import styles from "./product_home.module.css";
import SearchBar from "@/app/_components/search_bar/search_bar";
import ProductList from "@/app/_components/product_list/product_list";
import FeaturedProduct from "@/app/_components/featured_products/feature_product";
import Header from "@/app/_components/header/header";
import Footer from "@/app/_components/footer/footer";

const ProdcutHome = ({params}) => {
const categories_list = params.categories.split('%2C')
const page = params.page
console.log("****************** " , params)
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
          {/* <ProductList categories_list={[categories_list]} page_number={page}/> */}
          <ProductList categories_list={categories_list} page_number={page}/>
          <FeaturedProduct />
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default ProdcutHome;
