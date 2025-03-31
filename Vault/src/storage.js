const fs = require('fs');
const crypto = require('./crypto');
const path = require('path');

const DB_PATH = path.join(__dirname, '../passwords.json');

function loadDB() {
    return fs.existsSync(DB_PATH)
    ? JSON.parse(fs.readFileSync(DB_PATH))
    : [];
}

function saveDB(data) {
    fs.writeFileSync(DB_PATH, JSON.stringify(data, null, 2));
}

function addPassword(service, username, password){
    const db = loadDB();
    db.push({
        service,
        username,
        password: crypto.encrypt(password),
        createdat: new Date().toISOString()
    });
    saveDB(db);
}

function updatePassword(service, username, newPassword) {
    const db = loadDB();
    const entry = db.find(
        e => e.service === service && e.username === username
    );

    if (entry) {
        entry.password = crypto.encrypt(newPassword);
        entry.updatedAt = new Date().toISOString();
        saveDB(db);
        return true;
    }
    return false;
}

module.exports = { loadDB, addPassword, updatePassword}