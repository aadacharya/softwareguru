module.exports = {
    images: {
      domains: ['images.g2crowd.com'],
    },
  };
  // next.config.js

module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'http', // Change this to 'http' since your URL is using 'http'
        hostname: '127.0.0.1',
        port: '8000', // Include the port number
        pathname: '/media/product_images/**', // Adjust the pathname pattern
      },
    ],
  },
};
