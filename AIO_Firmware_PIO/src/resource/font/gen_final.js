#!/usr/bin/env node
/**
 * Generate Traditional Chinese font - Final approach using execSync
 */

const { execSync } = require('child_process');
const fs = require('fs');

console.log("=".repeat(70));
console.log("Generating Traditional Chinese Font with 994 Characters");
console.log("=".repeat(70));

// Read characters
const chars = fs.readFileSync('tc_safe_1000.txt', 'utf8').trim();

console.log(`\nFont: GenJyuuGothic-Normal.ttf`);
console.log(`Characters: ${chars.length}`);
console.log(`\nThis will take 2-5 minutes...`);
console.log("=".repeat(70));
console.log();

// Build command - escape quotes in characters
const escapedChars = chars.replace(/"/g, '\\"');

const cmd = `npx lv_font_conv --no-compress --no-prefilter --bpp 4 --size 20 --font GenJyuuGothic-Normal.ttf --range 0x20-0x7F --symbols "${escapedChars}" --format lvgl --output ch_font20_tc.c --force-fast-kern-format --lv-font-name ch_font20_tc`;

console.log('Starting lv_font_conv...\n');

try {
    execSync(cmd, {
        stdio: 'inherit',
        shell: 'cmd.exe',
        encoding: 'utf8',
        maxBuffer: 50 * 1024 * 1024  // 50MB buffer
    });
    
    console.log('\n' + "=".repeat(70));
    console.log('SUCCESS!');
    console.log("=".repeat(70));
    
    if (fs.existsSync('ch_font20_tc.c')) {
        const stats = fs.statSync('ch_font20_tc.c');
        console.log(`\nFile: ch_font20_tc.c`);
        console.log(`Size: ${stats.size.toLocaleString()} bytes (${(stats.size / 1024).toFixed(2)} KB)`);
        console.log("=".repeat(70));
    }
} catch (error) {
    console.error('\n' + "=".repeat(70));
    console.error('ERROR: Font generation failed');
    console.error("=".repeat(70));
    console.error(error.message);
    process.exit(1);
}
