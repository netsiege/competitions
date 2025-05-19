// 🚨 DEBUG ONLY - DO NOT DEPLOY THIS FILE 🚨

// Used for automated tests
const TEST_USER = 'ysree';
const TEST_PASS = 'duqu3IfRunAv';

fetch('/status.json')
  .then(res => res.json())
  .then(data => {
    const statusDiv = document.getElementById('status');
    statusDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
  })
  .catch(err => {
    console.error("Failed to load status:", err);
  });
