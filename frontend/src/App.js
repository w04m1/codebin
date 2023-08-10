import React from "react";

function SnippetCard({ id, title, description }) {
  return (
    <div className="snippet-card" id={id}>
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

function SnippetsContainer({ snippets }) {
  return (
    <div className="snippet-container">
      <h2>Snippets</h2>
      {snippets.map((snippet) => (
        // it says to add a key prop to the snippet card, but I don't know what to use for the key prop
        // TODO:so better check that out in docs
        <SnippetCard
          key={snippet.key}
          id={snippet.id}
          title={snippet.title}
          description={snippet.description}
        />
      ))}
    </div>
  );
}

const data = [
  {
    key: 0,
    id: 1,
    title: "Python Snippet",
    description: "Snippet 1 description",
  },
  {
    key: 1,
    id: 2,
    title: "JS Snippet",
    description: "Snippet 2 description",
  },
  {
    key: 2,
    id: 3,
    title: "C++ Snippet",
    description: "Snippet 3 description",
  },
];

function App() {
  return (
    // TODO: move all that to a proper file and add fetching data via api
    <div className="App">
      <SnippetsContainer snippets={data} />
    </div>
  );
}

export default App;