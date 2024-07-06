import React from 'react';
import Link from 'next/link';
import styles from './category.module.css';

const Category = ({ key, category, singleCategory = false }) => {
  return (
    <div
      key={key}
      className={
        singleCategory
          ? styles['productCategorySingle']
          : styles['productCategory']
      }
    >
      <Link href={`/${category}/1`}>{category}</Link>
    </div>
  );
};

export default Category;
