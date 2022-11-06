const { log, chalk } = require('@vue/cli-shared-utils');
const { readDirSync } = require('./util')
const AbstractWebpack = require('./abstractWebpack')

const DEFAULT_OPTIONS = {
  dir: ['./webpack']
};

module.exports = (api, options) => {
  const pluginOptions = {
    ...DEFAULT_OPTIONS,
    ...(options.pluginOptions && options.pluginOptions.webpack),
  }
  let dirs = pluginOptions.dir;
  dirs = Array.isArray(dirs) ? dirs : typeof dirs === 'string' ? [dirs] : []
  const webpackFiles = dirs.map(dir => api.resolve(dir)).map(dir => readDirSync(dir)).flat();
  const webpackConfigs = webpackFiles
    .map(file => require(file))
    .filter(f => f.constructor === AbstractWebpack.constructor)
    .map(f => Reflect.construct(f, [options, api]))
    .filter(c => c instanceof AbstractWebpack)
    .filter(c => c.enable())

  log();
  log(`  🚀  初始化webpack配置...`);
  log(`      ${chalk.green(webpackConfigs.map(c => c.constructor.name).join('、'))}`);

  api.configureWebpack(config => webpackConfigs.forEach(c => c.configureWebpack(config)));
  api.chainWebpack(config => webpackConfigs.forEach(c => c.chainWebpack(config)));
}

module.exports.util = require('./util')
module.exports.AbstractWebpack = AbstractWebpack;
