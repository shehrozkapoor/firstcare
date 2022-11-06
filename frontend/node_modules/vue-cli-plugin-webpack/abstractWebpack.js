module.exports = class AbstractWebpack {
    constructor(options, api) {
        this.options = options;
        this.api = api;
    }

    enable () {
        return true;
    }

    isEnv (env) {
        return process.env.NODE_ENV === env;
    }

    isDevelopment () {
        return this.isEnv('development');
    }

    isProduction () {
        return this.isEnv('production');
    }

    configureWebpack (config) {
        return config;
    }

    chainWebpack () {}
};
