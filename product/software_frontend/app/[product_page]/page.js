import Image from "next/image";
import Link from "next/link";
import Header from "../_components/header/header";
import Footer from "../_components/footer/footer";
import styles from "./product_page.module.css"
import ProductPage from "../_components/product_page/poduct_page";


export default function Home({ params}) {
    // console.log("Here is")
    // console.log(params.product_page)
  return (
    <div className={styles.homeMain}>
      <Header/>
      <ProductPage product_unique_id={params.product_page} key={params.product_page}/>
      <Footer/>
    </div>
      );
}
