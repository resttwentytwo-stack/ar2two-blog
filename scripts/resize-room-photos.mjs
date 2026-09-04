import sharp from 'sharp';
import { readdirSync } from 'node:fs';
import { join } from 'node:path';

const dir = join(process.cwd(), 'src/assets/rooms');
const maxWidth = 1600;

for (const file of readdirSync(dir)) {
  if (!/\.(jpg|jpeg|png)$/i.test(file)) continue;
  const filePath = join(dir, file);
  const image = sharp(filePath);
  const meta = await image.metadata();
  if (!meta.width || meta.width <= maxWidth) {
    console.log(`skip (already small): ${file}`);
    continue;
  }
  const buffer = await image.resize({ width: maxWidth }).jpeg({ quality: 82 }).toBuffer();
  await sharp(buffer).toFile(filePath + '.tmp');
  const { renameSync } = await import('node:fs');
  renameSync(filePath + '.tmp', filePath);
  console.log(`resized: ${file} (${meta.width}x${meta.height} -> ${maxWidth}px wide)`);
}
