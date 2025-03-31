const crypto = require('crypto');
const config = require('../config/master.json');

const ALGORITHM = "aes-256-cbc";

function encrypt(text) {
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv(ALGORITHM, Buffer.from(config.key, 'hex'), iv);
    let encrypted = cipher.update(text, 'utf8', 'hex');
    encrypted += cipher.final('hex');
    return { iv: iv.toString('hex'), content: encrypted };
}

function decrypt(encrypted) {
    const decipher = crypto.createDecipheriv(
        ALGORITHM,
        Buffer.from(config.key, 'hex'),
        Buffer.from(encrypted.iv, 'hex')
    );
    let decrypted = decipher.update(encrypted.content, 'hex', 'utf8');
    decrypted += decipher.final('utf8');
    return decrypted;
}

module.exports = {encrypt, decrypt};