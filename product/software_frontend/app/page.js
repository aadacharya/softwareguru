import Image from "next/image";
import Link from "next/link";
import Header from "./_components/header/header";
import Footer from "./_components/footer/footer";
import styles from "./home.module.css"
import ProdcutHome from "./_components/product_home/product_home";


export default function Home() {
  return (
    <div className={styles.homeMain}>
      <Header/>
      <ProdcutHome/>
      <Footer/>
    </div>
      );
}
