import React from 'react'
import Image from 'next/image'
import Link from 'next/link'
import styles from './header.module.css'

const Header = () => {
  return (
    <div className={styles.headerMain}>
        <div className={styles["headerLogo"]}> 
        <Image src ="./vercel.svg" width={100} height={100} alt="Logo"></Image>
        </div>
        <div className={styles["headerComponent"]}> 
        <div className={styles["headerComponentEach"]}> Products </div>
        <div className={styles["headerComponentEach"]}> Categories </div>
        <div className={styles["headerComponentEach"]}> Blogs </div>
    </div>
        <div className={styles["headerMember"]}> 
        <div className={styles["signin"]}>Sign In</div>
        <div className={styles["getstarted"]}>Get Started</div>
        </div>
    </div>
  )
}

export default Header
