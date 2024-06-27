'use client'
import React, { useState } from 'react';
import styles from "./popup.module.css";
import Image from "next/image";

const PopUp = ({ popupText }) => {
  const [showPopup, setShowPopup] = useState(true);

  const togglePopup = () => {
    setShowPopup(!showPopup);
  };
  if (!showPopup) { 
    togglePopup
    return null}
  return (
    <div className={styles.popupMain}>
      <div className={styles["popupBody"]}>
          <div className={styles["popupIcon"]}>
          <Image height={32} width={32} src='./popupicon.svg' alt="icon"/>
          </div>
          <div className={styles["popupText"]}> {popupText}</div>
      </div><div className={styles["popupClose"]} onClick={togglePopup} > 
      <Image height={20} width={20} src='./cross.svg' alt="icon"/>
      </div>
    </div>
  );
};

export default PopUp;
