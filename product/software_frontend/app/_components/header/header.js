'use client';

import React from 'react';
import Image from 'next/image';
import Link from 'next/link';
import styles from './header.module.css';
import { useRouter } from 'next/navigation';

const Header = () => {
  const router = useRouter();

  const redirectHome = () => {
    router.push('/');
  };

  return (
    <div className={styles.headerMain}>
      <div className={styles['headerLogo']} onClick={redirectHome}>
        <Image src="/logo.svg" width={150} height={150} alt="Logo"></Image>
      </div>
      <div className={styles['headerComponent']}>
        <div className={styles['headerComponentEach']}>
          {' '}
          <Link href="/">Products</Link>{' '}
        </div>
        <div className={styles['headerComponentEach']}> <Link href="/categories">Categories</Link> </div>
        <div className={styles['headerComponentEach']}> Blogs </div>
      </div>
      <div className={styles['headerMember']}>
        <div className={styles['signin']}>Sign In</div>
        <div className={styles['getstarted']}>Get Started</div>
      </div>
    </div>
  );
};

export default Header;
