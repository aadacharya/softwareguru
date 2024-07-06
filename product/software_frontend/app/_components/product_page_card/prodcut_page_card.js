import React from 'react';
import Image from 'next/image';
import styles from './product_page_card.module.css';
import ProductImageDiv from './component/prodcut_image_div';
import Link from 'next/link';

const ProductPageCard = async ({ product_unique_id }) => {
  const res = await fetch(
    'http://127.0.0.1:8000/softwareguru/get_product?product_unique_id=' +
      product_unique_id
  );
  if (!res.ok) {
    console.error('Failed to fetch data:', res.statusText);
    return <div>Error: Failed to fetch data</div>;
  }
  const product_data = await res.json();

  return (
    <div className={styles.productPageCardMain}>
      <div className={styles['productPageCardHead']}>
        <div className={styles['productPageCardHeadList']}>
          <div className={styles['productPageCardHeadName']}>
            {' '}
            {product_data['product_name']}
          </div>
        </div>
        <div className={styles['productPageCardHeadRating']}>
          <Image width={24} height={24} alt="Star" src="/star.svg" />
          <h1>{product_data['product_rating']}/10</h1>
        </div>
      </div>
      <ProductImageDiv product_images={product_data['images']} />
      <div className={styles['productPageCardHeadCategories']}>
        {product_data['product_categories'].map((items) => (
          <div key={items} className={styles['productPageCardHeadCategory']}>
            <Link href={`/${items}/1`}>{items}</Link>
          </div>
        ))}
      </div>
      <div className={styles['']}></div>
      <div className={styles['']}></div>
      <div className={styles['productPageCardProCon']}>
        <div className={styles['productPageCardPros']}>
          <h1>PROS</h1>
          {product_data['product_pros'].map((items) => (
            <li key={items}> {items}</li>
          ))}
        </div>
        <div className={styles['productPageCardCons']}>
          <h1>CONS</h1>
          {product_data['product_cons'].map((items) => (
            <li key={items}> {items}</li>
          ))}
        </div>
      </div>
      <div className={styles['productPageCardDescription']}>
        <h1> Product Description </h1>
        <h2> {product_data['product_summary']} </h2>
      </div>
      <div className={styles['productPageCardUseCase']}>
        <h1> Use Cases </h1>
        {product_data['product_usecases'].map((items) => (
          <div key={items['usecase']}>
            <li> {items['usecase']}: </li>
            <h2> {items['details']} </h2>
          </div>
        ))}
      </div>
      <div className={styles['productPageCardToolFor']}>
        <h1> Tool For </h1>
        {product_data['product_toolfor'].map((items) => (
          <div key={items['target']}>
            <li> {items['target']}: </li>
            <h2> {items['details']} </h2>
          </div>
        ))}
      </div>
      <div className={styles['']}></div>
    </div>
  );
};

export default ProductPageCard;
