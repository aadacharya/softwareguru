import Image from "next/image";
import Header from "./_components/header/header";
import Footer from "./_components/footer/footer";
import styles from './home.module.css'
import Link from "next/link";
import Product_Card from "./_components/product_card/product_card";

export default function Home() {
  return (
    <div className={styles.homemain}>
      <Header/>
      <Product_Card/>
      <Footer/>
    </div>
  );
}
