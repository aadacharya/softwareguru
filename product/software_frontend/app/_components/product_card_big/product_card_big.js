import React from "react";
import Link from "next/link";
import Image from "next/image";
import styles from "./product_card_big.module.css";

const ProductCardBig = ({product_data}) => {
  return (
    <Link href={product_data["product_unique_id"]}>
      <div className={styles.productCardMain}>
        <div className={styles["productHead"]}>
          <div className={styles["productName"]}>
            <div className={styles["name"]}>{product_data["product_name"]}</div>
            <div className={styles["productLink"]}>
              <Link href={product_data["product_url"]}>
                <Image
                  src="/external_link.svg"
                  width={100}
                  height={100}
                  alt="Website"
                />
              </Link>
            </div>
          </div>
          <div className={styles["productRating"]}>
            <Image width={24} height={24} alt="Star" src="./star.svg" />
            <h1>{product_data["product_rating"]}/10</h1>
          </div>
        </div>
        <div className={styles["productImage"]}>
        <Image width={3000} height={1000} alt='Logo' src={product_data["images"][0]["image"]}/>
        </div>
        <div className={styles["productAbout"]}>
        {product_data["product_summary"]}
        </div>
        <div className={styles["productTail"]}>
          <div className={styles["productCategoires"]}>
          {product_data["product_categories"].map((items) => (
              <div key={items} className={styles["productCategory"]}> {items}</div>
                  ))}
          </div>
          <div className={styles["productFeatured"]}>
            <Image src="/featured.svg" width={70} height={70} alt="Featured" />
          </div>
        </div>
      </div>
    </Link>
  );
};

export default ProductCardBig;
