"use client";
import React, { useState } from "react";
import Image from "next/image";
import styles from "./product_image_div.module.css";

const ProductImageDiv = ({ product_images }) => {
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  const handleClick = (index) => {
    setCurrentImageIndex(index);
  };
  const prodcut_image_lenght = product_images.length;
  return (
    <div className={styles.productImageDivMain}>
      <div className={styles["productImage"]}>
        <Image
          width={3000}
          height={1000}
          alt="Logo"
          src={product_images[currentImageIndex]["image"]}
        />
      </div>
      <div className={styles["productChange"]}>
      {Array.from({ length: prodcut_image_lenght }, (_, index) => (
        <div key={index} className={index === currentImageIndex? styles["productChangeBarActive"]: styles["productChangeBarDeactive"]} onClick={() => handleClick(index)}>
        </div>
      ))}
      </div>
    </div>
  );
};

export default ProductImageDiv;
