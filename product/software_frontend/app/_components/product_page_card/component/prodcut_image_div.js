'use client';
import React, { useState, useEffect, useRef } from 'react';
import Image from 'next/image';
import styles from './product_image_div.module.css';

const ProductImageDiv = ({ product_images, slideshowTime = 5 }) => {
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  const intervalRef = useRef(null);
  const product_image_length = product_images.length;

  const handleClick = (index) => {
    setCurrentImageIndex(index);
    resetInterval();
  };

  const resetInterval = () => {
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
    }
    intervalRef.current = setInterval(() => {
      setCurrentImageIndex((prevIndex) =>
        prevIndex === product_image_length - 1 ? 0 : prevIndex + 1
      );
    }, slideshowTime * 1000);
  };

  useEffect(() => {
    resetInterval();
    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
    };
  }, [product_image_length]);

  return (
    <div className={styles.productImageDivMain}>
      <div className={styles['productImage']}>
        <Image
          width={3000}
          height={1000}
          alt="Product Image"
          src={product_images[currentImageIndex]['image']}
        />
      </div>
      <div className={styles['productChange']}>
        {Array.from({ length: product_image_length }, (_, index) => (
          <div
            key={index}
            className={
              index === currentImageIndex
                ? styles['productChangeBarActive']
                : styles['productChangeBarDeactive']
            }
            onClick={() => handleClick(index)}
          ></div>
        ))}
      </div>
    </div>
  );
};

export default ProductImageDiv;
