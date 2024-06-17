// Define the URL of the API endpoint
const url = 'http://127.0.0.1:8000/softwareguru/get_product?product_unique_id=feb414be-9d96-4ded-8377-49dfa8ccaa57';

// Define an async function to fetch data
async function fetchData(url) {
  try {
    // Fetch data from the API
    const response = await fetch(url);
    
    // Check if the response is OK (status code 200-299)
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the JSON data from the response
    const data = await response.json();

    // Log the JSON data to the console
    console.log('Fetched data:', data);

    // Return the data
    return data;
  } catch (error) {
    // Handle any errors that occurred during the fetch
    console.error('There was a problem with the fetch operation:', error);
    
    // Return a default value or handle the error as needed
    return {};
  }
}

// Call the fetchData function
fetchData(url);
