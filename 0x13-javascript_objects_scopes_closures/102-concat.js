#!/usr/bin/env node
// prettier-ignore
const fs = require('fs').promises;

// prettier-ignore
async function main () {
  const f1 = await fs.readFile(process.argv[2], 'utf8');
  const f2 = await fs.readFile(process.argv[3], 'utf8');
  await fs.writeFile(process.argv[4], f1 + f2);
}
main();
