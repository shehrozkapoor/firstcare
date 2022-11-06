const util = require('util');
const fs = require('fs');
const path = require('path');
const exists = util.promisify(fs.exists);
const rmdir = util.promisify(fs.rmdir);
const unlink = util.promisify(fs.unlink);
const readdir = util.promisify(fs.readdir);
const mkdir = util.promisify(fs.mkdir);
const copyFile = util.promisify(fs.copyFile);

const readDirSync = (dir, filter = () => true) => {
  const rs = [];
  if (!fs.existsSync(dir)) {
    return rs;
  }
  const files = fs.readdirSync(dir);
  files.filter((filename, index) => filter(filename, index)).forEach((filename) => {
    const p = path.join(dir, filename);
    const info = fs.statSync(p);
    if (info.isDirectory()) {
      rs.push(...readDirSync(p, filter));
    } else {
      rs.push(p);
    }
  });
  return rs;
};

const deleteFileSync = async (dir) => {
  const has = await exists(dir);
  if (has) {
    const stat = fs.statSync(dir);
    if (stat.isDirectory()) {
      const files = await readdir(dir);
      if (files.length <= 0) {
        await rmdir(dir);
        return;
      }
      for (const f of files) {
        await deleteFileSync(path.join(dir, f));
      }
      return deleteFileSync(dir);
    }
    await unlink(dir);
  }
};


const copyFiles = async (source, dest, filter = () => true) => {
  const has = await exists(source);
  if (!has) {
    return;
  }
  const stat = fs.statSync(source);
  const info = path.parse(source);
  const ok = await filter(source, stat, info);
  if (ok === false) {
    return;
  }
  if (stat.isDirectory()) {
    const hasDest = await exists(dest);
    if (!hasDest) {
      await mkdir(dest);
    }
    const files = await readdir(source);
    for (const f of files) {
      await copyFiles(path.join(source, f), path.join(dest, f), filter);
    }
    return;
  }
  return copyFile(source, dest);
};


exports.readDirSync = readDirSync;
exports.copyFiles = copyFiles;
exports.deleteFileSync = deleteFileSync;
