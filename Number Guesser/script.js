let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Creates the target number
const generateTarget = () => Math.floor(Math.random() * 10);

// Compares the human and computer guesses to the target number and returns true if the human wins
const compareGuesses = (humanGuess, computerGuess, targetGuess) =>
  Math.abs(targetGuess - humanGuess) <= Math.abs(targetGuess - computerGuess)
    ? true
    : false;

// If the winner was human increase their score by one, otherwise increase the computers score by one
const updateScore = (winner) =>
  winner === "human" ? humanScore++ : computerScore++;

// Increase the round number
const advanceRound = () => currentRoundNumber++;
