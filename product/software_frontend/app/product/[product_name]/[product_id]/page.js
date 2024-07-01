import React from "react";
import Image from "next/image";
import Link from "next/link";
import Header from "../../../_components/header/header";
import Footer from "../../../_components/footer/footer";
import styles from "./product_page.module.css"
import ProductPage from "../../../_components/product_page/poduct_page";


export default function Home({params}) {
  const product_unique_id = params.product_id
  const  product_name= params.product_name
  // const product_unique_id = "ceb36fda-ab6a-4f9c-8fd7-ea318c32560a"
  console.log("###########" , params)
  return (
    <div className={styles.homeMain}>
      <Header/>
      <ProductPage product_unique_id={product_unique_id} key={product_unique_id}/>
      <Footer/>
    </div>
      );
}

