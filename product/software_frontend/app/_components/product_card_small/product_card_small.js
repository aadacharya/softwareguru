import React from "react";

import styles from './product_card_small.module.css'
import Image from "next/image";

const ProductCardSmall = ({product_data}) => {
  return (
    <div className={styles.productCardMain}>
      <div className={styles["productCardHead"]}>
        <div className={styles["productName"]}> {product_data["product_name"]}</div>
        {/* <div className={styles["ProductWebsite"]}> 
        <Image src="/website.svg" width={70} height={70} alt="Featured" />
        </div> */}
      </div>
      <div className={styles["productImage"]}>
      <Image width={3000} height={1000} alt='Logo' src={product_data["images"][0]["image"]}/>
      </div>
      <div className={styles["productItems"]}>
        <div className={styles["productCategories"]}>
          <div className={styles["productCategory"]}>{product_data["product_categories"][0]}</div>
          {/* <div className={styles["productCategory"]}>Data Analytics</div> */}
        </div>
        <div className={styles["productFeatured"]}>
          <Image src="/featured.svg" width={70} height={70} alt="Featured" />
        </div>
      </div>
    </div>
  );
};

export default ProductCardSmall;
