import React from 'react'
import styles from './header.module.css'
import Image from 'next/image'
import Link from 'next/link'

const Header = () => {
  return (
    <div className={styles.headermain}>
        <div className={styles["logo"]}>
            <Link href="/"> <Image width={200} height={200} src="/next.svg" alt="logo"/></Link>
        </div>
        <div className={styles["content"]}>
            <div>Top 10</div>
            <div>Products</div>
            <div>Community</div>

        </div>
        <div className={styles["member"]}>
            <div className={styles["old"]}> Sign In</div>
            <div className={styles["new"]}>Join Today</div>
        </div>

    </div>
  )
}

export default Header