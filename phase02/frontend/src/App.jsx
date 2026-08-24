import React, { useEffect, useState } from "react";

export default function App() {
  const [health, setHealth] = useState(null);
  const [items, setItems] = useState([]);
  useEffect(() => {
    Promise.all([
      fetch("/api/health").then((response) => response.json()),
      fetch("/api/items").then((response) => response.json())
    ]).then(([healthData, itemData]) => {
      setHealth(healthData);
      setItems(itemData);
    });
  }, []);
  return (
    <main>
      <h1>Phase 2 Docker Compose Web System</h1>
      <p id="health">Health: {health ? JSON.stringify(health) : "loading"}</p>
      <ul>{items.map((item) => <li key={item.id}>{item.id}: {item.message}</li>)}</ul>
    </main>
  );
}
