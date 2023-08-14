import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";

function Snippet({ snippet }) {
  return (
    <div className="Snippet">
      <h3>{snippet.title}</h3>
      <p>{snippet.description}</p>
    </div>
  );
}

export default function Snippets() {
  const [snippets, setSnippets] = useState([]);
  const [error, setError] = useState(false);
  const [state, setState] = useState("");
  useEffect(() => {
    setState("Loading...");
    axios
      .get("http://localhost:8000/api/snippets/")
      .then((res) => {
        console.log(res.data);
        setState("success");
        setSnippets(res.data);
      })
      .catch((err) => {
        console.log(err);
        setState("error");
        setError(true);
      }, []);
  });
  if (state === "success") {
    return (
      <div className="Snippets">
        <h1>Snippets</h1>
        {snippets.map((snippet) => (
          <Snippet key={snippet.id} snippet={snippet} />
        ))}
      </div>
    );
  }
  if (state === "error") return <h1>{error.toString()}</h1>;
  if (state === "Loading...") return <h1>{state}</h1>;
}
