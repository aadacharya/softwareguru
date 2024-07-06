import React from 'react';
import Image from 'next/image';
import Link from 'next/link';
import styles from './product_list.module.css';
import ProductCardBig from '../product_card_big/product_card_big';

const ProductList = async ({ categories_list, page_number }) => {
  page_number = parseInt(page_number);
  const previousPage = Math.max(1, page_number - 1);
  const nextPage = page_number + 1;
  let categories_param =
    categories_list.length === 1 && categories_list[0] === 'home'
      ? ''
      : categories_list.join(',');
  console.log(
    '##### ------->',
    categories_list,
    page_number,
    previousPage,
    nextPage
  );
  if (categories_list.length === 0) {
    categories_list = ['home'];
  }
  let search_url = `http://127.0.0.1:8000/softwareguru/search?categories_list=${categories_param}&offset=${page_number}`;
  const res = await fetch(search_url, { cache: 'no-store' });
  if (!res.ok) {
    console.error('Failed to fetch data:', res.statusText);
    return <div>Error: Failed to fetch data</div>;
  }
  const products_data = await res.json();
  return (
    <div className={styles.productListMain}>
      {products_data.map((product_data) => (
        <ProductCardBig
          product_data={product_data}
          key={product_data['product_unique_id']}
        />
      ))}
      <div className={styles.pageChange}>
        <div className={styles.previous}>
          <Link href={`/${categories_list}/${previousPage}`}>
            &lt; Previous
          </Link>
        </div>
        <div className={styles.next}>
          <Link href={`/${categories_list}/${nextPage}`}>Next &gt;</Link>
        </div>
      </div>
    </div>
  );
};
export default ProductList;
