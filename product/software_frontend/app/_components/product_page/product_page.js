import React from 'react';
import Image from 'next/image';
import Product_Card from '../product_card/product_card';

const Product_Page = async ({product_unique_id}) => {
  // const res = await fetch('http://127.0.0.1:8000/softwareguru/get_product?product_unique_id='+product_unique_id);
  const res = await fetch('http://127.0.0.1:8000/softwareguru/get_products?page=1');
  if (!res.ok) {
    console.error('Failed to fetch data:', res.statusText);
    return <div>Error: Failed to fetch data</div>;
  }
  const products_data = await res.json();
  console.log("------->" , products_data)
  return (
    <div>
      {products_data.map((product_data) => (
        // {console.log("here")}
          <Product_Card product_data={product_data} key={product_data["product_id"]}/>
        ))}
    </div>
  );
};

export default Product_Page;