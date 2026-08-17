// API Base URL (Dynamic for localhost, file://, vs deployment)
const IS_LOCAL = (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1" || window.location.hostname === "");
const API_BASE = IS_LOCAL ? "http://127.0.0.1:8000/api" : "https://api.flyrank.com/api";

// Global state to store the current queue for context
let currentQueueContext = "No data uploaded yet.";

// ---- Navigation Logic ----
const navBtns = document.querySelectorAll('.nav-btn');
const views = document.querySelectorAll('.view-section');

navBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        // Update active button
        navBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        // Update active view
        const targetId = btn.getAttribute('data-target');
        views.forEach(v => {
            if (v.id === targetId) {
                v.classList.add('active');
            } else {
                v.classList.remove('active');
            }
        });
    });
});

// ---- Drag and Drop Upload Logic ----
const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const uploadStatus = document.getElementById('upload-status');
const browseBtn = document.getElementById('browse-btn');

browseBtn.addEventListener('click', () => fileInput.click());

dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    if (e.dataTransfer.files.length) {
        handleFileUpload(e.dataTransfer.files[0]);
    }
});

fileInput.addEventListener('change', (e) => {
    if (e.target.files.length) {
        handleFileUpload(e.target.files[0]);
        // Reset the input value so the exact same file can be uploaded again without refreshing
        e.target.value = ''; 
    }
});

async function handleFileUpload(file) {
    if (!file.name.endsWith('.csv')) {
        alert("Please upload a CSV file.");
        return;
    }
    
    if (!IS_LOCAL) {
        alert("Live Engine requires the local backend API to score files. Please clone the repository and run `python api/server.py` to use this feature.");
        return;
    }

    uploadStatus.innerText = `Scoring ${file.name}...`;
    browseBtn.style.display = 'none';
    
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch(`${API_BASE}/score`, {
            method: 'POST',
            headers: { 'X-API-Key': 'flyrank-demo-123' },
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            const errorDetail = data.detail || "Unknown API Error";
            throw new Error(errorDetail);
        }
        
        // Update Context for Chatbot
        currentQueueContext = `There are exactly ${data.scored_pages.length} URLs in this dataset. ` + JSON.stringify({
            total_urls_in_dataset: data.scored_pages.length,
            note: "Due to context limits, you are only being provided the top 50 highest priority URLs.",
            top_urls_preview: data.scored_pages.slice(0, 50)
        }); // Send metadata and top 50
        
        // Render Table
        renderTable(data.scored_pages);
        
        uploadStatus.innerText = `Success! Scored ${data.scored_pages.length} URLs.`;
        browseBtn.innerText = 'Upload Another';
        browseBtn.style.display = 'inline-block';
        
    } catch (error) {
        uploadStatus.innerText = `Error: ${error.message}`;
        uploadStatus.style.color = '#ef4444';
        browseBtn.style.display = 'inline-block';
        console.error(error);
    }
}

function renderTable(results) {
    const tbody = document.getElementById('results-body');
    tbody.innerHTML = '';

    results.forEach(row => {
        const tr = document.createElement('tr');
        
        // Action Color Mapping
        let actionClass = 'status-basement';
        if (row.action === 'Urgent Refresh') actionClass = 'status-urgent';
        if (row.action === 'Standard Review') actionClass = 'status-standard';

        const tdUrl = document.createElement('td');
        tdUrl.textContent = row.url_id;
        
        const tdProb = document.createElement('td');
        tdProb.textContent = row.decay_probability.toFixed(3);
        
        const tdAction = document.createElement('td');
        tdAction.className = actionClass;
        tdAction.textContent = row.action;
        
        tr.appendChild(tdUrl);
        tr.appendChild(tdProb);
        tr.appendChild(tdAction);
        tbody.appendChild(tr);
    });
}

// ---- Chatbot Logic ----
const chatInput = document.getElementById('chat-input');
const sendBtn = document.getElementById('send-chat');
const chatHistory = document.getElementById('chat-history');

sendBtn.addEventListener('click', sendChatMessage);
chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendChatMessage();
});

async function sendChatMessage() {
    const message = chatInput.value.trim();
    if (!message) return;

    // Append User Msg
    appendChat(message, 'user');
    chatInput.value = '';

    try {
        const response = await fetch(`${API_BASE}/chat`, {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                'X-API-Key': 'flyrank-demo-123'
            },
            body: JSON.stringify({
                message: message,
                context: currentQueueContext
            })
        });

        if (!response.ok) throw new Error("Chat API Error");

        const data = await response.json();
        appendChat(data.response, 'bot');
        
    } catch (error) {
        appendChat("Error connecting to LLaMA (Groq).", 'system');
    }
}

function appendChat(text, sender) {
    const div = document.createElement('div');
    div.classList.add('chat-msg', sender);
    div.innerText = text;
    chatHistory.appendChild(div);
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

// ---- Export Chat Logic ----
document.getElementById('export-chat').addEventListener('click', () => {
    let chatLog = "Data Analyst Helper - Chat Export\n\n";
    const messages = document.querySelectorAll('.chat-msg');
    
    messages.forEach(msg => {
        let role = "Helper";
        if (msg.classList.contains('user')) role = "You";
        if (msg.classList.contains('system')) role = "System";
        chatLog += `[${role}]: ${msg.innerText.replace(/^(Bot|Helper):\s*/, '')}\n\n`;
    });

    const blob = new Blob([chatLog], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'chat_analysis_export.txt';
    a.click();
    URL.revokeObjectURL(url);
});
