import Image from "next/image";
import Header from "./_components/header/header";
import Footer from "./_components/footer/footer";
import styles from './home.module.css'
import Link from "next/link";
import Product_Card from "./_components/product_card/product_card";
import Product_Page from "./_components/product_page/product_page";

export default function Home() {
  return (
    <div className={styles.homemain}>
      <Header/>
      <Product_Page product_unique_id={'feb414be-9d96-4ded-8377-49dfa8ccaa57'}/>
      {/* <Footer/> */}
    </div>
  );
}
