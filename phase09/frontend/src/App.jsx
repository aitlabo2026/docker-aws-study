import React, { useEffect, useState } from "react";

export default function App({keycloak, authenticated}) {
const [health, setHealth] = useState(null);
const [secureMessage, setSecureMessage] = useState("");
const [job, setJob] = useState(null);
const h = React.createElement;

useEffect(() => {
fetch("/api/health").then((response) => response.json()).then(setHealth);
}, []);

async function authFetch(path, options = {}) {
await keycloak.updateToken(30);
const headers = {...options.headers, Authorization: "Bearer " + keycloak.token};
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

return h("main", null,
h("h1", null, "Phase 3 Auth and Async System"),
h("p", null, "Health: " + (health ? JSON.stringify(health) : "loading")),
!authenticated && h("button", {onClick: () => keycloak.login()}, "Login"),
authenticated && h("section", null,
h("p", null, "User: " + keycloak.tokenParsed.preferred_username),
h("button", {onClick: loadSecure}, "Call Secure API"),
h("button", {onClick: createJob}, "Create Job"),
h("button", {onClick: () => keycloak.logout({redirectUri: window.location.origin})}, "Logout"),
h("p", null, "Secure: " + secureMessage),
h("p", null, "Job: " + (job ? JSON.stringify(job) : "not created"))
)
);
}