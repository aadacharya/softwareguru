import React from 'react';

const Product_Page = async ({product_unique_id}) => {
  const res = await fetch('http://127.0.0.1:8000/softwareguru/get_product?product_unique_id='+product_unique_id);
  if (!res.ok) {
    console.error('Failed to fetch data:', res.statusText);
    return <div>Error: Failed to fetch data</div>;
  }
  const product_data = await res.json();
  // console.log("------->" , product_data)
  return (
    <div>
      <div>{product_data["product_summary"]}</div>
    </div>
  );
};

export default Product_Page;