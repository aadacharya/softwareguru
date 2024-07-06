import React from 'react';

import styles from './product_card_small.module.css';
import Image from 'next/image';
import Link from 'next/link';
import CategoryList from '../categoryList/categoryList';

const ProductCardSmall = ({ product_data }) => {
  const product_name = product_data['product_name'];
  const product_unique_id = product_data['product_unique_id'];
  const product_page_url = `/product/${encodeURIComponent(
    product_name
  )}/${encodeURIComponent(product_unique_id)}`;
  const categories_url = `/${product_data['product_categories'].join(',')}/1`;
  const product_redirect_url = product_data['product_featured']
    ? product_data['product_url']
    : product_page_url;
  return (
    <Link href={product_redirect_url}>
      <div className={styles.productCardMain}>
        <div className={styles['productCardHead']}>
          <div className={styles['productName']}>
            {product_data['product_name']}
          </div>
        </div>
        <div className={styles['productImage']}>
          <Image
            width={3000}
            height={1000}
            alt="Logo"
            src={product_data['images'][0]['image']}
          />
        </div>
        <div className={styles['productItems']}>
          <CategoryList
            categoryList={product_data['product_categories']}
            singleCategory={true}
          />
          <div className={styles['productFeatured']}>
            {product_data['product_featured'] && (
              <Image
                src="/featured.svg"
                width={70}
                height={70}
                alt="Featured"
              />
            )}
          </div>
        </div>
      </div>
    </Link>
  );
};

export default ProductCardSmall;
