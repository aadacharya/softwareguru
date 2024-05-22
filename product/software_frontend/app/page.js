import Image from "next/image";
import Header from "./_components/header/header";
import Footer from "./_components/footer/footer";
import styles from './home.module.css'
import Link from "next/link";
import Product from "./_components/product_abstract/product";

export default function Home() {
  return (
    <div className={styles.homemain}>
      <Header/>
      <Product/>
      <Footer/>
    </div>
  );
}
