#!/usr/bin/node

const request = require('request');

// Function to fetch movie data and characters
async function fetchCharacters (movieId) {
  try {
    // Fetch the movie details from the SWAPI using the movie ID
    const movieData = await request(`https://swapi.dev/api/films/${movieId}/`);
    const movie = JSON.parse(movieData);
    const characters = movie.characters;

    // Fetch and print each character's name
    for (const characterUrl of characters) {
      const characterData = await request(characterUrl);
      const character = JSON.parse(characterData);
      console.log(character.name);
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Check if Movie ID is provided
if (!movieId) {
  console.error('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

// Fetch and display the characters for the given Movie ID
fetchCharacters(movieId);
