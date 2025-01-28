"use client"
const options = [
  {
    value: 1,
    text: "Prog_Mog_1"
  },
  {
    value: 2,
    text: "Prog_Mog_2"
  },
  {
    value: 3,
    text: "Prog_Mog_3"
  },
  {
    value: 4,
    text: "Prog_Mog_4"
  },
]

export default function Home() {
  return (
    <div id="app">
      <select name="quiz_chooser">
        {options.map(option => {
          return <option
            key={option.value}
            value={option.value}
          >{option.text}</option>
        }
        )}
      </select>
      <h1 id="quiz-title">Loading...</h1>
      <div id="quiz-container"></div>
      <button id="submit-btn" style={{ "display": "none" }}>Submit</button>
    </div>
  );
}

