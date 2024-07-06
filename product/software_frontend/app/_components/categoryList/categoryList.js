import React from 'react';
import Link from 'next/link';
import styles from './categoryList.module.css';
import Category from '../category/category';

const CategoryList = ({ categoryList = [], singleCategory = false }) => {
  return (
    <div
      className={
        singleCategory ? styles['productCategory'] : styles['productCategories']
      }
    >
      {singleCategory && categoryList.length ? (
        <Category key={0} category={categoryList[0]} singleCategory />
      ) : (
        categoryList.map((item, index) => (
          <Category key={index} category={item} />
        ))
      )}
    </div>
  );
};

export default CategoryList;
