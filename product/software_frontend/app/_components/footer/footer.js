"use client"
import React, { useEffect, useState }  from 'react';
import Link from 'next/link'
import Image from 'next/image'
import styles from './footer.module.css'
import { FaFacebookSquare , FaInstagramSquare , FaLinkedin, FaTwitterSquare , FaArrowRight} from "react-icons/fa";
import { FaSquareXTwitter } from "react-icons/fa6";

const Footer = () => {
  const [searchText, setSearchText] = useState('');
  const handleInputChange = (e) => {
    console.log("Input change detected");
    setSearchText(e.target.value);
    console.log("Current input value:", e.target.value);
  };
  return (
    <div className={styles.footerMain}>
      <div className={styles["footerNewsLetter"]}>
        <div className={styles["title"]}> Suscribe to Epic AI Newsletters</div>
        <div className={styles["email"]}>
          <input
            type="text"
            placeholder="Enter Your Email"
            value={searchText}
            onChange={handleInputChange}
          />
          <Link href={"/"}><FaArrowRight/></Link>
        </div>
      </div>
      <div className={styles[""]}></div>
      <div className={styles["footerSocial"]}>
      <div className={styles.socialItems}>
        <Link href={"/"}><FaFacebookSquare style={{ color: "white", fontSize: "1.5em" }}/></Link>
      </div>
      <div className={styles.socialItems}>
        <Link href={"/"}><FaInstagramSquare style={{ color: "white", fontSize: "1.5em" }}/></Link>
      </div>
      <div className={styles.socialItems}>
        <Link href={"/"}><FaLinkedin style={{ color: "white", fontSize: "1.5em" }}/></Link>
      </div>
      <div className={styles.socialItems}>
        <Link href={"/"}><FaSquareXTwitter style={{ color: "white", fontSize: "1.5em" }}/></Link>
      </div>
      </div>
    </div>
  )
}
export default Footer