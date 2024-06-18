import React from 'react'
import styles from './product.module.css'
import Image from 'next/image'
import Link from 'next/link'


const Product_Card = ({product_data}) => {
  // console.log("******** " , product_data["images"][0]["image"])
  return (
    <div className={styles.productmain}>
    <div className={styles.productinnermain}>
        <div className={styles["producthead"]}>
            <div className={styles["productimage"]}>
                <Image width={2000} height={2000} alt='Logo' src={product_data["images"][0]["image"]}/>
            </div>
            <div className={styles["productbody"]}>
                  <div className={styles["productname"]}>{product_data["product_name"]}</div>
                <div className={styles["productabout"]}>{product_data["product_summary"]}</div>
                <div className={styles["productcategory"]}>
                {product_data["product_categories"].map((items) => (
                  <div key="category"> {items} </div>
                ))}
                </div>
            </div>
        </div>
        
    </div>
    </div>
  );
}

export default Product_Card
