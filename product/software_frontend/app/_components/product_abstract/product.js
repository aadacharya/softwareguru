import React from 'react'
import styles from './product.module.css'
import Image from 'next/image'
import Link from 'next/link'


const Product = () => {
  return (
    <div className={styles.productmain}>
    <div className={styles.productinnermain}>
        <div className={styles["producthead"]}>
            <div className={styles["productimage"]}>
                <Image width={200} height={200} alt='Logo' src="https://images.g2crowd.com/uploads/product/image/large_detail/large_detail_9e8e86037198aef6f46b0cfb68bf9b30/kbuilding.jpeg"/>
            </div>
            <div className={styles["productbody"]}>
                <div className={styles["productname"]}>Human Interest 401(k)</div>
                <div className={styles["productabout"]}>Human Interest makes it easy to offer a 401(k). With automated administration and built-in investment advising, we make it affordable to help your employees plan for their futures.</div>
                <div className={styles["productcategory"]}>
                <div><li>Other Infor Resellers</li></div>
                <div>Infor EAM Resellers</div>
                <div>Infor Consulting Services</div>
                <div></div>
                </div>
            </div>
        </div>
        
    </div>
    </div>
  );
}

export default Product
