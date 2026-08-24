import React, { useEffect, useState } from "react";

export default function App({keycloak, authenticated}) {
  const [health, setHealth] = useState(null);
  const [secureMessage, setSecureMessage] = useState("");
  const [job, setJob] = useState(null);

  useEffect(() => {
    fetch("/api/health").then((response) => response.json()).then(setHealth);
  }, []);

  async function authFetch(path, options = {}) {
    await keycloak.updateToken(30);
    const headers = {...options.headers, Authorization: `Bearer ${keycloak.token}`};
    return fetch(path, {...options, headers});
  }

  async function loadSecure() {
    const response = await authFetch("/api/secure");
    setSecureMessage((await response.json()).message);
  }

  async function createJob() {
    const response = await authFetch("/api/jobs", {method: "POST"});
    setJob(await response.json());
  }

  return (
    <main>
      <h1>Phase 3 Auth and Async System</h1>
      <p>Health: {health ? JSON.stringify(health) : "loading"}</p>
      {!authenticated && <button onClick={() => keycloak.login()}>Login</button>}
      {authenticated && <section>
        <p>User: {keycloak.tokenParsed.preferred_username}</p>
        <button onClick={loadSecure}>Call Secure API</button>
        <button onClick={createJob}>Create Job</button>
        <button onClick={() => keycloak.logout({redirectUri: window.location.origin})}>Logout</button>
        <p>Secure: {secureMessage}</p>
        <p>Job: {job ? JSON.stringify(job) : "not created"}</p>
      </section>}
    </main>
  );
}
