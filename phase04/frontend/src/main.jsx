import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";
import keycloak from "./keycloak.js";

keycloak.init({onLoad: "check-sso", pkceMethod: "S256"}).then((authenticated) => {
  createRoot(document.getElementById("root")).render(
    <React.StrictMode><App keycloak={keycloak} authenticated={authenticated} /></React.StrictMode>
  );
});
